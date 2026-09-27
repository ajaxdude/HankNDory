# Plain-speech checklist

Adapted from [unslop](https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md) for design-document prose. Hank applies it actively during the "Plain-speech pass" at the end of Phase 2, and again to any prose section revised afterward. Dory's Step 6 critic review references it passively, to flag any slop that survived Hank's pass.

## Where this applies

Prose sections: Problem, Technical plan, the narrative parts of Architecture and flows, Alternatives considered, Risks and mitigations, and Rollout, migration, and rollback.

Not Detailed implementation's file-by-file entries, Referenced files, the Decision log, or the Dory validation record. Keep those terse, structured, and list-based. Forcing them into paragraph prose would make the document harder to implement from, not easier.

## Process

1. Reread every in-scope section.
2. Rewrite anything the checklist below flags.
3. Preserve every technical claim, citation, file path, and open question. Cutting a sentence must never delete a requirement, a rejected alternative, or a verified-versus-assumed distinction.

## Vocabulary

- Replace inflated words with plain ones: crucial, delve, enduring, fostering, garner, interplay, intricate, landscape, pivotal, robust, seamless, showcase, tapestry, testament, underscore, vibrant, leverage, utilize, facilitate, numerous.
- Say "is" or "has" instead of "serves as", "stands as", "boasts", "features".
- Replace vague metaphor nouns with the concrete mechanism: substrate, vector (when it means "way", not an actual vector), nexus, locus, vantage, bedrock, north star, flywheel, paradigm, modality, ratchet (as metaphor), evacuate (for moving code), endgame. Established engineering terms stay as is: primitive, API surface, test harness, scaffolding (generated code), gold-plating.
- Name the same component, file, or concept the same way every time it appears. Synonym cycling ("the service", "the layer", "the module" for one thing) reads fine in an essay; here it breaks Dory's ability to trace a claim back to one referenced file.

## Filler and hedging

- "In order to" becomes "to". "Due to the fact that" becomes "because". Delete "it is important to note that".
- Collapse stacked hedges ("could potentially possibly be argued") into one honest hedge, or replace it with the actual confidence level and evidence.
- Delete generic claims ("this will greatly improve reliability") and state the specific, testable outcome instead.

## Structure and voice

- Say what a decision does, not how it feels. Replace "keeps the system responsive" with the number or mechanism that makes it true.
- Prefer active voice and name the actor: "requests are validated" becomes "the gateway validates requests."
- Cut an adverb propping up a weak verb, or use a stronger verb: state the number instead of "significantly" or "quickly."
- Split a sentence the reader has to re-read to parse. One claim per sentence.
- Do not force ideas into a rule of three. Use the count the content actually needs.
- State "not just X, but Y" as the direct point instead.

## Style

- No em dashes. Use a period or comma.
- Use a colon only before a list or example, never as a mid-sentence connector.
- Do not bold a proper noun or heading lead-in that only restates the sentence following it.
- Sentence case for headings. No decorative emoji. Straight quotes.

## What never to touch

- Citations, file paths, version numbers, and code identifiers: never alter these while editing the prose around them.
- Detailed implementation's file entries, Referenced files, the Decision log, and the Dory validation record: these stay terse and structured, per "Where this applies" above.
