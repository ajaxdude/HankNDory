# Bootstrap context for an existing codebase

The `bootstrap-context` mode in `SKILL.md` follows this file.

Use this mode when the repository is too large to understand directly and lacks sufficient design-document coverage.

## Generate leaf README files

1. Inventory the source tree and exclude generated, vendored, dependency, cache, build-output, binary, and secret-bearing directories.
2. Start with leaf directories containing meaningful project-owned source.
3. Read all relevant files in one leaf directory.
4. Create or update `README.md` in that directory with:
   - directory purpose;
   - role in the larger system, if verifiable;
   - key flows, invariants, and dependencies;
   - an enumeration of each meaningful file and its function;
   - known uncertainties requiring human verification.
5. Ask or require an assigned human to verify and correct the README. Do not mark it verified automatically.

## Roll up parent README files

Move upward one level at a time:

1. Read verified child `README.md` files.
2. Read project-owned files directly in the current directory.
3. Create or update the current directory's `README.md` with its purpose, subsystem relationships, important flows, and direct-file inventory.
4. Preserve links to child READMEs instead of duplicating their full contents.
5. Require human verification at meaningful subsystem boundaries.
6. Continue until the repository root is summarized.

## Maintain README quality

- Prefer compressed, high-signal context over exhaustive code paraphrase.
- Never claim human verification when none occurred.
- Flag contradictions between code, existing docs, and generated summaries.
- Preserve existing README content unless the user authorizes replacement; merge carefully.
- Keep generated documentation reviewable in small commits.
- Refresh summaries when referenced code changes materially.

README files may be removed only when the user has verified that design documents provide complete file coverage and no workflow or human reader still depends on them. Do not assume 100 percent coverage from search absence; calculate it from an explicit repository inventory and design-document reference index.
