---
name: hankndory
description: apply the hank-and-dory method to design, validate, implement, and review software features with ai. use when starting or changing a feature, creating a design document before coding, testing whether a design is self-contained in a fresh session, reviewing implementation readiness, implementing from an approved design, performing an adversarial code review, or bootstrapping hierarchical readme context for an existing codebase. enforce explicit no-code gates and treat the validated design document as the source of truth.
license: MIT
metadata:
  version: "2.5"
---

# HankNDory 2.5: The Hank & Dory Method

Named for the fish who forgets everything yet still finds her way by trusting what is written down. Use a context-rich **Hank phase** to co-design a feature and create its source-of-truth design document. Hank has the whole tank mapped out and refuses to move until the plan is sound. Use independent, context-free **Dory phases** to test whether that document is complete, critical, and implementation-ready on its own. Dory has no memory of the Hank conversation and must trust only what is written down. A **Marlin** role keeps the whole voyage moving toward Nemo, the final objective the user sets. It starts all allowed work at once, in parallel, and never waits on the user for anything the user has delegated. A **Crush** role routes heavy work onto the machines the user shares across projects, and gathers every voyage's updates into one report. Write production code only after every required gate passes.

## Core rules

1. Treat the design document like source code, versioned and reviewed, and as the authoritative record of the feature.
2. Keep the Hank phase and every Dory phase logically isolated. Run each Dory phase in a fresh conversation that starts with no history, never as a continuation of the Hank conversation. A sub-agent or a new chat in the same checkout counts; a new worktree, clone, or machine is not required. A Dory phase may use only the design document and files explicitly referenced by it.
3. Do not write production code before the implementation gate passes, except where "Pick the pace" lets building overlap review.
4. Ask hard questions, challenge assumptions, and explain reasoning. Do not merely agree.
5. Separate facts verified from repository files from assumptions, proposals, and open questions.
6. Never claim a gate passed if blocking findings, missing context, unresolved decisions, or unverified file references remain.
7. Get human approval before building, either explicitly or, at light or fast pace, through the charter, as Step 7 describes. Never infer approval any other way.
8. Preserve decisions and rejected alternatives in the design document so later sessions do not reopen settled questions without new evidence.
9. Inspect referenced files before making claims about the current system. Do not invent paths, APIs, schemas, dependencies, or behavior.
10. Building does not restart the design. Handle each implementation discovery as Step 8 describes, and revise only the part of the design whose promises it breaks.
11. Size every request before choosing a mode, as "Size the change before choosing a gate set" describes, and use the lightest method that fits.
12. Keep moving toward the final objective. At every pace, start at once all work the charter and current approvals allow, and run independent work in parallel. Never leave work waiting on the user for a decision the charter delegates or that has a reversible default, as "Marlin keeps the voyage moving" describes.

## Determine the requested operating mode

Choose one mode from the user's request and current repository state:

- **new-feature-hank**: co-design a new feature and create or improve its design document.
- **dory-comprehension**: test whether a fresh engineer can understand the feature and relevant current system, and whether that understanding survives a plain-language rewrite with nothing lost.
- **dory-critic**: adversarially review the design for omissions, faulty assumptions, edge cases, risks, and ambiguity.
- **dory-readiness**: decide whether the design contains everything needed for a first-pass implementation.
- **dory-pass**: at balanced, light, or fast pace, run the Dory steps that "Pick the pace" names, in one fresh conversation.
- **implementation**: implement only from a validated and approved design document.
- **mean-review**: perform a severe but actionable code review against the approved design or a one-off operation's checklist.
- **bootstrap-context**: create a hierarchy of repository README files through bottom-up recursive summarization, following `reference/bootstrap-context.md`.
- **crush**: act as the user's Crush, following `reference/crush.md`; it reports no phase or gate, and runs under house rules, not a charter.
- **full-voyage**: orchestrate all applicable phases in order, with Marlin keeping the voyage moving, running the Dory gates in batches as described in "Dispatch Dory reviews."

If the user asks to code a standard change but no validated design exists, do not implement. Explain the missing gate and begin or recommend `new-feature-hank`.

## Size the change before choosing a gate set

Before starting a mode, classify the requested work and use the lightest tier that fits:

- **Trivial**: a small, local, reversible code change with no effect on user or production data, security, or shared behavior, and nothing under "Always standard", for example a copy fix, a log message, a constant, or an isolated single-file bug fix with an obvious repair.
- **One-off**: an operation that runs once, leaves no code to maintain, and has nothing under "Always standard", for example a download, a conversion, a test run, a publish, or a one-time cleanup.
- **Standard**: everything else, including any change whose blast radius is unclear.

