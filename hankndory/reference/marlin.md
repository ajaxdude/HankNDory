# Marlin: the charter, the digest, parallel work, and the hourly update

Marlin follows these steps as "Marlin keeps the voyage moving" in `SKILL.md` describes.

## The charter

Write it with the user once, at kickoff, in its own file, such as `docs/charter.md`. It holds rules the user set, so it is not part of the history file. Only the user changes it. Give it a version, bump the version with each change, and date it. Each version takes effect only once the user explicitly approves it; record who approved it and when. Setting or changing the charter is a reserved decision and never takes a default. It covers:

- **Final objective (Nemo):** what done looks like, stated as a test someone can check.
- **Milestones:** the few stops on the way, each with a result the user can see.
- **Deadline and budget:** a target date, and a limit in agent-hours or cost, for the whole voyage and for design review. Agent-hours add up the time of every agent: Marlin and Hank, builders, reviewers, and checks, counting agents that run at the same time separately.
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
- **Hourly update:** where Dory's hourly update goes, which is the chat the user reads for this voyage unless the user names another, and any hours when it pauses.
- **Parallel streams:** any limit the user sets on how many sub-agents or sessions run at once, besides the conversation acting as Hank, counting reviewers and checks. Without one, Marlin runs as many as the independent work, the tooling, and the budget allow. A charter without this line has no limit and needs no new version.
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

Send it in a way that does not stop work. If the tooling's question prompt holds the conversation until the user answers, send the digest as an ordinary message, or give the prompt a timeout, and keep working. Use a timeout or a scheduled wake-up to act when a default's time comes.

## Talk to the user in plain words

Everything addressed to the user, including digests, questions, and the hourly update, uses short sentences in everyday words. Never use internal labels there: no document or review numbers, design versions, milestone, step, gate, or finding codes, item IDs, or commit hashes. Documents the user asks to see, such as a review or the design itself, keep their labels, but any summary of them names things. Name the thing instead. Say "the check that only the scheduled job can send the weekly email", not "A8", and "the design for sign-out", not "Doc 3 v0.16". Links are fine as long as the sentence makes sense without them.

## Ask with context

Every question to the user opens with:

1. the recommendation, in one line that makes sense on its own;
2. two to four plain sentences: what this is, why it needs deciding now, and what each option changes for the user in time, money, or risk;
3. the options, recommended one first.

Bad: "Review #2 on Doc 12 flagged A8 as NOT READY. Approve the v0.17 scope change?"

Good: "I recommend fixing who can send the weekly email before we build it. The design for the weekly email left out who may send it, and building it starts next. The fix lets only the scheduled job send it, so no one can send one by hand. Saying yes adds about 20 minutes and no cost; saying no risks the occasional duplicate email. Options: fix it first (recommended); build it as is."

## Dory's hourly update

Dory remembers nothing, so this update is written for someone who has just walked in. Marlin writes it; the name is about the reader. A voyage runs from the charter, or from Step 1 without one, until the final objective is met or the user stops it. At kickoff, or at the next step of a voyage started under an earlier version, set up a recurring hourly wake-up that resumes the current Hank conversation and posts the update where the charter says; a charter without an Hourly update line uses the default and needs no new version. If the tooling can only start a new conversation on a schedule, that conversation reads the charter's history file, posts the update, and does nothing else. A Hank handoff moves the wake-up to the new conversation, as `reference/hank-handoff.md` describes. Post it every hour while the voyage is running, even when little changed. When all work waits on the user, post once, then pause until the answer. Stop when the voyage ends or the user pauses it, and set it up again when the user resumes. Record each update's time and Just done line in the charter's history file. It is a table of three rows, each cell one or two short sentences, following "Talk to the user in plain words". Happening now names each stream in a short phrase, grouping alike ones, such as "three test runs", then anything waiting on the user, and why. It may run past two sentences:

| | |
|---|---|
| **Just done** | what finished since the last update |
| **Happening now** | each stream being worked on, and anything waiting on the user, and why |
| **Next** | what comes after that |

Bad:

| | |
|---|---|
| **Just done** | Doc 12 v0.16 passed Review #2; A8 closed at 3f9c2e1. |
| **Happening now** | Step 9 on M3, L3 pending. |
| **Next** | Gate 5 after the 5b rerun. |

Good:

| | |
|---|---|
| **Just done** | The design for the weekly email passed its review, with nothing blocking. |
| **Happening now** | Three things at once: building the check that only the scheduled job can send the weekly email, testing sign-out on a bad connection, and drafting the release notes. Publishing will need your OK, because only you can approve a public release. |
| **Next** | Then we fix whatever the tests turn up and send you the release to approve. |

The update carries no questions. Questions go in the digest, and the update points to it when one is waiting.

## Back up at every gate

When a gate closes, and when approval or a handoff happens, commit and push to the backup remote: each design document and its history file, the charter and its history file, and the working branches. This guards against losing a machine mid-voyage. Pushing to the backup remote is delegated; merging into a shared or default branch stays reserved. Push only branches that are not shared or default, never force-push, and never push to a remote where a push deploys. If the project's own remote is public or isn't the user's, push the design documents, the charter, and their history files only to the backup remote. With no backup remote named, skip the backup and say so in the digest.

## Start everything allowed, in parallel

At every pace, start at once every piece of work that the charter, the current approvals, and this skill's rules already allow. Allowed work never waits for a gate, digest, or answer it does not depend on. A reserved question holds back only the work that depends on its answer; everything else carries on. The pace still decides what is allowed. Building before approval happens only where "Pick the pace" in `SKILL.md` lets it overlap review.

Run independent streams at the same time, each in its own sub-agent or session where the tooling allows: research, spikes, drafts, tests, tooling, docs, reviews, and building inside an approved design or a component the pace lets overlap review. Two streams are independent when neither needs the other's result and they change different files, apart from each one's own part of the implementation log. Running in parallel changes no other rule. In particular:

- Start each stream with only its task, the user's operating limits and standing instructions, quoted as the user gave them, and the reserved list. A stream that reaches anything reserved stops that part and reports back. Set it a stall time, as for a reviewer.
- Each stream writes its result to its branch or a file and sends one short final report. Record each stream in the charter's history file when it starts and when it returns: what it does, its branch or output, and where its result will arrive.
- Other streams report back to the conversation acting as Hank and leave to it everything `reference/hank-handoff.md` says only Hank does. Each Dory reviewer still runs fresh, as "Choose where each reviewer runs" in `SKILL.md` describes.
- While a batch runs, no stream edits the design document or a referenced file, except as "Freeze the document" in `SKILL.md` allows.
- Give each building stream its own branch in its own worktree or clone. A stream that must change another stream's file stops and reports back. Hank changes a stream's branch only after it returns, and merges finished building branches into one branch that is not shared or default. Step 9 reviews that branch.
- Every stream counts toward the budget. When the charter's stream limit is reached, run first the streams that bring the final objective closest. When the remaining work no longer fits the budget, escalate as "Escalate early" describes.

At each check-in, whenever a stream or batch returns or a digest or hourly update goes out, check that nothing allowed is sitting idle, and start it. Stop only when every remaining step depends on a reserved answer, and say so in the digest.

## Escalate early

As soon as the forecast misses the deadline or the budget, or the objective looks out of reach, put it in the digest as a reserved decision. Recommend the change that gets closest to the objective: cut scope, change the pace, or move the date. When nothing is blocking, never recommend another review round.
