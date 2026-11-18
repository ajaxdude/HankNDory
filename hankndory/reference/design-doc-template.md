# <Feature name>

<!-- Replace <Feature name> and every bracketed or commented placeholder in
     this template. Keep every heading even when a section is briefly "Not
     applicable" with a stated reason. Do not delete a heading to avoid
     writing it. Keep the document within the "Length limit" in SKILL.md.
     Create the sibling history file at the same time, for example
     <feature-name>.history.md next to this document. "Keep history out of
     the rules" in SKILL.md says what goes in it. -->

## Status

<!-- Current workflow state from "Maintain workflow state" in SKILL.md, and the
     change classification from "Size the change before choosing a gate set,"
     with the reason for it, and the pace and the charter's path and version
     from "Pick the pace" and "Marlin keeps the voyage moving" in SKILL.md.
     Add `risk: one-way` or `risk: two-way` for the legs; fast and yolo run
     Step 7 unless every leg is a two-way door, and an absent line counts as
     one-way.
     Target date for approval, review budget, time spent so far, and
     critic rounds used, as "Status" in SKILL.md describes.
     Add one line per substantive revision since the document was last
     reviewed, formatted `vN — YYYY-MM-DD — <what changed>`, and move older
     lines to the history file. Bump the version
     whenever a Dory phase or human reviewer needs to know what is new; do not
     bump it for typo fixes. -->

## Product contract

<!-- Required for user-facing work; write "Not applicable" with a reason
     otherwise. Follow reference/product-contract.md:
     - User and moment
     - First success
     - Quality bar
     - Reference
     - Reject if
     - Not the product
     The brief is input, not accepted output. Get the user's agreement before
     detailing internals. -->

## Problem

<!-- 3-5 plain-language sentences: affected user, present pain, desired
     change, and why it matters. -->

## Goals and non-goals

<!-- Must-haves versus explicit non-goals. Keep future extensions separate
     from both. -->

## Current system

<!-- Purpose and user-visible behavior; relevant components and boundaries;
     data flow and control flow; public interfaces and integration points;
     constraints, invariants, and failure behavior; tests and operational
     concerns. Cite a repository path for every material claim. -->

## Glossary

<!-- One meaning per word. List the names, verbs, and states the design
     and its requirements use: the system name that every "shall" sentence
     names, the domain objects, and the state names the requirements test.
     Add a word here before using it; when two words mean one thing, keep
     one. Words the code already defines and the design keeps unchanged
     need no entry. State "Not applicable" with a reason when the design
     adds no domain vocabulary. -->

## Requirements and acceptance criteria

<!-- Write every requirement in the requirement format. Each requirement
     maps to a design element in "Technical plan" or "Detailed
     implementation", and each Verify ID names an acceptance test that Ray
     writes and names with it. tools/design-lint.py in this skill checks
     this section, and Gill's pre-flight scan runs it.

         Requirement R<n> (<pattern>): <one obligation sentence>.
         Because <the reason a reviewer needs>.

         Verify V<n>.<m> (<name>):
           Given <start state>.
           When <trigger>.
           Expect <one observable result>.
           Expect no <result that must not occur>.

     <pattern> is the EARS shape the sentence uses:
       plain:    The <system> shall <response>.
       event:    When <trigger>, the <system> shall <response>.
       state:    While <state>, the <system> shall <response>.
       unwanted: If <condition>, then the <system> shall <response>.
       optional: Where <feature>, the <system> shall <response>.

     One requirement, one obligation: exactly one shall, in one sentence;
     two responses joined by "and" are two requirements. Name the acting
     system, never "it". The response must be observable: reject, lock,
     write, not "be secure" or "be fast". Each Verify block has one When,
     even for a plain or state requirement; the trigger may be the check
     running or the state being entered. Keep every sentence and clause to
     25 words. Write each numeric source as (source: ...), naming the
     measurement, the calculation file, the model, or a Bailey card.
     Order Verify clauses Given, When, Expect; the accepted clause words
     are Given, While, When, and Expect, and Expect no. Each Expect holds
     one check and names the observation that proves the shall sentence,
     never a restated copy of it. Prefer the Glossary's names, and use
     numbers with a bound or range and a source, or an (exact) mark, per
     the "Numbers from evidence" core rule in `SKILL.md`, instead of vague
     words such as "fast" or "as needed".

     IDs are stable. Once a review, test, or digest cites an ID, never
     renumber it: retire an obsolete requirement with a struck line that
     keeps its ID, and never reuse a retired ID.

     Ray names each acceptance test with the Verify ID it implements, for
     example "V1.2 lockout after three failures", so coverage of the
     promises is checkable without reading the design. Each test asserts
     the Expect, not the shall sentence. -->

