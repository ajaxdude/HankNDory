# Hank's checks

Hank runs these as "Run the gates in batches" in `SKILL.md` describes.

## Pre-flight scan

A mechanical pass over the design document at the candidate commit. Hank runs it with search tools or a script, reading that commit as "Freeze the document" in `SKILL.md` requires. Fix each real hit. Some hits are false, such as "above 10 ms"; leave those.

- Line-number citations: `line 12`, `lines 40-52`, `L12`, `#L12`, or `<path>:12`. Cite a decision, test, or section name instead.
- Counting and layout claims: text that counts the document's own contents or says where something sits in it, such as "the three rules", "stated once", "above", "below", or "N paragraphs away". Name the section, decision, or test instead.
- References that don't resolve: every section, decision, requirement, or test the text names must exist in the document, and every link inside the document must reach a heading.
- File paths missing at the commit: every path the document gives must exist at the candidate commit, checked for example with `git cat-file -e <commit>:<path>`, unless the document marks it as proposed.
- Duplicate sentences: the same sentence in two places, ignoring case, spacing, and punctuation. Keep one and refer to it by name.
- Unsourced quotations: every quoted passage names its source, such as a file, a decision, or who said it and when.
- Stale version references: any version of the design document other than the current one, outside Status, the Decision log, the Dory validation record, and Human approval.
- Length: the document is within the "Length limit" in `SKILL.md`.

## Diff check

The diff check reviews every change to the design document and its referenced files from the candidate commit of the last diff check that completed, not counting one that errored out or stalled, to the new candidate commit. Until a diff check has completed, it starts from the first commit a batch reviewed.

Run it in a new conversation rather than Hank's, on the model, reasoning effort, and session mode that "Choose where each reviewer runs" in `SKILL.md` requires. It is not a Dory gate, so a sub-agent is fine even when its starting context shows session files or checkpoint names from before its kickoff prompt. Give it the questions in this section, the design document's path, both commits, the findings the revision fixes, the defect classes earlier reviews found (taken from the history file), and any operating limits the user set. Tell it to read only the diff of the design document and its referenced files between the two commits, and each section the diff touches, in full, each once, to change nothing, and to send one final report with no progress messages. It returns both commits with its findings.

It answers these questions and cites the diff for every finding:

1. Does the revision fix each finding it was meant to fix?
2. Does the new text bring back a defect class that an earlier review found, including one the revision was meant to fix?
3. Does the new text contradict text the revision left unchanged?
4. Does the new text add, drop, or change an obligation without a Decision log entry that records it?
