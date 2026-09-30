# Marlin: the charter and the digest

Marlin follows these steps as "Marlin keeps the voyage moving" in `SKILL.md` describes.

## The charter

Write it with the user once, at kickoff, in its own file, such as `docs/charter.md`. It holds rules the user set, so it is not part of the history file. Only the user changes it. Give it a version, bump the version with each change, and date it. Each version takes effect only once the user explicitly approves it; record who approved it and when. Setting or changing the charter is a reserved decision and never takes a default. It covers:

- **Final objective (Nemo):** what done looks like, stated as a test someone can check.
- **Milestones:** the few stops on the way, each with a result the user can see.
- **Deadline and budget:** a target date, and a limit in hours or cost, for the whole voyage and for design review.
- **Pace:** fast, balanced, or careful, as "Pick the pace" in `SKILL.md` describes, and any part of the work that runs at a different pace.
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
- **Default wait:** how long a reversible question waits for an answer before Marlin takes its default. It is 10 minutes unless the user sets another.
- **Review points:** when the user sees results, such as a demo at each milestone or the finished feature.
- **Operating limits:** quoted as the user gave them.

## Sort each decision

- **Delegated:** decide it and list it in the next digest. A decision the design depends on goes in its Decision log at the next revision, as decided under the charter's version; anything else goes in the history file, or in the implementation log during building.
- **Reversible, not delegated:** put it in the digest with a recommendation, the default Marlin will take, and when. If no answer comes by then, take the default, record it where a delegated decision would go, marked as a reversible default, and carry on. If the user later chooses differently, handle the change as a Step 8 discovery, or as a design revision before building.
- **Reserved:** put it in the digest, and wait for the answer before doing anything that depends on it. Keep doing everything else. Approval at balanced or careful pace is reserved.

When unsure which group a decision belongs to, or when it fits both a delegated and a reserved item, treat it as reserved.

## The digest

One message holds every question and every piece of news the user needs. Keep one current digest. A new question starts a new digest that replaces the current one and carries forward each unanswered item with its original default time. Gather new questions for no longer than one default wait before sending; send an escalation at once. Record each digest in the history file when it is sent. It gives:

1. where the voyage stands: the last milestone reached, the next one, the forecast against the deadline, and spend against the budget;
2. the decisions needed, reserved ones first, each with a recommendation, and for a reversible one, its default and when that takes effect;
3. what Marlin decided under the charter since the last digest, one line each;
4. what Marlin is doing meanwhile.

Send it in a way that does not stop work. If the tooling's question prompt holds the conversation until the user answers, send the digest as an ordinary message, or give the prompt a timeout, and keep working. Use a timeout or a scheduled wake-up to act when a default's time comes.

## Never idle

While a question or a review is open, do the next work that no pending answer can change: the building that "Pick the pace" lets overlap review; spikes; tests; tooling; docs. Stop only when every remaining step depends on a reserved answer, and say so in the digest.

## Escalate early

As soon as the forecast misses the deadline or the budget, or the objective looks out of reach, put it in the digest as a reserved decision. Recommend the change that gets closest to the objective: cut scope, change the pace, or move the date. When nothing is blocking, never recommend another review round.
