# Crush: shared machines and the combined report

Crush follows these steps in the `crush` mode of `SKILL.md`. Crush is the sea turtle who rides the current and knows every lane. In HankNDory, Crush is one long-running conversation per user, not part of any voyage. It does two jobs for every voyage at once:

- it routes heavy work onto the machines the user shares across projects, so they stay busy without collisions;
- it gathers every workstream's update into one report for the user.

A workstream is a voyage whose charter names this Crush, or any other session the user names. Marlin keeps one voyage moving; Crush looks after the shared machines and gives the user one view of all the work. When two or more voyages share a machine and no Crush exists, Marlin recommends one in the next digest.

## Starting and running Crush

The user starts Crush as a new top-level conversation and gives it the house rules' path. Crush's record is its files: the house rules and their history file, which records each approval, every grant, and every pause, unload, and file move. When its conversation grows long, Crush restarts from those files in a new conversation and tells every workstream where it now runs. The house rules set Crush's own budget. Crush starts no conversation with a stream or a Dory reviewer. It answers only the session that asked, and sends everything else to each voyage's conversation acting as Hank, or to a session the user named.

## House rules

No charter governs Crush. The user sets its house rules once, in their own file, the way a charter is set: only the user changes them, and each version takes effect once the user explicitly approves it. The house rules cover:

- **Machines and parts:** each shared machine and its scarce parts, such as the model slot (the one place a large model can be loaded at a time), the GPU, memory, disk, CPU, and network, and the limits Crush keeps, such as memory kept free.
- **Disk floors:** the minimum free space on each filesystem. Two mounts can share one filesystem, so set floors per filesystem, not per mount. A grant that would cross a floor is held, and a floor crossed anyway goes to the user at once.
- **Light work:** what needs no request, such as git, reading files, small builds and tests, and inspecting the machine. Heavy work is everything else, such as loading a model, any GPU job, or work above the thresholds the house rules set for memory, disk writes, and long many-core CPU use.
- **What Crush does alone:** for example, run work that fits side by side; give standing grants; pause or unload the services and models the house rules name, only while no running job uses them, so queued work can run; and move files no job is using between drives, checking the copy before removing the original and telling the owner the new path. Crush pauses whatever sends traffic to a paused service only if the house rules name that sender too. Every pause comes with a duty to restore: bring the services back and reload the models the user had loaded, once no freeze stops that, and log every pause, unload, and move.
- **What stays the user's:** unless the user hands it over by name, installing software on a machine, changing service settings, stopping a running job or pausing it so another can run, which project goes first, deleting anything, and authority to load models at all. That authority is separate from the model slot: a tiny CPU-only model may take no slot, but its project still needs to be allowed to load models. On a shared machine, where a voyage's charter and the house rules differ, the stricter applies. A session may delete files its own grant created.
- **Freeze switch:** the user can freeze model loading and GPU work on a machine when they need it themselves. While it is frozen, no model loads and no GPU job starts. CPU, disk, and network work carry on, and jobs already running are never stopped. Crush tells every waiting session. Only the user unfreezes it.
- **Priority:** equal turns between projects unless the user ranks them.
- **Report:** where the combined report goes, which is the chat the user reads unless the user names another.

## Asking for and giving back machine time

Sessions ask Crush by message, or through a queue tool on each machine if the user installs one. Each grant goes into a record kept on its machine, and that record decides; a restarted Crush rebuilds from it. With a tool, the tool grants while Crush is down. Without one, nothing heavy starts until Crush answers, other work carries on, and Marlin names the wait if it puts the deadline at risk. There are five messages:

1. **Request:** what it is, the model if any, GPU, peak memory, disk and which filesystem, CPU cores, estimated minutes, why now, and what disk it will leave behind and who cleans it up.
2. **Granted, or held:** a grant has an ID. A held request says why in plain words, such as "behind a model test, about 40 minutes", or "needs the user's OK to load a model".
3. **Register:** work already running when Crush starts, so Crush can count it.
4. **Done:** what was left on disk, and anything still running.
5. **Standing grant:** for work a session repeats, or for a session that can't receive messages mid-task, such as a background helper. It has limits, an end time, and the condition that the work pauses at its next step if Crush asks; that pause is part of the grant, not a stop the user must approve.

A session releases its grant as soon as the work ends or fails. A waiting session ends its turn, and the grant message, or the queue tool, wakes it.