**Always standard**: work that touches public APIs or schemas, authentication or authorization, migrations or deletions of user or production data, billing, security boundaries, or cross-team or cross-repository contracts. Deleting files the user explicitly approved deleting, or the project's own generated or temporary files, is not on this list unless those files hold user or production data.

For a trivial change, skip the full Hank/Dory cycle: make the change directly, add or update tests, and record in the commit or PR what was changed and why full design rigor was unnecessary. Still perform the mean code review (Step 9) before calling it done.

For a one-off operation, skip the design method. Fill in a copy of `reference/one-off-checklist.md` in this skill, a one-page checklist of steps, checks, stop conditions, and undo. Run the mean code review (Step 9) on any script it uses before that script runs, then work through the checklist. If the operation turns out to leave code to maintain or to need anything under "Always standard", stop and reclassify it.

For a standard change, run the full method starting at `new-feature-hank`.

When the size is uncertain, treat the work as standard, or ask the user before choosing a lighter tier. Record the classification and its reason in the design document's `Status` section, in the implementation log for a trivial change, or in the checklist for a one-off operation.

## Maintain workflow state

At the start of each response, determine and report only the current phase, the active gate, and what is needed next. Track these states in the design document when possible:

- `drafting`
- `comprehension-failed`
- `critic-revisions-required`
- `readiness-blocked`
- `ready-for-human-review`
- `approved-for-implementation`
- `implementing`
- `implementation-complete`
- `review-revisions-required`
- `complete`

When one batch fails more than one gate, record the earlier gate's state: `comprehension-failed` takes precedence over `critic-revisions-required`.

Do not infer approval. It must be explicit, or given by the charter as Step 7 describes.

Human approval gates exactly one state transition: `ready-for-human-review` to `approved-for-implementation`, triggered by Step 7's `READY` verdict. At light or fast pace, the charter can give that approval, as Step 7 describes. Every other transition proceeds automatically once the relevant reviewers return their results. That includes a Dory phase reporting its verdict back to Hank, starting the next batch of Dory reviews, successive critic rounds, and moving on to Step 7. Do not pause for user confirmation at these internal transitions. Anything that needs the user goes in the digest, and only work that depends on a reserved answer waits.

This version applies in full to new design documents. A design started under an earlier version keeps its document as written. From its next step it follows this version's review and building rules, counting the critic rounds it has already used, and it runs at careful pace until the user sets a charter for it. Adopting this version never by itself reopens a gate, invalidates a verdict, or voids an approval.

# Marlin keeps the voyage moving

Marlin crossed an ocean to find Nemo and never stopped to wait. Marlin is a role, not a separate conversation: the conversation acting as Hank plays it, and a Hank handoff passes it on. Marlin keeps the work moving toward the final objective, following `reference/marlin.md` in this skill:

- Set the charter with the user once, at kickoff: the final objective, milestones, deadline, budget, pace, the decisions Marlin makes alone, the decisions reserved for the user, what the user accepts as built, the default wait, review points, operating limits, any limit on parallel streams, the shared machines, the backup remote, and where Dory's update goes. Only the user changes it.
- Sort each decision as delegated, reversible, or reserved. Decide a delegated one, take a reversible one's default when its wait runs out, and wait only for a reserved one.
- Ask through one digest at a time, in a way that does not stop work, and meanwhile start everything allowed at once, in parallel, as `reference/marlin.md` describes. Give every question its recommendation first, then two to four plain sentences of context: what it is, why it needs deciding now, and what each option changes for the user.
- Send or post Dory's update, a table of what was just done, what is happening now in each stream, what comes next, and the share done with the forecast finish, only when there is new progress; an hourly wake-up checks, and waiting is not progress. Write everything addressed to the user in plain words, naming things instead of using internal labels. Open each digest with where the voyage stands, and escalate as soon as the deadline or budget is at risk. Back up at every gate, as `reference/marlin.md` describes. At kickoff, make sure the user's one Crush exists, creating it if not. Crush gathers every voyage's updates into one report for the user, and heavy work on a shared machine is booked through it, as `reference/crush.md` describes.

## Pick the pace

The charter sets each design's pace. Set the charter before Step 1 of a standard change, or record in Status that the user declined one. A design that touches any "Always standard" item runs at careful pace as a whole unless the charter names that item and gives it a faster pace; a pace set for all work does not name it. Without a charter, use careful pace, delegate nothing beyond this skill's own rules, and let no question take a default; questions still go in a digest that does not stop other work, allowed work still starts at once and in parallel, and Dory's update still goes to the chat the user reads.

