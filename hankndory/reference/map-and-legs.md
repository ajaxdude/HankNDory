# The Map and its legs, and two-way doors

`SKILL.md` points here from "Size the change before choosing a gate set" and "Detailed implementation". Code is cheap for an agent to write, and keeping a project coherent is expensive, because agents forget everything between conversations. So design first only what is hard to undo, and design each stretch of the work when it starts, using what the last stretch taught.

## Two-way and one-way doors

A **two-way door** is a change that reverting its commits fully undoes. It changes no user, production, or shared data, and no shared environment. It publishes, deploys, and sends nothing to users or outside the project. It changes no contract that others already rely on, adds no infrastructure or paid resource, changes no secret, credential, or pipeline that can deploy, and touches nothing under "Always standard". Examples are user-interface work, internal code, and experiments behind a switch that is off by default. Everything else is a **one-way door**. When unsure, treat it as a one-way door.

Build a two-way door first, and write its design as built. Design a one-way door first, and build it only once its design is approved. Hank marks each leg's door in the Map; Step 6 and Bruce's review each check that a leg marked two-way really is one. If a two-way-door leg turns out to need a one-way door, stop that part, keep its branch unmerged, and design and approve that part as a one-way-door leg.

## The Map

The Map is the design document as written before building starts: every section of `reference/design-doc-template.md`, with Detailed implementation holding:

- the contracts that cross legs or that other systems rely on;
- the legs, in order, one line each: what the leg delivers, what its demo will show, whether it is a one-way or a two-way door, and what it depends on;
- the first leg in full, unless it is a two-way door.

The Map is not the charter. The charter says how the voyage is run: who decides what, the budget, and the pace. The Map says what is being built and the promises that hold across it. A leg usually matches one of the charter's milestones. With legs, `Status` records each leg's door and state, as `Leg <name>: <state>`.

## Legs

A leg is one stretch of the build that ends in a demo. Before a one-way-door leg starts, Hank writes its section under Detailed implementation, following that section's rules in `SKILL.md`, plus the acceptance criteria Ray tests, as `reference/crew.md` describes. Before a two-way-door leg starts, Hank writes only its acceptance criteria. Hank writes from the Map and from what earlier legs taught, and writes nothing that breaks a Map promise without following Step 8's rule for a broken promise.

- **One-way-door leg:** run Hank's checks on the new section, then one review of Steps 6 and 7 scoped to that leg, reading the rest of the document for context, in the pace's reviewer layout: a scoped `dory-pass`, or separate reviewers at careful pace. Its critic rounds follow Step 6's limit for a leg. Build once the review has no blocking finding, Step 7 says `READY`, and the leg is approved as "Pick the pace" says: by the charter at light or fast pace, otherwise explicitly by the user. Record the approval under Human approval with the leg's name. A leg that touches anything under "Always standard" needs the charter to name that item, or the user's explicit approval of that leg.
- **Two-way-door leg:** start building at once, at every pace, on a branch that is not shared or default, from the Map's line for the leg and its acceptance criteria. When the leg is built, Hank writes its section as built, and Bruce's code review checks the code against it and the Map. The Map's approval covers it while it stays inside the Map's contracts and the charter.

Nothing merges into a shared or default branch, or deploys, until the Map is approved, the leg's acceptance tests pass, and its Step 9 review is clean. Merging stays reserved unless the charter delegates it.

When a leg is done, shrink its section to what later legs rely on, and move the rest to the implementation log, except decisions, which stay in the Decision log, so the document stays within the "Length limit". A design written before legs existed counts as one one-way-door leg, unless `Status` records otherwise.

## A change that is all two-way doors

When every leg is a two-way door, the Map is short: Problem, Goals and non-goals, Requirements and acceptance criteria, and the contracts others rely on, with every other section "Not applicable yet". No Dory pass runs before building. Building and Ray's acceptance tests start at once. Once built, Hank completes the document as built, and one `dory-pass` under light-pace rules reviews it while Bruce reviews the code, at the same time. Approval then comes after building and approves merging, given by the user, or by the charter at light or fast pace.
