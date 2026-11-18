# The product contract and the demo council

`SKILL.md` points here from "User-facing work: show the product". Use this page for any artifact a person will see, operate, read, or listen to.

## The product contract

Write it before requirements, in the design document's Product contract section, and agree it with the user. Keep it short enough to read back in one minute.

Template:

```markdown
## Product contract

- User and moment: <who opens this, where, and what they are trying to do>
- First success: <what the user can see or do in the first 30 seconds>
- Quality bar: <legibility, density, responsiveness, latency, platform fit, tone, accessibility>
- Reference: <screenshot, URL, recording, or existing product, with the part that matters>
- Reject if: <three to seven observable failures>
- Not the product: <what the user may not mistake this for>
```

Good reject conditions are observable, not adjectives:

- "the panel label is clipped at the default GNOME font size";
- "the menu takes more than 100 ms to open on the test host";
- "a stopped engine still shows a numeric speed";
- "the game board is a white rectangle with indistinguishable black pieces";
- "the preferences window looks like a different application from the shell".

The reference is required unless the user explicitly waives it. A reference is not a licence to copy code, names, or logos. Say which part is the reference: layout, density, color, interaction, or tone.

Gill reads the contract back to the user in plain words before designing internals. If the user says "you decide", Gill still proposes one reference and one reject list, and the user accepts or changes it. Taste stays reserved unless the charter names it.

## The playable slice

For user-facing work, the first leg is a playable slice:

- one real user path, end to end;
- the final visual frame, not a grey placeholder;
- real platform controls and constraints;
- a URL, a command, or a file the user can try;
- a screenshot or short recording;
- the user's verdict: accept, revise, or reject.

A slice is a two-way door unless it touches an "Always standard" item. Build it first at every pace, on a branch that is not shared or default, from the product contract. Write its design as built once it exists. Do not run Dory over reversible visual choices before the user has seen the slice.

The slice is allowed to use mock data. It is not allowed to look like an unfinished internal tool when the product is user-facing.

## The demo artifact

Every user-facing leg ends with an artifact. A demo without one is not a demo.

```markdown
### Demo: <leg name>

- Presenter: <one character, chosen by the product>
- What works now: <one or two sentences>
- Try it: <URL, command, or file path>
- In three steps: <open, do, observe>
- Checks: <commands and results>
- Choices: <one line each, with the reason>
- Next: <the next user-visible outcome>
- Boss verdict: <accept | revise | reject, with the date>
```

One character presents it, in half a page, in the boss's chat pane. Choose the presenter by the product: Hank for code, Gill for architecture, Dory for design, Ray for tests, Bailey for measurement, Bruce for security, Crush for operations, Jacques for streams, Marlin for coordination. The presenter explains the choices and tradeoffs, not just the status.

Marlin sends it at the leg's end. The boss does not have to ask. A screenshot can be a file path, an image attachment, or a URL. A recording is a short capture of the actual product, not a mockup.

If the leg cannot be run on the boss's machine, the artifact must include a screenshot or recording and the exact command used to produce it.

## The demo council

The council runs when the boss is absent or the pace is yolo, before the next leg is chosen. It is not a safety gate; it chooses what to show next.

1. Marlin opens one council with the last demo, the objective, the board, the budget, and the question: "What should the next demo show?"
2. Every configured seat, whatever its role, sends one proposal: the user-visible outcome, why it matters now, the cost, and the risk. A seat that cannot answer names what it needs.
3. A missing or dead seat is repaired or named in the digest. It is not silently skipped.
4. Marlin groups the proposals, names the disagreements, and records the consensus and the next demo. If the seats do not agree, Marlin chooses the smallest next demo that tests the disagreement, and says so.
5. The council result is one short message to the boss and one line in the next update. The boss may replace the choice at any time.

The council does not approve a design, grant a lease, merge, or spend beyond the charter. It only decides the next user-visible slice.

## Experience checks

Rule checks prove the promises. Experience checks prove the user can see, read, reach, and use the result.

- A test may pin an implementation detail only when that detail is the user-visible requirement.
- A test that counts calls, layers, or elements must not forbid an obvious improvement such as a background, a grid, a focus ring, or a loading state.
- A screenshot check proves presence and layout, not taste. Taste is the boss's verdict.
- A mock or unit test is not evidence that the product looks or feels right. A running artifact is.

## Ceremony budget

For reversible user-facing work, design and review must not outrun building without an artifact. If the artifact is missing when the review budget is spent, stop the loop and show the slice. A longer document is not progress.
