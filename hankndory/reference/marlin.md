# Marlin: the charter, the digest, parallel work, and Dory's update

Marlin follows these steps as "Marlin keeps the voyage moving" in `SKILL.md` describes.

## The charter

Write it with the user once, at kickoff, in its own file, such as `docs/charter.md`. It holds rules the user set, so it is not part of the history file. Only the user changes it. Give it a version, bump the version with each change, and date it. Each version takes effect only once the user explicitly approves it; record who approved it and when. Setting or changing the charter is a reserved decision and never takes a default. It covers:

- **Final objective (Nemo):** what done looks like, stated as a test someone can check.
- **Milestones:** the few stops on the way, each with a result the user can see.
- **Deadline and budget:** a target date, and a limit in agent-hours or cost, for the whole voyage and for design review. Agent-hours add up the time of every agent: Marlin and Hank, builders, reviewers, and checks, counting agents that run at the same time separately. Time a session spends waiting for a grant with its turn ended doesn't count.
- **Pace:** light, fast, balanced, or careful, as "Pick the pace" in `SKILL.md` describes, and any part of the work that runs at a different pace.
- **Delegated decisions:** what Marlin decides without asking. Unless the user narrows it, this covers:
  - reversible technical choices inside the design's contracts;
  - commits, and pushes to the project's own working branches;
  - installing dependencies within the user's operating limits;
  - running builds, tests, and spikes;
  - choosing among options the user already approved.
- **Reserved decisions:** what always waits for the user. Unless the user delegates any of it by name, this covers:
  - spending beyond the budget;
  - anything that can't be undone;
  - deleting or migrating user or production data;
  - merging into a shared or default branch, and anything that deploys;
  - public releases, store submissions, and messages to other people;
  - legal, licensing, privacy, and terms questions;
  - taste calls the user keeps, such as brand, voice, or look.
- **Accepted as built:** wording, such as interface or email text, and small extensions inside a scope already decided, that the user accepts as built without being asked. Marlin treats them as delegated. For what it names, this overrides the reserved taste calls. It never covers anything on the "Always standard" list and never sends anything to anyone. Privacy, legal, and terms wording stays reserved unless named here.
- **Default wait:** how long a reversible question waits for an answer before Marlin takes its default. It is 10 minutes unless the user sets another.
- **Review points:** when the user sees results, such as a demo at each milestone or the finished feature.
- **Operating limits:** quoted as the user gave them.
- **Updates:** where Dory's update goes, and any hours when the wake-up pauses. By default it goes to the user's Crush. The voyage sends each update to Crush as its row instead of posting it, as `reference/crush.md` describes. Without a Crush, or if the user names another place, it is posted in this voyage's own chat. An Updates line written under an earlier version that names this voyage's chat keeps it there until the user changes it.
- **Parallel streams:** any limit the user sets on how many sub-agents or sessions run at once, besides the conversation acting as Hank, counting reviewers and checks. Without one, Marlin runs as many as the independent work, the tooling, and the budget allow. A charter without this line has no limit and needs no new version.
- **Shared machines:** each machine the voyage uses that other projects also use, which the user's Crush routes, as `reference/crush.md` describes. A charter without this line needs no new version, but heavy work on a shared machine still asks the user's Crush.
- **Backup remote:** where Marlin pushes the backups "Back up at every gate" describes. If the project's own remote is public or isn't the user's, ask the user for a private one.

## Sort each decision

- **Delegated:** decide it and list it in the next digest. A decision the design depends on goes in its Decision log at the next revision, as decided under the charter's version; anything else goes in the history file, or in the implementation log during building.
- **Reversible, not delegated:** put it in the digest with a recommendation, the default Marlin will take, and when. If no answer comes by then, take the default, record it where a delegated decision would go, marked as a reversible default, and carry on. If the user later chooses differently, handle the change as a Step 8 discovery, or as a design revision before building.
- **Reserved:** put it in the digest, and wait for the answer before doing anything that depends on it. Start or keep doing everything else, as "Start everything allowed, in parallel" describes. Approval at balanced or careful pace is reserved.

When unsure which group a decision belongs to, or when it fits both a delegated and a reserved item, treat it as reserved.

## The digest

One message holds every question and every piece of news the user must act on. Keep one current digest. A new question starts a new digest that replaces the current one and carries forward each unanswered item with its original default time. Gather new questions for no longer than one default wait before sending; send an escalation at once. Record each digest in the charter's history file, such as `docs/charter.history.md`, when it is sent. It gives:

1. where the voyage stands: the last milestone reached, the next one, the forecast against the deadline, and spend against the budget;
2. the decisions needed, reserved ones first, each asked as "Ask with context" describes, and for a reversible one, its default and when that takes effect;
3. what Marlin decided under the charter since the last digest, one line each;
4. the work streams running meanwhile.

When the voyage sends updates to Crush, it also tells Crush in one line when an item waiting on the user is answered, withdrawn, or settled by its default.

Send it in a way that does not stop work. If the tooling's question prompt holds the conversation until the user answers, send the digest as an ordinary message, or give the prompt a timeout, and keep working. Use a timeout or a scheduled wake-up to act when a default's time comes.

## Talk to the user in plain words

Everything addressed to the user, including digests, questions, and Dory's update, uses short sentences in everyday words. Never use internal labels there: no document or review numbers, design versions, milestone, step, gate, or finding codes, item IDs, or commit hashes. Documents the user asks to see, such as a review or the design itself, keep their labels, but any summary of them names things. Name the thing instead. Say "the check that only the scheduled job can send the weekly email", not "A8", and "the design for sign-out", not "Doc 3 v0.16". Links are fine as long as the sentence makes sense without them.

## Ask with context

Every question to the user opens with:

1. the recommendation, in one line that makes sense on its own;
2. two to four plain sentences: what this is, why it needs deciding now, and what each option changes for the user in time, money, or risk;
3. the options, recommended one first.

Bad: "Review #2 on Doc 12 flagged A8 as NOT READY. Approve the v0.17 scope change?"

Good: "I recommend fixing who can send the weekly email before we build it. The design for the weekly email left out who may send it, and building it starts next. The fix lets only the scheduled job send it, so no one can send one by hand. Saying yes adds about 20 minutes and no cost; saying no risks the occasional duplicate email. Options: fix it first (recommended); build it as is."

## Dory's update

Marlin writes it in Dory's voice, for someone who has just walked in; no Dory reviewer writes or sees it. A voyage runs from the charter, or from Step 1 without one, until the final objective is met or the user stops it. At kickoff, or at the next step of a voyage started under an earlier version, set up a recurring hourly wake-up that resumes the current Hank conversation and checks for new progress; a charter without an Updates line uses the default and needs no new version. If the tooling can only start a new conversation on a schedule, that conversation reads the charter's history file, posts or sends an update, as the Updates line says, if there is new progress, and does nothing else. A Hank handoff moves the wake-up to the new conversation, as `reference/hank-handoff.md` describes.

Post an update only when there is new progress since the last one: something finished, started, or changed course. Waiting, "still running", and "no change" are not progress, so the wake-up posts nothing then. If Crush sends a reminder, answer Crush in one line with what is still running; that is not an update. Stop the wake-up when the voyage ends or the user pauses it, and set it up again when the user resumes. Record each update's time, Status, and Just done line in the charter's history file. Send or post it as the Updates line says. The update is a table of five rows, each cell one or two short sentences, following "Talk to the user in plain words". Happening now names each stream in a short phrase, grouping alike ones, such as "three test runs", then anything waiting on the user, and why. It may run past two sentences. Progress gives the share of the final objective done, as a rough percent, and the forecast finish, as a day and time, such as Thursday evening, or as hours left when it is less than a day away. Estimate the share as each finished milestone's share of the estimated agent-hours, plus the finished part of the current one, and use the same forecast the digest gives. Without a charter, write "not set yet". A forecast that moves counts as new progress. Status is one word, then, for Blocked or Issues, one short sentence on what and why. Use these three words exactly; the user chose them:

- **LGTM:** going well and on course.
- **Blocked:** some part of the plan cannot go on until the user acts, such as a reserved decision or a task only the user can do. Name it, and it is also listed in the digest. If Marlin may take the recommended path under the charter, it takes it, and the voyage is not Blocked. A reversible question waiting for its default is not Blocked either; Marlin takes the default when its time comes. A user decision that is coming but not yet holding up work is not Blocked, and neither is waiting in Crush's queue.
- **Issues:** something the plan didn't foresee needs a fix or a workaround, and it is being worked on without the user.

When more than one fits, use Blocked, then Issues. A change of status counts as new progress:

| | |
|---|---|
| **Status** | LGTM, Blocked, or Issues, and for the last two, what and why |
| **Just done** | what finished since the last update |
| **Happening now** | each stream being worked on, and anything waiting on the user, and why |
| **Next** | what comes after that |
| **Progress** | about how much of the final objective is done, and when it should be finished |

