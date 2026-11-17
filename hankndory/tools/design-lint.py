#!/usr/bin/env python3
"""design-lint: check the Requirements and acceptance criteria section of a
HankNDory design document.

Part of the HankNDory skill (MIT). Checks the requirement format defined in
`reference/design-doc-template.md`: EARS-shaped requirements with one
`shall`, a `Because` reason, stable IDs, `Verify` blocks with `Expect`
clauses, numeric `Expect` clauses with a range or bound and a source or an
`(exact)` mark, and a 25-word-per-sentence cap. The rules follow the EARS
requirement patterns and the Simplified Technical English
principle that a specification is only useful when every reader understands
it the same way. This implementation is original, standard-library Python.

Usage:
    design-lint.py [--json] [--strict] [--self-test] [FILE ...]

Reads from stdin when a file is "-"; pipe the frozen copy, for example
`git show <commit>:<path> | design-lint.py -`.

Exit code: 0 when clean, 1 on error findings, 1 on warnings with --strict,
and 2 when an input cannot be read. Some checks are heuristics and can
report false findings; report those instead of changing a name, a quoted
passage, or a counter-example to satisfy the tool. Fenced examples and
comments inside the requirements section are linted as real text; keep
format examples outside the section. --self-test checks the checker against
built-in fixtures and reads no files.
"""

import argparse
import json
import re
import sys

EARS_STARTS = ("The", "When", "While", "If", "Where")
PATTERN_START = {
    "plain": "The",
    "event": "When",
    "state": "While",
    "unwanted": "If",
    "optional": "Where",
}
CLAUSE_RANK = {"Given": 0, "While": 0, "When": 1, "Expect": 2}
CLAUSE_WORDS = set(CLAUSE_RANK)
CLAUSE_VOCAB = "Given, While, When, Expect, or Expect no"

VAGUE_WORDS = [
    "fast", "quick", "quickly", "easy", "easily", "simple", "simply",
    "robust", "seamless", "efficient", "efficiently", "appropriate",
    "user-friendly", "intuitive", "as needed",
]
VAGUE_RE = re.compile(
    r"\b(" + "|".join(re.escape(w) for w in VAGUE_WORDS) + r")\b", re.IGNORECASE
)

REQ_RE = re.compile(
    r"^\s*(?:#{1,6}\s+|[-*+]\s+)?Requirement\s+(?P<id>R[A-Za-z0-9_.-]+)\s*"
    r"(?:\((?P<pattern>[A-Za-z-]+)\))?\s*:\s*(?P<text>.*)$"
)
BOLD_BLOCK_RE = re.compile(r"^\s*(?:[-*+]\s+)?\*\*(?P<head>.*?):\*\*\s*(?P<tail>.*)$")
RETIRED_REQ_RE = re.compile(
    r"^\s*(?:[-*+]\s+)?~~+\s*Requirement\s+(?P<id>R[A-Za-z0-9_.-]+)",
    re.IGNORECASE)
RETIRED_VERIFY_RE = re.compile(
    r"^\s*(?:[-*+]\s+)?~~+\s*Verify\s+(?P<id>V[A-Za-z0-9_.-]+)",
    re.IGNORECASE)
VERIFY_RE = re.compile(
    r"^\s*(?:#{1,6}\s+|[-*+]\s+)?Verify\s+(?P<id>V[A-Za-z0-9_.-]+)\s*"
    r"(?:\((?P<name>[^()]*(?:\([^()]*(?:\([^()]*\)[^()]*)*\)[^()]*)*)\))?"
    r"\s*:\s*(?P<text>.*)$"
)
HEADING_RE = re.compile(r"^\s*#{1,6}\s+(?P<title>.+?)\s*$")
REQ_SECTION_RE = re.compile(r"^requirements and acceptance criteria", re.IGNORECASE)
GLOSSARY_HEADING_RE = re.compile(r"^glossary\s*$", re.IGNORECASE)