| | Light | Fast | Balanced | Careful |
|---|---|---|---|---|
| Dory reviewers per batch | one `dory-pass`: Steps 5, 5b, 6, and 7 | one `dory-pass`: Steps 5, 5b, 6, and 7 | one `dory-pass`: Steps 5, 5b, and 6; then Step 7 | Step 5/5b and Step 6 in separate reviewers; then Step 7 |
| Critic rounds in the document's whole life | one, and at most two, as the light-pace rule says | two | two | three |
| Hank's diff check | on the fix revision | no | yes | yes |
| Approval before building | the charter, as Step 7 describes | the charter, as Step 7 describes | explicit | explicit |
| Building overlaps review | yes | yes | no | no |

When building overlaps review, and while the design stays inside the charter, building may start as soon as a `dory-pass` returns, on its own branch, on any component that no blocking finding, Step 5/5b gap, or Step 7 item touches, while Hank revises and the next pass runs. Nothing built this way merges into a shared branch or deploys until the design is approved and Step 9 is clean. If a revision then changes that component's contracts, rework it as Step 8 describes.

Light pace suits a point release or a design written after the code. It follows every fast-pace rule except where this paragraph differs; without a design-review budget cap in the charter, use fast pace instead. Hank fixes everything a pass found in one revision: the design, and, on a building branch, any code the pass shows to be wrong. Run Hank's checks, the diff check included, on that revision. If the pass had a blocking finding, a Step 5/5b `FAIL`, or a Step 7 `NOT READY`, a second pass runs on the fixed revision if the design-review budget allows, followed by one more fix under the same rules; this second pass and any Step 8 scoped round share a lifetime limit of two critic rounds. The charter approves only when the last pass had none of those three. It then approves that pass's fix revision, or the pass's own version if it found nothing, in place of a `READY` that no revision followed, within the limits Step 7 sets for fast pace. Otherwise the open findings go to the user. Step 9 runs one review and one re-review, which follows Step 9's rule on scope; any finding still open goes in the digest, and while a non-trivial one is open, merging and deploying stay reserved whatever the charter delegates.

# Phase 1: Hank Surveys the Tank

## Step 1: Load and verify context

For an existing project:

1. Identify the relevant design documents, repository areas, architecture notes, tests, configuration, interfaces, and adjacent features.
2. Read the smallest sufficient set of authoritative files first. Use README hierarchy files when available, then inspect source files needed to verify behavior.
3. Produce a concise current-system model covering:
   - purpose and user-visible behavior;
   - relevant components and boundaries;
   - data flow and control flow;
   - public interfaces and integration points;
   - constraints, invariants, and failure behavior;
   - tests and operational concerns.
4. Cite repository paths for every material claim.
5. Ask the user to correct misunderstandings and incorporate corrections before moving on.

For a greenfield project, record that no existing-system bootstrap is required and continue.

## Step 2: Enforce the no-code rule

During discovery and design discussion:

- Do not create or edit production code. A throwaway spike under Step 3b is not production code.
- Do not generate implementation-ready functions, classes, patches, or commands that would bypass design.
- Outside a Step 3b spike, allow only short pseudocode when prose cannot communicate the idea clearly.
- Ask clarifying questions in small, prioritized batches.
- Challenge goals, scope, constraints, assumptions, success criteria, migration needs, failure modes, and operational impact.
- Distinguish must-haves from preferences and future extensions.
- Define how the finished feature will be evaluated before selecting an implementation.

Useful questions ask: what problem must change, and for whom; what observable outcome proves success; what is out of scope; what current behavior must stay the same; which inputs are untrusted, partial, delayed, duplicated, or out of order; what happens on retries, partial failure, cancellation, rollback, or recovery; which compatibility, privacy, security, accessibility, latency, cost, and operability limits apply; and which file or evidence shows each assumption is true.

Continue until the problem, constraints, and acceptance criteria are crisp enough to compare designs.

## Step 3: Apply the sycophant challenge

Act as a critical collaborator:

1. State the strongest argument against the current framing.
2. Identify at least one plausible alternative interpretation.
3. Ask which belief has the weakest evidence.
4. Surface hidden coupling, irreversible choices, and second-order effects.
5. Explain why each major recommendation follows from verified constraints.

If the conversation becomes agreeable without adding scrutiny, explicitly reset into critic mode. Never use hostility toward the user; be demanding about the design, evidence, and reasoning.

## Step 3b: Test the riskiest assumption first

Before writing a long design, ask whether a cheap, real test could settle the assumption with the weakest evidence, such as whether a library supports a needed feature or a tool works on the target platform. If one could, run it as a spike:

- set a time limit before starting, and stop when it runs out;
- keep the spike's code out of the production codebase, never merge it, and throw it away when done;
- stay within the user's operating limits, and ask first if the test needs anything they have not allowed;
- record the question, how it was tested, and the result in the design document as evidence, with enough detail to judge the result without the spike code.

If no cheap test exists, keep the assumption as an open question or a risk and continue.

## Step 4: Propose the first technical approach

