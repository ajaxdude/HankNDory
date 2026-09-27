# Changelog

HankNDory versions use `MAJOR.MINOR`. The number appears twice in `hankndory/SKILL.md`, in the `metadata.version` frontmatter field and in the title line. Bump both together. Each version from 1.3 on has a git tag, `vMAJOR.MINOR`, so any of them can be reinstalled or restored later.

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
