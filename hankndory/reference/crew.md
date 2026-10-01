# The crew: Ray, Bruce, and Bailey

`SKILL.md` names three more roles besides Hank, Dory, Marlin, and Crush. Each is a role, not a standing conversation. Marlin starts one as a stream when there is work for it, as "Start everything allowed, in parallel" in `reference/marlin.md` describes, on a model at least as capable as Hank's. None of them sees the builder's conversation.

## Ray tests the promises

Mr. Ray is the teacher who quizzes the class. In HankNDory, Ray writes the acceptance tests for each leg from its acceptance criteria and the Map's contracts, as `reference/map-and-legs.md` describes, before seeing any of the leg's code. Building may start at the same time, so Ray costs no waiting.

- Ray gets only the design document at a named base commit, its referenced files, and the leg to test, never reads a building branch, and runs at Hank's reasoning effort or one level lower. For a two-way-door leg, which has no written contracts yet, Ray tests through what the user can see and do, or binds to the as-built contracts before reading the implementation.
- Ray writes the tests in the project's own test tools, on a branch that is not shared or default, and reports any criterion that can't be tested as written, which goes back to Hank.
- The builder runs Ray's tests and never changes them. A test the builder thinks is wrong goes back to Ray once, with the reason. If they still disagree, Hank decides from the design, unless it changes what a promise means, which follows Step 8's rule for a broken promise.
- A leg is done only when Ray's tests pass and its Step 9 review is clean. The tests then join the project's tests.

## Bruce tries to break it

Bruce is the shark who promises to be nice. In HankNDory, Bruce runs Step 9, the mean code review, in a fresh conversation or a sub-agent that gets the design document and its referenced files, the diff, the implementation log, Ray's tests, and read access to the repository at the reviewed commit, but never the builder's conversation. Bruce reviews as an attacker would: abuse, broken trust boundaries, leaked data, and inputs nobody planned for, as well as everything else Step 9 lists. Bruce also checks that no acceptance test was weakened or skipped. Findings go to Hank, and Step 9's rules on re-review apply.

## Bailey measures

Bailey is the beluga whose echolocation finds what nobody can see. In HankNDory, Bailey runs the spikes of Step 3b and any experiment the design calls for, and gathers the measures the Testing and evaluation section and the final objective name.

For each spike, experiment, model, or dataset the voyage produces, Bailey writes a card of at most one page, kept next to the design, such as `docs/cards/<name>.md`:

- what it is, and the question it answers;
- how it was measured, on what data or setup, so someone else could repeat it;
- the results, with numbers;
- the limits, and what the results do not show;
- what it decides for the design.

The design lists each card it cites in Referenced files, and cites it as evidence instead of restating it. Bailey's latest measures go into each demo.