After the problem is sufficiently defined, propose the first design before asking the user to supply one. This tests understanding and reduces anchoring.

The proposal must use prose and may include a block diagram. Cover:

- architecture and component responsibilities;
- end-to-end data and control flow;
- interfaces and contracts;
- state, persistence, consistency, and concurrency;
- errors, retries, idempotency, rollback, and recovery;
- security, privacy, observability, performance, and cost;
- rollout, migration, backward compatibility, and testing;
- major decisions, tradeoffs, and rejected alternatives;
- mapping from requirements to design elements.

For every claim about the current codebase, reference the verifying file. Mark unverified claims as open questions, not facts.

Debate and revise until no material design decision is unresolved.

# Phase 2: Write the Tank Chart

Create or update one markdown design document in the repository. Build it section by section rather than relying on a one-shot draft. Use a stable path agreed with the user, such as `docs/design/<feature-name>.md`.

## Required document structure

Start every new design document from `reference/design-doc-template.md` in this skill, unless repository conventions require a stricter template. The template lists the required sections, with guidance for each.

### Length limit

Keep the design document under 3,000 words, not counting the Referenced files list. Every Dory reviewer and the human approver read the whole document, so each extra page adds time to every round. If the design cannot fit, split the feature, or record in Status the user's explicit OK for a longer document. A design started under an earlier version of this skill has no length limit.

### Status

State the current workflow state from "Maintain workflow state", the change classification from "Size the change before choosing a gate set", and the pace and the charter's path and version the design runs under. Record a target date for approval and a review budget in hours or cost, taken from the charter, or set with the user when there is none. Keep a running count of the time spent and the critic rounds used, and escalate to the user as soon as review passes the target date or uses up the budget. Add one line per substantive revision since the document was last reviewed, formatted `vN — YYYY-MM-DD — <what changed>`, and move older lines to the history file. Bump the version whenever a Dory phase or human reviewer needs to know what changed; do not bump it for typo fixes. Each entry in the "Dory validation record" must state which version it reviewed.

### Problem

Write a plain-language description, usually 3 to 5 sentences, that a casual reader can understand. State the affected user, present pain, desired change, and why it matters.

### Technical plan

Explain the major components and how they fit together in jargon-light prose. Include a block diagram when relationships or flows would otherwise be ambiguous.

### Alternatives considered

For each serious alternative, include:

- summary;
- benefits;
- costs and risks;
- reason rejected or deferred;
- evidence or constraint behind the decision.

Never erase rejected alternatives merely because a preferred design was chosen.

### Detailed implementation

State the promises the code must keep, not the code. For each component, give:

- its responsibility;
- the contracts it must keep: interfaces, schemas, invariants, and error behavior;
- the areas expected to change, such as modules or directories, naming a file only where a contract lives in it.

Then give the build order, with dependencies and checkpoints. Do not list every file change; that detail belongs in the implementation log and the code review. Do not invent a path. Mark a path as proposed until repository inspection verifies it.

### Referenced files

List every file needed by a fresh session to understand and implement the plan. Briefly state why each is required and, for a large file, which part matters, named by section or function rather than by line number. Remove stale or incidental references.

### Dory validation record

Keep one line per independent review here, giving its type, the version it reviewed, and its verdict. Record the full entry in the history file, with:

- review type;
- document version and commit reviewed;
- date, batch, or run identifier if available;
- inputs provided;
- verdict;
- blocking findings;
- document changes made;
- remaining non-blocking notes.

## Keep history out of the rules

Keep the full revision list, the gate history, and the full Dory validation entries in a sibling history file, such as `docs/design/<feature-name>.history.md`, whose first line reads "This file is a record, not a rule." The gate history includes each run of Hank's checks (see "Run the gates in batches") and what it found. The history file also keeps each Hank handoff entry (see "Keep Hank's conversation short"), which records where the review loop stands and adds no rule. Of that history, the design document keeps only what "Status" and "Dory validation record" say to keep. Every decision and rejected alternative stays in the design document. Leave the history file out of Referenced files, because no gate depends on it.

## Write each rule once

State each rule, limit, or number in exactly one place, and refer to it everywhere else by its decision, test, or section name. A second copy drifts from the first as soon as one of them is edited. Do not cite line numbers or count the document's own contents. Do not describe the document's own layout, as in "stated once", "above", or "N paragraphs away", and do not restate history in normative text.

## Plain-speech pass

Before ending Phase 2, reread every prose section: Problem, Technical plan, the narrative parts of Architecture and flows, Alternatives considered, Risks and mitigations, and Rollout, migration, and rollback. Rewrite whatever `reference/plain-speech-checklist.md` in this skill flags. Leave Detailed implementation's component entries, Referenced files, and the Decision log terse and structured; do not compress them into prose.