Bad:

| | |
|---|---|
| **Status** | Amber, see D7. |
| **Just done** | Doc 12 v0.16 passed Review #2; A8 closed at 3f9c2e1. |
| **Happening now** | Step 9 on M3, L3 pending. |
| **Next** | Gate 5 after the 5b rerun. |
| **Progress** | M2 of M4, 0.62. |

Good:

| | |
|---|---|
| **Status** | Issues. Sign-out on a bad connection kept the old account's notifications; the fix is being tested. |
| **Just done** | The design for the weekly email passed its review, with nothing blocking. |
| **Happening now** | Three things at once: building the check that only the scheduled job can send the weekly email, testing sign-out on a bad connection, and drafting the release notes. Publishing will need your OK, because only you can approve a public release. |
| **Next** | Then we send you the release to approve, once the sign-out fix passes. |
| **Progress** | About 60% done. Should be finished Thursday evening. |

Also bad: any table when nothing moved, such as "Still waiting for the review" in every row. Post nothing instead.

The update carries no questions. Questions go in the digest, and the update points to it when one is waiting.

## Back up at every gate

When a gate closes, and when approval or a handoff happens, commit and push to the backup remote: each design document and its history file, the charter and its history file, and the working branches. This guards against losing a machine mid-voyage. Pushing to the backup remote is delegated; merging into a shared or default branch stays reserved. Push only branches that are not shared or default, never force-push, and never push to a remote where a push deploys. If the project's own remote is public or isn't the user's, push the design documents, the charter, and their history files only to the backup remote. With no backup remote named, skip the backup and say so in the digest.

## Start everything allowed, in parallel

At every pace, start at once every piece of work that the charter, the current approvals, and this skill's rules already allow. Allowed work never waits for a gate, digest, or answer it does not depend on. A reserved question holds back only the work that depends on its answer; everything else carries on. The pace still decides what is allowed. Building before approval happens only where "Pick the pace" in `SKILL.md` lets it overlap review.

Run independent streams at the same time, each in its own sub-agent or session where the tooling allows: research, spikes, drafts, tests, tooling, docs, reviews, and building inside an approved design or a component the pace lets overlap review. Two streams are independent when neither needs the other's result and they change different files, apart from each one's own part of the implementation log. Running in parallel changes no other rule. In particular:

- Start each stream with only its task, the user's operating limits and standing instructions, quoted as the user gave them, the reserved list, and, for a stream that runs on a shared machine, the user's Crush, the machine's light-work line, and what its house rules keep for the user. A stream that reaches anything reserved stops that part and reports back. Set it a stall time, as for a reviewer; for a stream queued with Crush, it starts when the grant arrives.
- Each stream writes its result to its branch or a file and sends one short final report. Record each stream in the charter's history file when it starts and when it returns: what it does, its branch or output, and where its result will arrive.
- Other streams report back to the conversation acting as Hank and leave to it everything `reference/hank-handoff.md` says only Hank does. Each Dory reviewer still runs fresh, as "Choose where each reviewer runs" in `SKILL.md` describes.
- While a batch runs, no stream edits the design document or a referenced file, except as "Freeze the document" in `SKILL.md` allows.
- Give each building stream its own branch in its own worktree or clone. A stream that must change another stream's file stops and reports back. Hank changes a stream's branch only after it returns, and merges finished building branches into one branch that is not shared or default. Step 9 reviews that branch.
- A stream that needs heavy work on a shared machine asks the user's Crush for machine time as soon as the stream is known, and every other stream starts meanwhile. A stream queued with Crush is not idle. When the charter names a shared machine, also follow "How Crush fits the other rules" in `reference/crush.md`.
- Every stream counts toward the budget. When the charter's stream limit is reached, run first the streams that bring the final objective closest. When the remaining work no longer fits the budget, escalate as "Escalate early" describes.

At each check-in, whenever a stream or batch returns, a digest or update goes out, or the hourly wake-up runs, check that nothing allowed is sitting idle, and start it. Stop only when every remaining step depends on a reserved answer, and say so in the digest.

## Escalate early

As soon as the forecast misses the deadline or the budget, or the objective looks out of reach, put it in the digest as a reserved decision. Recommend the change that gets closest to the objective: cut scope, change the pace, or move the date. When nothing is blocking, never recommend another review round.
