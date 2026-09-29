# Changelog

HankNDory versions use `MAJOR.MINOR`. The number appears twice in `hankndory/SKILL.md`, in the `metadata.version` frontmatter field and in the title line. Bump both together. Each version from 1.3 on has a git tag, `vMAJOR.MINOR`, so any of them can be reinstalled or restored later.

## 1.5 (2026-09-28)

Fewer regressions between review rounds, and less waiting. Long design reviews showed revisions bringing back the defects they were meant to fix, checks holding up reviews, history crowding out the rules, reviewers seeing more than the design, and questions waiting unseen in files.

- Applies to new design documents, and to an existing document from its next substantive revision. Adopting it never by itself reopens a gate, invalidates a verdict, or voids an approval.
- Write each rule once: a design document states each rule, limit, or number in one place and refers to it by name elsewhere. No line-number citations, self-counting, layout references, or history in normative text.
- History moves to a sibling file whose first line says it is a record, not a rule. It also records each run of Hank's checks and what it found. The design keeps the Status lines since the last review, a one-line-per-review Dory index, and every decision and rejected alternative.
- Hank's checks, in the new `reference/hank-checks.md`: a mechanical pre-flight scan, and, once an earlier batch has reviewed a commit, a diff check. The diff check asks whether the revision brings back a known defect class, contradicts unchanged text, or changes an obligation without a recorded decision. It runs in a new conversation rather than Hank's, on the model, reasoning effort, and session mode the reviewer rules require. It is not a gate, so it may run in a sub-agent that can see session files or checkpoint names from before its kickoff prompt. Its kickoff prompt names both commits, the findings the revision fixes, and the defect classes earlier reviews found, and it returns both commits with its findings.
- Hank's checks run once on each version before the first batch that reviews it, on a pinned candidate commit. Hank fixes what they find and starts the batch on the fixed commit without rerunning them, to keep mistakes a fix just added away from reviewers. They are one pass, not a gate. Any other check Hank runs that reads the whole document runs alongside the batch on the batch's commit, never before it, and its findings join the batch's one revision. A check that errors out or stalls, before the batch or alongside it, holds nothing back and counts as returned. Hank stops it if it is still running, starts the batch or writes the batch's revision without it, and records the gap in the history file. When only one reviewer can run at a time, the whole-document check runs after the reviews.
- Only a Step 7 `READY` version that no revision followed goes to human approval. After a `READY`, only material findings from a whole-document check in the batch lead to a revision and another Step 7 run; the rest become non-blocking notes in the history file. Step 7 reviews at most three versions before approval; a fourth would go to the user instead.
- Every reviewer and check reads the commit it was given through `git show <commit>:<path>`, or a frozen copy outside git, never the working tree. Kickoff prompts name the commit. A reviewer or check that reports a different commit is discarded and rerun.
- A sub-agent whose starting context shows checkpoints, history, or session files from before its kickoff prompt is not isolated for a Dory review; use a new chat session instead, and record the gate as not certified if that shows them too. Reviewers report whether they saw any. Reviewer sessions start in a session mode that does not pause for plan approval.
- Stop-loss: when Hank's checks or reviewers find that two revisions in a row brought back the defect class they fix, restructure the document before the next batch. Restructuring or splitting it does not reset Step 6's round count.
- Code review: after the first round, a re-review reads the fix diff and what it could break, unless a fix touched a shared contract. Slow checks run alongside the review on the same commit, and a clean verdict counts only once they meet the bar the design's Testing and evaluation section sets; if it sets none, Hank asks the user for one right away.
- Anything that needs the user is asked right away, with a recommendation, and never left only in a file. Hank keeps doing the work every answer needs while waiting.

## 1.4 (2026-09-27)

Faster Dory phases, with the same gates.

- A Dory phase needs only a fresh conversation. A sub-agent or a new chat in the same checkout qualifies. A new worktree or clone is for when the checkout cannot stay unchanged during the review, or the review must run on another machine.
- The Step 5/5b reviewer and the first Step 6 critic round start together, against the same frozen version. Hank fixes all findings from a batch in one revision. Step 7 runs once both gates have closed.
- Kickoff prompts carry only the step, the document path and version, the user's operating limits, and what to return. They carry no design context.
- Reviewers run on a model at least as capable as Hank's, at the same or higher reasoning effort.
- A critic round that ran alongside a failed Step 5/5b does not count toward Step 6's three-round limit.
- The skill carries a version number and reports it in phase status.

## 1.3 (2026-09-27)

- Added the plain-speech pass at the end of Phase 2, with `reference/plain-speech-checklist.md` adapted from unslop.
- README: removed em dashes, and the copyright holder is now CostePartners.com.

## 1.2 (2026-09-17, commit e9e015d)

- Clarified that only Step 7's `READY` verdict pauses for human approval. Every other transition proceeds automatically.

## 1.1 (2026-09-16, commit f722396)

- Renamed to HankNDory. Hank, the septopus from *Finding Dory*, replaces Pearl as the design-phase character.

## 1.0 (2026-09-16)

- First version of the method. The design-phase character was first named Marlin, and the skill was briefly published as PearlNDory.

Versions 1.0 to 1.3 were numbered after the fact, when versioning started with 1.4.