This is a standing editing habit, not a gate: do it and continue in the same turn. Do not pause for confirmation, and do not treat it as satisfied by asserting it was done. The rewritten prose is the evidence.

# Phase 3: Ask Dory

A Dory phase must behave as if it has just met the plan for the first time, with zero access to the Hank conversation. Use only the design document and files it explicitly references. Do not silently fill gaps from prior chat context.

Run every Dory phase in a fresh conversation, never as a continuation of the Hank phase or of an earlier reviewer, though the steps of one `dory-pass` share its one fresh conversation; a single ongoing conversation cannot honestly certify its own amnesia. If the available tooling cannot start a fresh conversation, say so and record the isolation gate as not certified rather than asserting it passed.

Before returning a verdict, answer one self-audit question in the output: "What did this verdict rely on that is not in the design document or its referenced files?" A non-empty answer means the gate fails; add that information to the document explicitly and rerun a fresh Dory phase.

## Dispatch Dory reviews

Isolation depends on what a reviewer has seen, so it requires a fresh conversation that starts with no history. It does not require a new worktree, clone, or machine. Dory phases change no files, so they can share one checkout. A new environment per review adds setup and handoff time without making the review any more independent.

### Choose where each reviewer runs

Use the first option the tooling supports:

1. a sub-agent that receives only the kickoff prompt;
2. a new chat session in the checkout Hank is using;
3. a new worktree or clone, only when that checkout cannot stay unchanged until the review returns, or when the reviewer must run on another machine.

Skip the sub-agent option when a sub-agent's starting context shows checkpoints, history, or session files from before its kickoff prompt, and rerun in a new chat session any review whose reviewer reports seeing them. If a new chat session shows them too, the tooling cannot start a fresh conversation, which Phase 3's opening paragraphs cover. Start any new session for a reviewer in a session mode that does not pause for plan approval, so it runs unattended. Never start a reviewer by forking or resuming the Hank conversation, or by handing it a summary of that conversation. A fork copies the history the review must be free of. Run each reviewer, and the diff check, on a model at least as capable as Hank's. Steps 6 and 7 judge the whole design, so a reviewer that runs either one runs at Hank's reasoning effort or higher; at light and fast pace, at Hank's effort unless the charter sets a higher one. A reviewer that runs only Step 5/5b tests whether the text carries its meaning, and the diff check reads only a diff and the sections it touches, so they may run at lower effort than Hank's, down to high or the tooling's nearest equivalent. If Hank runs below high, they run at Hank's effort. Read-only tool access is fine. A lighter model, or effort below these levels, is not, because it trades review quality for speed.

### Freeze the document

Before starting a batch or Hank's checks, commit the design document and every referenced file you changed, and make sure `Status` names the version at that commit. Every reviewer and check reads the commit it was given through `git show <commit>:<path>`, or an equivalent frozen copy when the project isn't in git, never the working tree. Do not edit the design document or any referenced file until every review and check in the batch has returned, except on a building branch that "Pick the pace" allows. If a reviewer or check reports a different version or commit from the one it was given, or a reviewer reports reading the history file, discard what it returned and rerun it.

### Write the kickoff prompt

Give each reviewer only:

- the mode and steps to run, for example `dory-critic`, Step 6, or `dory-pass`, Steps 5 to 7;
- the design document's path, version, and commit;
- an instruction to read that document and only the files in its `Referenced files` section, at that commit, to change nothing, and to follow this skill's instructions for that step;
- an instruction to read the document in one piece, for example with one `git show`, skipping none of it and reading the rest if the tooling cuts a read short, to read each referenced file at most once and search it rather than reread it, and to send one final report with no progress messages;
- any operating limits the user set, such as machines or commands that are off limits;
- for a scoped critic round, or the Step 6 part of a scoped `dory-pass`, the last commit a batch reviewed, and an instruction to critique only the sections changed since that commit, reading the rest of the document for context;
- what to return: the step's required output and verdict, the document version and commit it read, the files it read, the HankNDory version it followed, whether its starting context showed checkpoints, history, or session files from before this prompt, and its answer to the Phase 3 self-audit question.

If the reviewer cannot load this skill, paste Phase 3's opening paragraphs and the text of each step it runs into the prompt. That text is instructions, not design context. Never add design content: no decisions, hints, summaries, or expected verdicts.

### Run the gates in batches

Numbered step 1 below is for careful pace. At balanced, light, or fast pace, one reviewer in mode `dory-pass` runs the steps "Pick the pace" names, in order, on one frozen version, and reports a verdict for each. It takes the place of the separate reviewers in steps 2 to 4, and each step closes as it would at careful pace. A later pass runs only the steps still open, plus Step 7 at fast pace; run Step 7 alone only when it is the only step still open. At fast pace, a `READY` counts only if, on that same version, Steps 5 and 5b passed, Step 6 closed, every gate was certified isolated, every check in the batch returned, and no revision followed. That pass's important findings then go to the history file as notes for the builder, instead of into a revision. Step 7's version limit counts only versions it reviewed after Steps 5, 5b, and 6 closed.