## Technical plan

<!-- Jargon-light prose covering the major components and how they fit
     together. Include a block diagram if flows would otherwise be
     ambiguous. -->

## Architecture and flows

<!-- End-to-end data and control flow; interfaces and contracts; state,
     persistence, consistency, and concurrency; errors, retries, idempotency,
     rollback, and recovery. -->

## Alternatives considered

<!-- For each serious alternative: summary; benefits; costs and risks; reason
     rejected or deferred; evidence or constraint behind the decision. Never
     delete a rejected alternative once recorded, even after a preferred
     design is chosen. -->

## Detailed implementation

<!-- Before building, the Map's part: the contracts that cross legs or that
     other systems rely on; the legs in order, one line each, giving what it
     delivers, what its demo will show, whether it is a one-way or a two-way
     door, and what it depends on; and the first leg in full unless it is a
     two-way door. Add a "Leg: <name>" subsection for each later leg when it
     starts, as reference/map-and-legs.md describes.
     Each leg states the promises the code must keep, not the code. For each component: its
     responsibility; the contracts it must keep (interfaces, schemas,
     invariants, error behavior); the areas expected to change, naming a file
     only where a contract lives in it. Then the build order, with
     dependencies and checkpoints. File-by-file changes go in the
     implementation log and the code review, not here. Mark any unverified path
     "(proposed, unverified)" until repository inspection confirms it. -->

## Demo plan

<!-- For user-facing work, the first leg is a playable slice, and every
     user-facing leg ends with a demo artifact: URL, screenshot or recording,
     run command, three-step script, checks, and the user's verdict. Name the
     first slice, who presents it, and the demo artifact it will produce.
     When the boss is absent or the pace is yolo, name how the demo council
     will choose the next slice. State "Not applicable" with a reason
     otherwise. -->

## Testing and evaluation

<!-- How each Verify ID will be exercised: unit, integration, manual, or
     evaluation-harness coverage, with Ray's named test for each Expect or a
     stated reason it can't be automated. State what proves the feature
     works, not just that it runs. Cite Bailey's cards for spikes,
     experiments, models, and datasets instead of restating them. -->

## Security, privacy, reliability, and operations

<!-- Threats, data handling, access control, observability, capacity, and
     on-call/runbook impact. State "Not applicable" explicitly with a reason
     if genuinely out of scope. -->

## Rollout, migration, and rollback

<!-- Deployment sequencing, feature flags, data migration steps, and exactly
     how to revert if something goes wrong. -->

## Risks and mitigations

<!-- Known risks ranked by severity, each with a concrete mitigation or an
     explicit accepted-risk rationale. -->

## Open questions

<!-- Only unresolved, material items. Remove a question once it is answered
     instead of leaving it stale. -->

## Decision log

<!-- One entry per settled decision that could plausibly be relitigated:
     decision, status, reason, date. Never erase a superseded entry; mark it
     superseded and link the replacement. -->

## Referenced files

<!-- Every file a fresh Dory phase needs to understand and implement the
     plan, with a one-line reason for each and, for a large file, the part
     that matters, named by section or function, not line number. Remove
     stale or incidental references. -->

## Dory validation record

<!-- One line per independent review: review type (comprehension | critic |
     readiness), the version it reviewed, and its verdict. A comprehension
     line gives both the content verdict (Step 5) and the clarity verdict
     (Step 5b). Record the full entry in the history file:
     - review type
     - document version and commit reviewed
     - date, batch, or run identifier if available
     - inputs provided
     - verdict(s)
     - blocking findings
     - document changes made
     - remaining non-blocking notes -->

## Human approval

<!-- Who approved, when, and the version and commit approved. For approval
     by the charter at light or fast pace, name the charter and its version. -->
