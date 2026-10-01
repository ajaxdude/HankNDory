# Changelog

HankNDory versions use `MAJOR.MINOR`. The number appears twice in `hankndory/SKILL.md`, in the `metadata.version` frontmatter field and in the title line. Bump both together. Each version from 1.3 on has a git tag, `vMAJOR.MINOR`, so any of them can be reinstalled or restored later.

## 2.1 (2026-09-30)

A light pace and a sturdier charter, from trying 2.0's fast pace on a small release. Separate reviewers at the highest effort cost far more than one pass at Hank's effort and found little more. The budget unit was unclear, Step 7 kept sending already-decided wording to the user, and nothing protected the work against losing a machine.

- New light pace, for a point release or a design written after the code, with a design-review budget cap in the charter. It follows the fast-pace rules except where it differs. One `dory-pass` runs Steps 5 to 7. Hank fixes everything it found in one revision, the design and, on the building branch, any code it shows to be wrong, and runs his checks, the diff check included, on that revision. A second pass runs only if the first had a blocking finding, a Step 5/5b `FAIL`, or a Step 7 `NOT READY`, and the budget allows, followed by one more fix; it shares a lifetime limit of two critic rounds with any Step 8 scoped round. The charter approves the last fix revision only when the last pass had none of those three; otherwise the open findings go to the user. Step 9 runs one review and one re-review, and any finding still open goes in the digest; while a non-trivial one is open, merging and deploying stay reserved. "Always standard" items still have to be named in the charter.
- At light and fast pace, reviewers that run Step 6 or 7 run at Hank's reasoning effort unless the charter sets a higher one.
- The charter's budget is in agent-hours or cost. Agent-hours add up every agent's time, counting agents that run at the same time separately.
- New charter field, accepted as built: wording and small extensions inside a scope already decided that the user accepts without being asked. It overrides the reserved taste calls for what it names, never covers "Always standard" items, and never sends anything. Privacy, legal, and terms wording stays reserved unless named.
- Back up at every gate: Marlin pushes the design documents, the charter, their history files, and the working branches to the charter's backup remote. Only branches that aren't shared or default, never force-pushed, never to a remote where a push deploys. A public project, or one the user doesn't own, keeps its designs, charter, and history files on a private backup remote. Digests are recorded in the charter's history file.
- The README adds a tooling note: in the GitHub Copilot app, task sub-agents see the parent session's checkpoint titles and file list, so Dory reviewers run as new top-level sessions.

## 2.0 (2026-09-30)

Reaching the final objective sooner, at a pace the user chooses, and at lower cost. Work sat idle for hours waiting on routine answers and approvals, questions came one at a time, every design got the full set of separate reviews whatever its risk, and most of the cost came from Hank's own conversation growing long through the review loop. This is a major version because a charter can now make the method run faster and approve building by itself. Version 1.7 was never released; its changes are part of this one.

- Marlin returns, this time as the one who keeps the voyage moving: a role the conversation running the work plays, described in the new section "Marlin keeps the voyage moving" and the new `reference/marlin.md`. At kickoff, Marlin and the user write a charter in its own file: the final objective, milestones, deadline and budget, pace, the decisions Marlin makes alone, the decisions reserved for the user, the default wait for a reversible question (10 minutes unless the user sets another), review points, and operating limits. Only the user changes it.
- Decisions are sorted as delegated, reversible, or reserved. Marlin decides a delegated one and records it, takes a reversible one's default when its wait runs out, and waits only for a reserved one. When unsure, a decision is reserved. New core rule 12: never leave work waiting on the user for a delegated or reversible decision.
- One digest at a time replaces one-at-a-time questions: where the voyage stands against the deadline and budget, the decisions needed with recommendations and defaults, what Marlin decided, and what it is doing meanwhile. It is sent without stopping work. Marlin escalates as soon as the deadline or budget is at risk and never recommends another review round when nothing is blocking.
- Three paces, in the new section "Pick the pace". Careful keeps the 1.6 reviews. Balanced runs Steps 5, 5b, and 6 in one fresh reviewer in the new mode `dory-pass`, then Step 7, with two critic rounds in the document's whole life. Fast runs Steps 5 to 7 in one `dory-pass`, with two critic rounds, no diff check, and approval by the charter. At fast pace, building may overlap review on its own branch, on components no open finding touches, and nothing built that way merges or deploys before approval and a clean code review. A design that touches any "Always standard" item runs at careful pace unless the charter names that item. The charter is set before Step 1 of a standard change, and each version needs the user's explicit OK. Without a charter, everything runs at careful pace, nothing extra is delegated, and no question takes a default; a design started under an earlier version runs at careful pace until it gets a charter.
- Approval by the charter, at fast pace only, covers a `READY` that counts: on the same version, Steps 5 and 5b passed, Step 6 closed, every gate was certified isolated, every check returned, and no revision followed. Step 7 also lists the "Always standard" items and the steps that can't be undone that the design touches, and the charter approves only if it names them all and the design stays inside its objective, budget, and delegation. It is recorded with the charter's version and the commit it covers, and reported in the next digest. Core rule 7 no longer has a "skipped by user judgment" path: approval is explicit or comes from the charter.
- Any reviewer that runs Step 6 or Step 7 runs at Hank's reasoning effort or higher. The mean code review stays at every pace.
- The Hank handoff also carries the charter, the pace, and the open digest, and the new Hank conversation sends that digest again, keeping each default's original time.
- Behaviors to avoid adds leaving work waiting on a delegated or reversible decision, asking questions one at a time when a digest would do, and running "Always standard" work faster than careful pace without the charter naming it.
- The heading list in "Required document structure" is gone, since the template holds it, and Step 2's example questions are one paragraph, keeping `SKILL.md` under 500 lines.