CODE_SPAN_RE = re.compile(r"`[^`]*`")
# Same-character quote pairs only; an apostrophe preceded by a word
# character is possessive prose, not an opening quote.
QUOTED_RE = re.compile(
    r"(?<!\w)\"[^\"]*\"|(?<!\w)'[^']*'"
    r"|\u201c[^\u201d]*\u201d|\u2018[^\u2019]*\u2019"
)
# Note: [RV]\\d tokens double as version tokens (v2.14), so a numeric
# Expect citing a version has its digits masked; an accepted trade.
MASKED_RE = re.compile(
    r"\b(?:Requirement|Verify)?\s*[RV]\d[A-Za-z0-9_.:-]*"
    r"|\be\.g\.[.]?|\bi\.e\.[.]?|\betc\.[.]?",
    re.IGNORECASE,
)
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
SHALL_RE = re.compile(r"\bshall\b", re.IGNORECASE)
IT_AGENT_RE = re.compile(r"\bit\b\s+(?:shall|will|should)\b", re.IGNORECASE)
DIGIT_RE = re.compile(r"\d")
RANGE_RE = re.compile(r"\d+(?:[.,]\d+)?\s*[^\s,.;:]{0,8}\s*(?:-|–|—|~|to)\s*\d+|±|[<>≤≥]=?\s*\d|\d\s*[<>≤≥]|\b\w+er than\b")
BOUND_WORDS = (
    "at least", "at most", "no more than", "no fewer than", "no less than",
    "less than", "more than", "or more", "or less", "up to", "within",
    "greater than", "lower than", "higher than", "no later than", "over",
    "under", "about", "maximum of", "minimum of",
)
SOURCE_RE = re.compile(r"\(\s*source\s*:", re.IGNORECASE)
EXACT_RE = re.compile(r"\(\s*exact\s*\)", re.IGNORECASE)
CITATION_RE = re.compile(r"\(\s*(?:source|exact)[^)]*\)", re.IGNORECASE)
AND_RE = re.compile(r"\s+and\s+", re.IGNORECASE)
MAX_SENTENCE_WORDS = 25


class Finding:
    __slots__ = ("file", "line", "rule", "level", "message")

    def __init__(self, file, line, rule, level, message):
        self.file = file
        self.line = line
        self.rule = rule
        self.level = level
        self.message = message

    def as_dict(self):
        return {"file": self.file, "line": self.line, "rule": self.rule,
                "level": self.level, "message": self.message}


