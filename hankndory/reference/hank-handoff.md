# Hank handoff

Hank follows these steps as "Keep Hank's conversation short" in `SKILL.md` describes. The handoff moves Hank's working record into the files, so a new Hank conversation can start from the files alone.

Only one conversation acts as Hank at a time: the one named in the newest handoff entry marked `Taken over`, or the Phase 1 and 2 conversation before any handoff. Only that conversation revises the design document, starts a batch, plays Marlin, or sends the user a digest. A conversation that has handed off never acts as Hank again. If a message reaches it later, it points the sender to the current Hank.

## When the batch returns

The Hank conversation that started the batch waits for it, then:

1. Records the full entries for the batch's reviews and checks in the history file, as "Keep history out of the rules" in `SKILL.md` describes.
2. If a revision is needed, adds a handoff entry to the history file, titled `Handoff after <batch>`, with:
   - the design document's path, and the version and commit the batch reviewed;
   - the gates still open, and every finding the next revision must fix, by review and finding number;
   - the commit the next diff check starts from, where the pace calls for one, the defect classes earlier reviews found, and whether the next revision must restructure the document, as step 2 of "Run the gates in batches" in `SKILL.md` requires;
   - any reviewer or check still running, and where its result will arrive;
   - the charter's path and version, and the pace;
   - at fast pace, the building under way: its components, its branch, and its implementation log;
   - the critic rounds used, the time spent, the target date, and the review budget;
   - every user decision, preference, and rejected option since the last handoff, or since Phase 1 for the first handoff, that the design document does not hold yet;
   - the open digest: each question waiting on the user, with its recommendation, and for a reversible one, its default and when that takes effect;
   - the next action.
3. Commits the history file, or saves a frozen copy when the project isn't in git.
4. Starts a new Hank conversation with the prompt below, then tells the user where Hank now continues, and that the open digest should be answered there.
5. Checks once for the new conversation's `Taken over` mark: after the tooling reports that the new conversation has started, or after a wait set before starting it. If the mark is there, it stops. If not, it stops the new conversation and carries on as Hank, recording the failed handoff in the history file. If it cannot stop the new conversation, it tells the user and waits for them.

If the batch leads to no revision, such as a `READY` that goes to human approval, the same conversation carries on and no handoff is needed.

## The new conversation's prompt

Start it as a new top-level conversation that the user can see and answer in, not a sub-agent, and not a fork or resume of the old conversation, which would bring its length along. Start it in a session mode that does not pause for plan approval, on the model and reasoning effort Hank has used so far. Give it only:

- the instruction to run HankNDory as Hank, in the review loop, following `SKILL.md`;
- the model and reasoning effort it runs on, which every later handoff keeps;
- the design document's path, the charter's path, and the commit holding the handoff entry;
- the user's operating limits and standing instructions, quoted as the user gave them, as a Dory kickoff prompt carries them;
- the instruction to read `SKILL.md`, `reference/marlin.md`, the charter, the design document, the handoff entry and the batch's entries in the history file, and any implementation log the entry names, each once and in one piece, and only the referenced files the fixes need.

If the tooling cannot start such a conversation without the user, shrink the current conversation down to the handoff entry instead, if the tooling can, and record that in the history file. If it cannot do either, carry on in the current conversation and record that the handoff was skipped.

## What the new conversation does

1. Marks the handoff entry `Taken over`, with the commit it read, and commits that.
2. Sends the open digest again, as its first message to the user, keeping each default's original time.
3. Writes the revision, applying `reference/plain-speech-checklist.md` to each prose section it changes, runs Hank's checks, starts the next batch, and waits for it. When that batch returns, it hands off in turn.

Anything the handoff entry leaves unclear, it puts in the next digest rather than guesses. If something it needed was missing from the files, it adds that to the design document or the next handoff entry, so the gap does not repeat.