From the unreleased 1.7, lower cost and faster steps with the same gates:

- A new Hank conversation writes each revision. Once a batch returns, Hank records its results and a handoff entry in the history file, and a new top-level conversation, never a fork, resume, or sub-agent, picks up from the files. Phases 1 and 2 stay in one conversation, and during building the implementing conversation revises the design itself. Only one conversation acts as Hank at a time: the new one marks the handoff entry `Taken over`, and the old one stops once it sees that mark. The user's operating limits go in the new conversation's prompt, as the user gave them. The entry carries the user decisions not yet in the design and any waiting question, which the new conversation asks again. If the tooling cannot start a new conversation, Hank shrinks the current one or carries on, and records that. The steps are in the new `reference/hank-handoff.md`. Failure recovery now also reads the latest handoff entry.
- Hank sets a stall time before starting each reviewer or check, then waits for the tooling's notice that it has finished, instead of checking on it again and again. It checks once when the stall time passes.
- Reasoning effort matches the job. Every reviewer, and the diff check, runs on a model at least as capable as Hank's. Steps 6 and 7 still run at Hank's reasoning effort or higher. Step 5/5b and the diff check may run at lower effort than Hank's, down to high or the tooling's nearest equivalent, or at Hank's effort if Hank runs below high.
- Leaner reads. The kickoff prompts for reviewers and the diff check say to read the design document in one piece, read each file at most once, and send one final report. Referenced files names the part that matters in a large file, by section or function. A review that read the history file is discarded and rerun.
- Behaviors to avoid adds carrying one Hank conversation through the whole review loop when the tooling can start a new one, and checking on a running reviewer again and again.

## 1.6 (2026-09-29)

Designs reach building sooner, and building no longer restarts review. Design reviews could run for days: discoveries made while building went back through full review, critic rounds kept going after the blocking findings were gone, the round limit restarted after each return from building, designs restated the code, and one-off jobs went through the full method.

- Applies in full to new design documents. A design started under an earlier version keeps its document as written, with no length limit, and follows the 1.6 review and building rules from its next step, counting the critic rounds it has already used.
- Test first. Before a long design, a time-limited spike can settle the riskiest assumption with a cheap, real test (new Step 3b). Spike code is throwaway, never merged, and stays within the user's operating limits. Its result goes into the design as evidence. The no-code rule covers production code.
- Right tool for the job. A new one-off tier covers operations such as a download, a conversion, a test run, a publish, or a one-time cleanup. They get a one-page checklist, the new `reference/one-off-checklist.md`, and a code review of any script before it runs, instead of the design method. Deleting files the user explicitly approved deleting, or the project's own generated or temporary files, no longer forces the full method. Migrations or deletions of user or production data still do, and a trivial change still may not affect user or production data or security. The always-standard list is now stated once, in the sizing section.
- Promises, not code. Detailed implementation states each component's responsibility, the contracts it must keep, the areas expected to change, and the build order, not every file change. File-level detail goes in the implementation log and the code review. A design document stays under 3,000 words, not counting Referenced files, unless the user OKs a longer one. Step 7 and the pre-flight scan check the length.
- No blocking findings means pass. A critic round with no blocking findings closes Step 6, even when Step 5/5b failed in the same batch. The comprehension fix then gets the diff check, a Step 5/5b rerun, and Step 7, but no new critic round. Its important findings are fixed once and verified by a diff check, with no new round, and nits are optional. Another critic round follows only a round with blocking findings, and it may be scoped to the fix. Step 6 now defines a blocking finding, and core rule 6 names blocking findings instead of material ambiguity. After a Step 7 `READY`, only blocking findings from a whole-document check lead to another revision.
- One review limit for the document's whole life. Three critic rounds in total, counting scoped rounds and rounds after returns from building. Restructuring or splitting doesn't reset the count, and more rounds need the user's explicit OK. A critic round that ran beside a failed comprehension test now counts too.
- Building doesn't restart the design. A discovery that keeps the design's promises is the implementer's call, logged in one line and covered by the code review. A discovery that breaks a promise revises only that part, followed by Hank's checks and one scoped critic round. Steps 5, 5b, and 7 rerun only if the Problem, the Goals, or the overall approach changes. The user is asked only when the scope, an approved contract, or the risk changes.
- Deadline and budget. Status records a target date, a review budget, the time spent, and the critic rounds used, and Hank escalates when review passes the date or the budget. Every escalation states the time spent, the rounds used, and what is actually blocking. When nothing is blocking, it recommends proceeding with notes, never another round.
- The diff check starts from the last commit a completed diff check covered, and it also checks that each fix resolves its finding. A late result from a stalled check that could not be stopped becomes non-blocking notes in the history file.
- The bootstrap-context steps move to `reference/bootstrap-context.md`, keeping `SKILL.md` under 500 lines.
- Behaviors to avoid adds recommending another review round when nothing is blocking, using the design method for a one-off job, and restating code in the design.

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