class Checker:
    def __init__(self, name, text):
        self.name = name
        self.lines = text.split("\n")
        self.findings = []

    def add(self, line, rule, level, message):
        self.findings.append(Finding(self.name, line, rule, level, message))

    # ---------- text helpers ----------

    @staticmethod
    def mask(text):
        """Blank out code spans, quotations, IDs, and abbreviation dots so
        the pattern checks see only the specification prose."""
        text = CODE_SPAN_RE.sub(lambda m: " " * len(m.group(0)), text)
        text = QUOTED_RE.sub(lambda m: " " * len(m.group(0)), text)
        return MASKED_RE.sub(lambda m: " " * len(m.group(0)), text)

    @staticmethod
    def sentences(text):
        return [s.strip() for s in SENTENCE_SPLIT_RE.split(text.strip()) if s.strip()]

    # ---------- document walk ----------

    def check(self):
        in_section = False
        has_section = False
        has_glossary = False
        requirements = []
        retired = {}
        current = None
        verify = None

        def flush():
            nonlocal current, verify
            if current is not None:
                requirements.append(current)
            current = None
            verify = None

        for idx, raw in enumerate(self.lines, start=1):
            line = raw.rstrip("\r")
            bold = BOLD_BLOCK_RE.match(line)
            block_line = bold.group("head") + ": " + bold.group("tail") \
                if bold else line
            heading = HEADING_RE.match(line)
            heading_is_block = False
            if heading and in_section and (REQ_RE.match(line)
                                           or VERIFY_RE.match(line)):
                heading_is_block = True
            if heading and not heading_is_block:
                title = heading.group("title")
                if REQ_SECTION_RE.match(title):
                    has_section = True
                    flush()
                    in_section = True
                elif in_section:
                    flush()
                    in_section = False
                if GLOSSARY_HEADING_RE.match(title):
                    has_glossary = True
                continue

            if not in_section:
                continue

            retired_match = (RETIRED_REQ_RE.match(line)
                             or RETIRED_VERIFY_RE.match(line))
            if retired_match:
                retired[retired_match.group("id")] = idx
                continue

            req_match = REQ_RE.match(block_line)
            if req_match:
                flush()
                current = {
                    "id": req_match.group("id"),
                    "pattern": (req_match.group("pattern") or "").lower(),
                    "line": idx,
                    "text": [req_match.group("text")],
                    "verifies": [],
                }
                continue

            verify_match = VERIFY_RE.match(block_line)
            if verify_match:
                if current is None:
                    self.add(idx, "orphan-verify", "error",
                             "A Verify block appears before any Requirement.")
                    continue
                verify = {
                    "id": verify_match.group("id"),
                    "line": idx,
                    "clauses": [],
                }
                current["verifies"].append(verify)
                if verify_match.group("text").strip():
                    verify["clauses"].append(
                        (idx, verify_match.group("text").strip()))
                continue

            if verify is not None:
                if not line.strip():
                    continue
                clause = re.sub(r"^\s*(?:[-*+]\s+)+", "", line.strip())
                head = re.sub(r"\*\*", "", clause).split(" ", 1)[0]
                head = re.sub(r"[.:]$", "", head)
                indented = line[:1] in (" ", "\t")
                if verify["clauses"] and indented and \
                        head not in CLAUSE_WORDS:
                    first, prev = verify["clauses"][-1]
                    verify["clauses"][-1] = (first, prev + " " + clause)
                else:
                    verify["clauses"].append((idx, clause))
                continue
            if current is not None and line.strip():
                stripped = re.sub(r"^\s*[-*+]\s+", "", line.strip())
                current["text"].append(stripped)
                continue

        flush()

        if not has_section:
            self.add(1, "missing-section", "warn",
                     'No "Requirements and acceptance criteria" section.')
            return self.findings
        if not requirements:
            self.add(1, "no-requirements", "warn",
                     "The requirements section has no `Requirement R<n>:` "
                     "lines in the requirement format.")
        if not has_glossary:
            self.add(1, "no-glossary", "warn",
                     "No Glossary section; the core rule One word, one "
                     "meaning wants one.")

        seen_ids = dict(retired)
        for req in requirements:
            self.check_requirement(req, seen_ids)
        return self.findings

    # ---------- per-requirement checks ----------

    def check_requirement(self, req, seen_ids):
        req_id = req["id"]
        if req_id in seen_ids:
            self.add(req["line"], "duplicate-id", "error",
                     f"Requirement {req_id} repeats the ID first used on "
                     f"line {seen_ids[req_id]}; IDs are stable and never "
                     "reused.")
        seen_ids[req_id] = req["line"]

        raw = " ".join(CODE_SPAN_RE.sub(lambda m: " " * len(m.group(0)), text)
                        for text in req["text"]).strip()
        masked = self.mask(raw)
        sentences = self.sentences(masked)
        obligation = [s for s in sentences if not re.match(r"Because\b", s)]
        if not any(re.match(r"Because\b", s) for s in sentences):
            self.add(req["line"], "no-because", "error",
                     f"Requirement {req_id} has no Because sentence with the "
                     "reason a reviewer needs.")

        joined = " ".join(obligation)
        shalls = SHALL_RE.findall(joined)
        if len(shalls) != 1:
            self.add(req["line"], "one-shall", "error",
                     f"Requirement {req_id} uses shall {len(shalls)} times; "
                     "one requirement carries exactly one obligation.")
        if len(obligation) > 1:
            self.add(req["line"], "one-sentence", "error",
                     f"Requirement {req_id} is {len(obligation)} obligation "
                     "sentences; keep the obligation to one sentence and put "
                     "notes in the Because sentence.")
        if obligation:
            first = obligation[0].lstrip()
            if not first.startswith(EARS_STARTS):
                self.add(req["line"], "ears-pattern", "error",
                         f"Requirement {req_id} does not start with The, "
                         "When, While, If, or Where.")
            elif req["pattern"]:
                want = PATTERN_START.get(req["pattern"])
                if want is None:
                    self.add(req["line"], "unknown-pattern-tag", "warn",
                             f"Requirement {req_id} tags an unknown pattern "
                             f"'{req['pattern']}'; use plain, event, state, "
                             "unwanted, or optional.")
                elif not first.startswith(want):
                    self.add(req["line"], "tag-mismatch", "error",
                             f"Requirement {req_id} is tagged "
                             f"({req['pattern']}); its sentence must start "
                             f"with '{want}', not '{first.split()[0]}'.")
            if first.startswith("If") and not re.search(r",\s*then\b", first,
                                                         re.IGNORECASE):
                self.add(req["line"], "if-then", "error",
                         f"Requirement {req_id} opens with If but has no "
                         "then clause.")
        if IT_AGENT_RE.search(joined):
            self.add(req["line"], "name-system", "error",
                     f"Requirement {req_id} says it shall; name the acting "
                     "system instead.")
        response_half = re.split(r"\bshall\b", joined, maxsplit=1,
                                 flags=re.IGNORECASE)[-1]
        if response_half and AND_RE.search(response_half):
            self.add(req["line"], "compound-obligation", "warn",
                     f"Requirement {req_id} joins clauses with \"and\" "
                     "after shall; if it joins two responses, split it "
                     "into two requirements.")

        for sentence in sentences:
            words = sentence.split()
            if len(words) > MAX_SENTENCE_WORDS:
                self.add(req["line"], "long-sentence", "warn",
                         f"Requirement {req_id} has a {len(words)}-word "
                         f"sentence; keep it to {MAX_SENTENCE_WORDS}.")
            vague = VAGUE_RE.findall(sentence)
            if vague:
                self.add(req["line"], "vague-word", "error",
                         f"Requirement {req_id} uses a vague word "
                         f"({', '.join(sorted(set(w.lower() for w in vague)))}); "
                         "use a number and a unit with a source.")

        if not req["verifies"]:
            self.add(req["line"], "no-verify", "error",
                     f"Requirement {req_id} has no Verify block; an "
                     "unverifiable requirement is not a requirement.")
        for block in req["verifies"]:
            self.check_verify(req_id, block, seen_ids)

    # ---------- per-verify checks ----------

    def check_verify(self, req_id, block, seen_ids):
        vid = block["id"]
        if vid in seen_ids:
            self.add(block["line"], "duplicate-id", "error",
                     f"Verify {vid} repeats the ID first used on line "
                     f"{seen_ids[vid]}; IDs are stable and never reused.")
        seen_ids[vid] = block["line"]

        ranks = []
        expects = 0
        when_count = 0
        for line_no, clause in block["clauses"]:
            stripped = re.sub(r"^(?:[-*+>]\s+)+", "", clause.strip())
            stripped = re.sub(r"\*\*([^*]+)\*\*", r"\1", stripped)
            masked = self.mask(stripped)
            words = masked.split()
            if not words:
                continue
            head = re.sub(r"[.:]$", "", words[0])
            if head not in CLAUSE_WORDS:
                self.add(line_no, "unknown-clause", "warn",
                         f"Verify {vid} clause starts with '{head}'; use "
                         f"{CLAUSE_VOCAB}.")
                continue
            ranks.append(CLAUSE_RANK[head])
            if head == "Expect":
                expects += 1
                body = masked[len(words[0]):].strip()
                if AND_RE.search(body):
                    self.add(line_no, "one-assertion", "warn",
                             "An Expect joins checks with and; one Expect is "
                             "one assertion.")
                self.check_numeric(line_no, vid, body)
            elif head == "When":
                when_count += 1
            if len(words) > MAX_SENTENCE_WORDS:
                self.add(line_no, "long-sentence", "warn",
                         f"Verify {vid} has a {len(words)}-word clause; keep "
                         f"it to {MAX_SENTENCE_WORDS} words.")
        if when_count == 0:
            self.add(block["line"], "no-when", "error",
                     f"Verify {vid} has no When clause; name the trigger.")
        if expects == 0:
            self.add(block["line"], "no-expect", "error",
                     f"Verify {vid} has no Expect; name the observation that "
                     f"proves requirement {req_id}.")
        if ranks != sorted(ranks):
            self.add(block["line"], "clause-order", "error",
                     f"Verify {vid} clauses are out of order: Given/While, "
                     "then When, then Expect.")

    def check_numeric(self, line_no, vid, body):
        if EXACT_RE.search(body):
            return
        scanned = CITATION_RE.sub(" ", body)
        if not DIGIT_RE.search(scanned):
            return
        lowered = scanned.lower()
        bounded = (bool(RANGE_RE.search(scanned))
                   or any(w in lowered for w in BOUND_WORDS))
        if not bounded:
            self.add(line_no, "numeric-range", "error",
                     f"Verify {vid} expects a number without a range, a "
                     "bound, or (exact); an unbounded number is a guess.")
        elif not SOURCE_RE.search(body):
            self.add(line_no, "numeric-source", "warn",
                     f"Verify {vid} has a number without (source: ...); "
                     "cite the measurement, calculation, model, or card.")


