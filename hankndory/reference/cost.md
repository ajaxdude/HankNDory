# Cost policy

`SKILL.md` points here from "Keep Hank's conversation short" and "Choose where each reviewer runs". Agents spend money every time they read their context, so most of a voyage's cost comes from helpers, long conversations, and checks repeated too often. This is the default for every voyage and for Crush. The charter's **Cost** line may change any part of it, and only the user changes that line.

## Two model tiers

- **Strong tier:** the conversation acting as Hank, which makes the decisions, and every review gate that decides go or no-go: each Dory reviewer and critic round, each `dory-pass`, and Bruce's Step 9 review and re-review. They run on a strong model at high reasoning effort, never the maximum unless the charter sets it. Every other rule in "Choose where each reviewer runs" still applies to the gates.
- **Helper tier:** every other sub-agent or child session: exploring, running tasks, building, running tests, monitoring, Bailey's spikes and experiments, Ray's acceptance tests, drafting, summarising, and Hank's checks, including any whole-document check run alongside a batch. They run on a model much cheaper per call than the strong tier, at medium effort. A helper's work is checked by the tests, Hank, or a review gate, never trusted on its own.

Crush's own conversation decides grants, so it runs on the strong tier unless its house rules name another, and its own helpers have their own cap of three, apart from every voyage's.

At kickoff, name the actual model and effort for each tier in the charter's Cost line. A helper task that fails its own checks twice goes back to Hank, who decides the next step; record that in the charter's history file.

## At most three at once

At most three helpers and reviewers run at once per voyage, counting sub-agents, background agents, and child sessions together, but not the conversation acting as Hank. When more are running, let each finish its current task, and start no new one until fewer than three run. Choose which allowed work starts first by what unblocks the most, review gates first. This cap is the default for the charter's "Parallel streams" line.

## Check at most once an hour

Wait for the tooling's notice that a stream or reviewer has finished. Never check on running work more than once an hour. One wake-up at a stall time is fine, once per run, never repeated. Any timer or session automation that repeats does so at most once an hour, or is driven by events instead.

## Hand off a long conversation

When a conversation's context passes about 300,000 tokens, write a short handoff and carry on in a fresh conversation, instead of sending the whole context with every call. Hank, who also plays Marlin, follows `reference/hank-handoff.md` at any point, not only after a batch, titling the entry `Handoff at <size>`. Crush and any other long-running conversation write the handoff in their history file: what is done, what is running and where its result will arrive, what comes next, and the open items.