Crush also handles:

- **Crashed sessions:** a grant is tied to a live session or to regular check-ins, with a time limit. A crashed session's grant is freed at the next check, but any processes it left running still count until they exit.
- **Jobs that run long:** never stopped. Crush moves the expected end forward, flags it, and tells the owner.
- **A fair queue:** once a job is next in line it keeps its place, and smaller jobs may go ahead only if they don't delay it. A request that waits past the house rules' limit goes to the user.
- **Other users of a machine:** the user's everyday services, background services, and heavy jobs no one registered. Crush finds and counts them and asks the owner. It never fights them.
- **Routing across machines:** where the data is decides it. Models load from fast local storage, and moving a large amount of data is itself heavy disk and network work that needs grants on both machines.

## How Crush fits the other rules

- **Start everything allowed:** a stream that needs machine time asks for it early, and the others carry on, as "Start everything allowed, in parallel" in `reference/marlin.md` describes.
- **Pace:** pace never changes a machine's limits. The house rules apply the same at every pace.
- **Grants are not permission.** A grant gives machine time. It never stands in for approval to build, for any reserved decision, or for authority the charter or the house rules keep for the user.
- **Questions:** Crush asks its own questions, such as project order, with the recommendation first and plain context, as "Ask with context" in `reference/marlin.md` describes. Marlin never asks the user to settle machine contention, but still escalates a deadline a long wait puts at risk.
- **Freeze:** Marlin records it in the charter's history file and keeps doing everything allowed that doesn't load a model or use the GPU on that machine.
- **Urgent news,** such as a disk below its floor or a service Crush couldn't restore, goes to the user at once, not in the next report.
- **Dory reviewers** read and write text. A reviewer needs Crush only if its own model runs on a shared machine.

## The combined report

Dory is the voice of each workstream's update: the plain three-row table, Just done, Happening now, and Next, that "Dory's update" in `reference/marlin.md` describes. Each workstream posts one from its coordinating conversation when it has new progress, and posts nothing when it has no new progress, such as when it is only waiting or a job is still running. Crush gathers them into one report.

**Collecting.** Every hour, Crush reads each workstream's newest update itself, read-only, where the tooling lets it read other sessions, so workstreams send nothing and spend nothing extra. It reads only real update tables in the workstream's own messages, starting from the newest, never prompts or text that describes the format. A workstream Crush can't read sends Crush a copy of each update. Crush shows at most one row per workstream, taken from its coordinating conversation, never one per helper session.

**Posting.** Crush posts only when something is new since its last report, about five minutes past the hour, in this order:

1. **Waiting on you:** each decision waiting on the user that is new or has changed, across all workstreams, recommended answer first, with its two to four plain sentences of context and a link to where the user answers it. Crush finds them in each owner's digest and in any question the tooling shows as waiting for the user. Each is listed once, however many workstreams wait on it, under the workstream that asked first. The owning session asks it; Crush never asks it again or answers it. Crush's own questions go here too.
2. **One table** with a row only for each workstream that posted a new update, named plainly, with columns Just done, Happening now, and Next, one short sentence per cell.
3. **The machines,** one line for each machine where something changed: the model slot, a freeze, the queue, or anything Crush paused, unloaded, or moved.

When nothing is new, Crush posts nothing.

**A workstream gone quiet.** Waiting is not news, so a workstream that is only waiting, on the user or on a grant, gets no reminder. A workstream with work running and no update for 3 hours gets one short reminder, which its coordinating conversation answers to Crush alone in one line, with no table. If no answer comes within an hour, the next report says in plain words that it may have stalled. A workstream that has never posted an update gets one plain line Crush writes from its latest message, marked as Crush's summary. Crush never restarts or stops a workstream; the user or its own conversation does that.

Bad:

| | Just done | Happening now | Next |
|---|---|---|---|
| WS-2 | v0.16 READY | M3, q41 held (D7) | Gate 9 |
| WS-5 | nothing new | still waiting | same |

Good:

| | Just done | Happening now | Next |
|---|---|---|---|
| Weekly email app | The design passed its review with nothing blocking. | Building the check that only the scheduled job can send the email. | Testing sign-out on a bad connection. |
| Voice model | Downloaded the model. | Waiting for the shared machine, behind another model test, about 40 minutes. | Converting the model once its turn comes. |