SELF_TEST_DOCS = {
    "clean": """# Doc
## Glossary
- gateway, session.
## Requirements and acceptance criteria
Requirement R1 (event): When a request fails three times, the gateway shall lock the session.
Because repeats can show an attack.
Verify V1.1 (lockout):
- Given an open session.
- When three requests fail in sequence.
- Expect the session state is locked.
- Expect no token in the response.
Requirement R2 (unwanted): If the queue is full, then the gateway shall reject the job.
Because callers must back off.
Verify V2.1 (reject):
- Given a queue at capacity.
- When a job arrives.
- Expect the response status to be 400 (exact).
- Expect the response time to be 80 ms to 120 ms (source: load test LT-3).
**Requirement R3 (plain):** The gateway shall log each rejection.
Because audits need the trail.
Verify V3.1 (log (cold (cache) test) case):
- Given a logged request.
- When the gateway rejects it.
- Expect one log line.
- Expect no data loss (source: RFC 2119).
""",
    "dirty": """# Doc
## Requirements and acceptance criteria
Verify V0.1 (orphan):
- Given nothing.
Requirement R1 (event): The gateway shall reject input and it shall be fast.
Requirement R1 (plain): The cache shall evict entries and shall log the eviction.
Because memory is limited.
Verify V1.1:
- Expect entries are evicted.
- When the cache is full.
- Then the world turns.
Requirement R2: If the queue fills up the worker shall drop nothing.
Verify V2.0:
- Given an idle system.
Requirement R3 (state): While draining, the worker shall take 5 jobs.
Because fairness.
Verify V3.1:
- Given draining.
- When a job waits 9 seconds.
- Expect the wait to be 9 seconds and the
  job accepted.
Requirement R4 (plain): All exports shall be recorded.
Because audits need records.
Requirement R5 (whenever): The worker shall retry once.
Because networks fail.
Requirement R6 (plain): The worker shall retry once. It shall log the retry.
Because networks fail.
- ~~Requirement R8 (plain): The old worker shall drop the retry.~~
Requirement R8 (plain): The worker shall log the retry.
Because audits need retries.
Verify V8.1:
- When a retry runs.
- Expect one log line.
- ~~Verify V8.2 (old):~~
Requirement R9 (plain): The worker shall flush the queue.
Because shutdown.
""",
    "nosection": "# Doc\n\n## Goals\n\nNothing here.\n",
    "noformat": "# Doc\n\n## Requirements and acceptance criteria\n\nSome prose, no format.\n",
}

