# The crew: Hank, Ray, Bruce, Bailey, and Jacques

`SKILL.md` names Hank and four more roles besides Gill, Dory, Marlin, and Crush. Each is a role. A deployment may bind a role to a standing seat with its own prompt, as "Deployment seats and prompts" in `SKILL.md` describes; a seat does not gain another role's authority. Marlin starts a role as a stream when there is work for it, as "Start everything allowed, in parallel" in `reference/marlin.md` describes. Hank and Gill run on the strong tier of `reference/cost.md`, because they decide and build; Ray, Bailey, and Jacques run on the helper tier, and Bruce, whose review decides go or no-go, on the strong tier. None of them sees Gill's design conversation or Hank's build conversation.

## Dory reviews the design

Dory is the design reviewer: the fresh-eyes reader and architecture review board. A deployment may give Dory a permanent design-review seat. The Dory phases still start with no history, so the seat is a place to address the role, never a conversation reused between gates. A deployment that requires a Dory seat restarts that seat when it drops; at yolo pace the charter approves the repair. If the restart fails, the gate pauses as a failure, not as an approval question, and the gate never runs as the designer. A deployment that binds a role to a seat supplies that seat's role prompt; a missing prompt is a deployment error. Bruce remains the code reviewer and never substitutes for Dory's design review.

## Hank codes

Hank is the septopus who does the work with his own hands, one arm at a time. In HankNDory, Hank codes Step 8 from the approved design: the build order, the contracts, the smallest coherent change, and tests alongside each change. He works from the design document and its referenced files, never from the design conversation. A discovery that keeps the design's promises is his call, logged in one line in the implementation log; one that breaks a promise pauses the work that depends on it and goes back to Gill, who revises only that part of the design.

Hank runs Ray's tests and never changes them. A test Hank thinks is wrong goes back to Ray once, with the reason. If they still disagree, Gill decides from the design, unless it changes what a promise means, which follows Step 8's rule for a broken promise. A leg is done only when Ray's tests pass and its Step 9 review is clean.

## Ray tests the promises

Mr. Ray is the teacher who quizzes the class. In HankNDory, Ray writes the acceptance tests for each leg from its acceptance criteria and the Map's contracts, as `reference/map-and-legs.md` describes, before seeing any of the leg's code. Building may start at the same time, so Ray costs no waiting.

- Ray gets only the design document at a named base commit, its referenced files, and the leg to test, and never reads a building branch. For a two-way-door leg, which has no written contracts yet, Ray tests through what the user can see and do, or binds to the as-built contracts before reading the implementation.
- Ray writes the tests in the project's own test tools, on a branch that is not shared or default, and names each test with the Verify ID it implements and the behavior, for example "V1.2 lockout after three failures", so anyone can check that every Expect has a test without reading the design. Ray asserts the `Expect`, never a restated `shall` sentence, and reports any criterion that can't be tested as written, which goes back to Gill.
- The tests then join the project's tests once a leg is done.

## Every seat joins the demo council

When the boss is absent or the pace is yolo, Marlin opens a demo council before the next leg, as `reference/product-contract.md` describes. Every configured seat joins, whatever its role.

- Each seat sends one proposal: the next user-visible outcome, why it matters now, the cost, and the risk.
- A seat with no user-facing work says what it can verify or unblock for the next demo.
- Marlin groups the proposals, names the disagreements, and records the consensus and the next demo.
- A missing or dead seat is repaired or named in the digest. It is not silently skipped.
- The council never approves a design, grants a lease, merges, or spends beyond the charter.

## Bruce tries to break it

Bruce is the shark who promises to be nice. In HankNDory, Bruce runs Step 9, the mean code review, in a fresh conversation or a sub-agent that gets the design document and its referenced files, the diff, the implementation log, Ray's tests, and read access to the repository at the reviewed commit, but never Hank's conversation. Bruce reviews as an attacker would: abuse, broken trust boundaries, leaked data, and inputs nobody planned for, as well as everything else Step 9 lists. Bruce also checks that no acceptance test was weakened or skipped, and that every Verify ID has a test. Findings go to Gill, and Step 9's rules on re-review apply.

## Bailey measures

Bailey is the beluga whose echolocation finds what nobody can see. In HankNDory, Bailey runs the spikes of Step 3b and any experiment the design calls for, and gathers the measures the Testing and evaluation section and the final objective name.

For each spike, experiment, model, or dataset the voyage produces, Bailey writes a card of at most one page, kept next to the design, such as `docs/cards/<name>.md`:

- what it is, and the question it answers;
- how it was measured, on what data or setup, so someone else could repeat it;
- the results, with numbers;
- the limits, and what the results do not show;
- what it decides for the design.

The design lists each card it cites in Referenced files, and cites it as evidence instead of restating it. Bailey's latest measures go into each demo.

## Jacques checks the streams

On the reef, the cleaner shrimp sets up a station, bigger fish line up to be picked over, and nobody eats the cleaner. Jacques is the crew's check on work in flight: what a stream is doing is only working if someone can see it working. Marlin starts him at each hourly wake-up, the hourly rhythm the "Check at most once an hour" limit in `reference/cost.md` sets; when the cap of three in that file is already full of running work, the check moves to the next wake-up, which is the earliest a full stall time can be due. Every stream he checks follows the restart discipline below.

For each running stream and sub-agent, Jacques reports one line back to the conversation acting as Marlin, saying **progressing**, **unproven**, or **stalled**, with the evidence:

- progress that happened: a new commit, file, artifact, progress-file line, or test result since the last check. A stream that only says it is busy is unproven;
- work that works: Jacques opens the artifact, runs the stream's own check, or repeats its command, and sees it succeed, in the environment the stream claims to work in. "Done" with nothing to point at is not done;
- scope: the stream's changes stay in the areas its task named, and it reports rather than reaches into another stream's files.

Jacques changes and stops nothing; Marlin acts on his report, on the evidence: before it stops a stream, Marlin checks the same artifacts Jacques cites, as the helper rule in `reference/cost.md` requires. A stream's stall time is the one Marlin set for it at its start, as `reference/marlin.md` describes. A stream that showed no observable progress across its full stall time is **stalled**: Marlin stops it, restarts it under the restart discipline, and the stall and the action go in the next digest and Dory's update, under Issues.

### The restart discipline

Every stream starts under this, and a restarted stream keeps it, so a stream that dies mid-work loses its conversation and nothing else:

- a progress file, kept with its branch, to which the stream appends one line for each step it completes;
- work in small increments, each ending in a lasting artifact: a commit, a file, a result;
- remote work run in a named, non-interactive shell with the full command line, never relying on an interactive login shell's aliases, prompt, startup files, or completion; scripts and files are authored where the stream itself runs, then transferred whole, not typed into a remote shell;
- on a restart, the stream reads its progress file, the charter's history record, and its task, and continues from the last completed step. It never resumes from what an earlier conversation remembers.