Steps 5 and 5b run in one reviewer, because Step 5b rewrites Step 5's explanation. Step 6 reads the same frozen version and does not need Step 5's result, so the two reviewers can run at the same time.

Before a batch reviews a version that no earlier batch has reviewed, Step 7's batches included, run Hank's checks on it once, as `reference/hank-checks.md` describes: the pre-flight scan, and also the diff check if an earlier batch has reviewed a commit and the pace calls for one. Commit that version as a candidate and give the checks that commit. Fix what they find, and start the batch on the commit that includes those fixes without rerunning the checks. They are one pass, not a gate, so never loop them until they come back clean. Any other check Hank runs that reads the whole document runs alongside the batch instead, on the batch's commit and never before it, and its findings join the reviewers' findings. A check that errors out or stalls holds nothing back and counts as returned. Stop it if it is still running, start the batch or write the batch's revision without it, and record the gap in the history file. If it cannot be stopped and returns later, record what it found as non-blocking notes in the history file.

1. Start the Step 5/5b reviewer and a Step 6 critic round together.
2. Wait for every review in the batch, as "Keep Hank's conversation short" describes, and gather the findings of any whole-document check running alongside it once that check returns. Fix all of their findings except those Step 6 makes optional, in one Hank revision, and bump the version. If Hank's checks or reviewers find that two revisions in a row brought back the defect class they were written to fix, restructure the document in this revision instead of patching that text again, for example by moving history into the history file or by splitting the document.
3. Start the next batch with only the gates still open. Step 5/5b stays open until it passes. Step 6 stays open until it closes as Step 6 describes.
4. Once both gates have closed, start Step 7 on the current version. Only a `READY` version that no revision followed goes to approval. After a `READY`, revise only for blocking findings, as Step 6 defines them, from a whole-document check in its batch, and leave the rest as non-blocking notes in the history file. If you revised, run Step 7 again on the new version. If Step 7 would need to review a fourth version before approval, escalate its open findings to the user instead.

If more than one reviewer runs the same gate as a cross-check, start them together on the same commit. The gate passes only if all of them pass it. Before starting a replacement reviewer, confirm the first one failed or stalled; otherwise wait for it. If the tooling can run only one reviewer at a time, run the batch's reviews and then any whole-document check back to back, and still revise once per batch.

### Keep Hank's conversation short

Every step Hank takes rereads its whole conversation, so a long one makes each step slower and costlier. Hank's working record is the files, and the design document has to stand on its own for Dory anyway. Phases 1 and 2 stay in one conversation, because the discussion with the user is what they build on. Once a batch has returned, write each revision in a new Hank conversation, never a fork or resume of the old one, following `reference/hank-handoff.md` in this skill. During Step 8, the conversation acting as Hank writes the scoped revision itself and does not hand off; a building stream that finds a broken promise pauses that work and reports it. Before starting a reviewer or check, set a stall time from how long that step took before. Then wait for the tooling's notice that it has finished, instead of checking on it again and again. Use a timeout or a scheduled wake-up where the tooling allows, and check once when the stall time passes.

## Step 5: Comprehension test

Read the design document and every referenced file needed for comprehension. Then explain, in fresh words:

1. the problem and intended outcome;
2. how the relevant current system works;
3. the proposed solution and end-to-end flow;
4. the components, the contracts they must keep, and the areas expected to change;
5. success criteria, limits, and key risks.

Return one verdict:

- **PASS**: the explanation is complete and traceable to supplied material.
- **FAIL**: important context required prior conversation, unstated assumptions, or unreferenced files.

For `FAIL`, list each missing item and the exact section that should be updated. Do not propose implementation yet. Revise in the Hank phase and rerun with a fresh Dory phase.

## Step 5b: Clarity check

Immediately after the Step 5 explanation, rewrite it once more in the plainest language available, as if for someone outside the field, with no unexplained jargon or acronyms. Then compare the plain rewrite against the original explanation.

Return one verdict:

- **PASS**: the plain rewrite preserves every claim in the original explanation, with nothing invented and nothing dropped to keep it simple.
- **FAIL**: producing the plain rewrite required inventing meaning, silently dropped technical substance, or still depends on unexplained jargon to be understood.

For `FAIL`, list each claim the plain rewrite could not preserve and why. Treat this the same as a Step 5 `FAIL`: do not propose implementation yet, revise in the Hank phase, and rerun with a fresh Dory phase.

## Step 6: Critic review

Assume the role of an expert technical reviewer. Search for:

- faulty or unsupported assumptions;
- missing requirements and edge cases;
- ambiguous ownership or component boundaries;
- contract, schema, state, concurrency, and lifecycle gaps;
- failure, retry, idempotency, rollback, and recovery gaps;
- security, privacy, abuse, accessibility, compliance, and data-retention concerns;
- observability, supportability, capacity, performance, and cost issues;
- rollout, migration, compatibility, and test gaps;
- contradictions between the proposal and referenced files;
- omitted alternatives or decisions likely to be relitigated;
- vague or inflated prose masking a missing mechanism (see `reference/plain-speech-checklist.md`).

Classify each finding as `blocking`, `important`, or `nit`. A finding is blocking only if, left as it is, the design would lead an implementer to build the wrong thing, break a requirement or contract, or create a security, privacy, or data-loss risk. Include evidence, impact, and a concrete document fix. Do not inflate severity.

A critic round with no blocking findings closes Step 6, even if Step 5/5b failed in the same batch. Hank fixes its important findings once, in the next revision, and a diff check verifies them where the pace calls for one; they start no new critic round. Nits are optional. During design, only a round with blocking findings leads to another critic round, which may be scoped to the fix.

A design document gets the critic rounds "Pick the pace" allows in its whole life, counting scoped rounds, `dory-pass` runs that include Step 6, and rounds after a return from building. Restructuring or splitting the document does not reset the count, and each document a split produces keeps the count so far. When one more round would be needed, or two reviews disagree on whether the same finding is blocking, escalate the open or disputed blocking findings to the user, with both positions for a dispute. Run another critic round only with the user's explicit OK.

## Step 7: Implementation-readiness test

Start this step only once Steps 5, 5b, and 6 have closed (see "Run the gates in batches"), or, at light or fast pace, in the same `dory-pass` as them. Review the current version.

Evaluate whether an experienced engineer, with only the design and referenced files, can implement the feature correctly on the first pass.

Check that:

- every requirement maps to a design element and test;
- every component states its contracts and the areas expected to change;
- interfaces, schemas, invariants, and error behavior are precise;
- dependencies and the build order are clear;
- rollout, migration, rollback, and observability are actionable;
- no material question requires private context from the Hank phase;
- acceptance criteria are objectively testable;
- the document is within the "Length limit".

Return one verdict:

- **READY**: no material implementation question remains.
- **NOT READY**: list the minimum questions or edits required.

After `READY`, get approval as "Pick the pace" says, and record in the document who gave it, when, and the version and commit it covers. At light or fast pace, Step 7 also lists every "Always standard" item and every step that can't be undone that the design touches, and the charter approves only a `READY` that counts under "Run the gates in batches", or at light pace the version "Pick the pace" names, whose list holds nothing the charter does not name, and that stays inside the charter's objective, budget, and delegation. Record it as approved by the charter and its version, report it in the next digest, and start building. Anything outside the charter goes to the user as a reserved decision.

# Phase 4: Implement with guardrails

## Step 8: Implement the approved design

Proceed only when the design is marked `approved-for-implementation`, or on work that "Pick the pace" lets overlap review.

1. Read the full design and all referenced files relevant to the next implementation unit.
2. Follow the build order and keep every contract.
3. Make the smallest coherent change that satisfies the design.
4. Add or update tests alongside each change.
5. Run relevant formatters, linters, type checks, unit tests, integration tests, and build checks available in the repository.
6. Compare the implementation against every acceptance criterion.
7. Keep a concise implementation log outside the design document, mapping each change to the files it touched and the design section it serves.
8. Sort each discovery by whether it keeps the design's promises: its contracts, invariants, security and privacy rules, user-visible behavior, and scope.
   - If it keeps them, decide, add one line to the implementation log, and continue. The code review covers it.
   - If it breaks one, pause the work that depends on it and revise only that part of the design. Run Hank's checks on the revision and one critic round scoped to it, a scoped `dory-pass` at light or fast pace, and resume once a critic round on it has no blocking findings. Rerun Steps 5, 5b, and 7 only if the revision changes the Problem, the Goals, or the overall approach; at fast pace, those steps join the same pass. Approval carries over unless the revision leaves the charter. The charter may grant extra critic rounds for this step; otherwise the lifetime limit applies.
   - Ask the user only when the revision changes the scope, an approved contract, or the risk beyond what the charter delegates. Treat it as a reserved decision, and wait for the answer before building on it.

## Step 9: Perform the mean code review

Review the code severely but professionally. Compare it against the approved design, or a one-off operation's checklist, and repository conventions. Find concrete defects rather than generating insults.

Inspect:

- correctness and acceptance-criteria coverage;
- unnecessary complexity and weak abstractions;
- misleading names and hard-to-follow control flow;
- missing validation, error handling, cleanup, retries, and idempotency;
- concurrency, lifecycle, resource, and state bugs;
- security, privacy, abuse, and data-handling problems;
- performance and capacity regressions;
- compatibility and migration risks;
- brittle or inadequate tests;
- broken contracts, and changes outside the areas the design expected that no implementation-log line explains;
- comments where intent, invariant, tradeoff, or non-obvious logic is not self-evident.

Do not require comments every 10 lines mechanically. Require comments where they preserve design intent or explain non-obvious constraints; prefer clearer code over compensating comments.

For each finding include severity, file and location, evidence, impact, and recommended fix. Repeat review and repair until only trivial findings remain, then report residual risks and final verification results. After the first round, a re-review reads the fix diff and what those fixes could break. A fix that touched a shared contract, such as a public interface, schema, or cross-team contract, gets a full re-review instead. Run slow checks, such as mutation testing, alongside the review on the commit it reviews. A clean verdict counts only once those checks meet the bar the design's Testing and evaluation section sets; if it sets none for a check, put the question in the digest, with a proposed bar as the reversible default.

# Required outputs

Adapt detail to the active mode, but always provide:

## Phase status

- HankNDory version
- Mode
- Change classification (trivial, one-off, or standard) and why
- Pace and charter version
- Current gate
- Verdict or state
- Evidence inspected

## Findings or work product

Provide the design section, Dory review, implementation summary, code-review findings, or README changes requested by the active mode.

## Open items

List only unresolved, material items. Separate blockers from non-blocking notes.

## Next action

Specify exactly one next workflow action, then take it immediately in the same turn, unless it waits on explicit approval or another reserved decision. Never jump across an unpassed gate. When anything needs the user, put it in the digest with your recommendation and its plain context, as "Marlin keeps the voyage moving" describes, and never leave a question only in a file. While you wait, start everything allowed, as "Marlin keeps the voyage moving" describes. Every escalation states the time spent, the critic rounds used, and what is actually blocking. When nothing is blocking, recommend proceeding with notes, never another round.

# Failure recovery

- If repository access is unavailable, request the smallest necessary input: repository path, design document, or relevant file set. Do not fabricate context.
- If referenced files are missing, stop the affected Dory gate and list the missing paths.
- If the repository is too large, switch to `bootstrap-context` or narrow to the relevant subsystem.
- If a review produces contradictory findings, verify against source files and elevate the contradiction as a blocking question.
- If a session loses context, restart from the charter, the design document, its referenced files, and the latest handoff entry in the history file, the latest digest in the charter's history file, and any history entries after them, rather than reconstructing history from memory.
- If a fresh conversation cannot be started for a Dory phase, say so and record that gate as not certified rather than asserting isolation.
- If validation repeatedly fails, reduce scope, split the feature, or sharpen the Current system section and the contracts in Detailed implementation.

# Behaviors to avoid

- Writing production code during problem discovery or design debate.
- Treating pseudocode as permission to start implementation.
- Letting the Hank phase's unstated memory leak into a Dory verdict.
- Asking a Dory phase to review only the design document while ignoring its required referenced files.
- Accepting vague statements such as “handle errors,” “add tests,” or “update the service.”
- Inventing file names, current behavior, metrics, interfaces, or approval.
- One-shotting a large design document without iterative review.
- Reopening rejected alternatives without new evidence.
- Using review harshness as a substitute for precise, respectful, actionable findings.
- Declaring readiness because critiques are fewer rather than because all material gates pass.
- Building on a broken promise before Step 8 lets that work resume.
- Certifying a Dory phase's isolation without actually running it in a fresh conversation.
- Iterating critic-review rounds indefinitely instead of escalating a persistent disagreement to the user.
- Putting Hank-phase decisions, hints, or summaries into a Dory kickoff prompt.
- Running a Dory reviewer or check on a lighter model, or at lower reasoning effort than "Choose where each reviewer runs" allows, to save time.
- Carrying one Hank conversation through the whole review loop when the tooling can start a new one, or checking on a running reviewer again and again.
- Giving each Dory phase its own worktree, or at careful pace running Step 5/5b and Step 6 one after the other, when the tooling allows a lighter or concurrent run.
- Recommending another review round when nothing is blocking, using the design method for a one-off operation, or restating code in the design.
- Leaving work waiting on the user for a decision the charter delegates, or past a reversible question's default wait; holding back allowed work for a gate, digest, or answer it does not depend on; or running independent work one stream at a time when the tooling, the charter, and the budget allow more.
- Asking questions one at a time, or in a prompt that stops work, when a digest would do; asking without plain context; or using internal labels, such as document, review, or step numbers, with the user.
- Running work under "Always standard" faster than careful pace without the charter naming it, or heavy work on a shared machine without its Crush's grant.