SELF_TEST_EXPECT = {
    "clean": set(),
    "dirty": {
        "orphan-verify", "no-because", "one-shall", "tag-mismatch",
        "name-system", "vague-word", "no-verify", "duplicate-id",
        "unknown-clause", "clause-order", "if-then", "no-when", "no-expect",
        "no-glossary", "one-assertion", "numeric-range",
        "compound-obligation", "ears-pattern", "unknown-pattern-tag",
        "one-sentence",
    },
    "nosection": {"missing-section"},
    "noformat": {"no-requirements", "no-glossary"},
}


def run_self_test():
    """Check the checker: the clean document must pass, and each planted
    document must raise exactly the rules it plants."""
    failed = 0
    for name, doc in SELF_TEST_DOCS.items():
        got = {finding.rule for finding in Checker(name, doc).check()}
        want = SELF_TEST_EXPECT[name]
        missing = want - got
        extra = got - want
        if missing or extra:
            failed += 1
            print(f"self-test {name}: missing {sorted(missing)} "
                  f"unexpected {sorted(extra)}")
    if failed:
        print(f"design-lint: self-test FAILED ({failed} fixtures)")
        return 1
    print("design-lint: self-test ok")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="design-lint",
        description="Check the requirements section of a HankNDory design "
                    "document. See the module docstring.")
    parser.add_argument("files", nargs="*",
                        help="design document(s), or - for stdin")
    parser.add_argument("--json", action="store_true", help="report as JSON")
    parser.add_argument("--strict", action="store_true",
                        help="treat warnings as failures")
    parser.add_argument("--self-test", action="store_true",
                        help="check the checker against built-in fixtures")
    args = parser.parse_args(argv)

    if args.self_test:
        return run_self_test()
    if not args.files:
        parser.error("no input files")

    all_findings = []
    io_error = False
    for path in args.files:
        text = None
        if path == "-":
            try:
                text = sys.stdin.buffer.read().decode("utf-8")
            except UnicodeDecodeError as error:
                print(f"design-lint: {path}: not valid UTF-8: {error}",
                      file=sys.stderr)
        else:
            try:
                with open(path, encoding="utf-8") as handle:
                    text = handle.read()
            except OSError as error:
                print(f"design-lint: {path}: {error}", file=sys.stderr)
            except UnicodeDecodeError as error:
                print(f"design-lint: {path}: not valid UTF-8: {error}",
                      file=sys.stderr)
        if text is None:
            io_error = True
            continue
        all_findings.extend(Checker(path, text).check())

    if args.json:
        json.dump([f.as_dict() for f in all_findings], sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        for finding in all_findings:
            print(f"{finding.file}:{finding.line}: {finding.level}: "
                  f"[{finding.rule}] {finding.message}")
        if not all_findings and not io_error:
            print("design-lint: no findings")

    errors = sum(1 for f in all_findings if f.level == "error")
    warnings = sum(1 for f in all_findings if f.level == "warn")
    if io_error:
        return 2
    return 1 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
