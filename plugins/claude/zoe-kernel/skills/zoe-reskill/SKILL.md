---
name: zoe-reskill
description: Create, improve, or delete a skill from the plan.
---

> ZOE Core file — read-only.

You carry out one change to your own skills. You do not decide what to change.

Read: the single change you were given; for improve or delete, the existing skill.

Skill file frontmatter — every skill you write uses this:

```yaml
---
name: short id
kind: action | understanding
model-kind: <capability tier>  # optional; see below
description: what it does (action) or what it explains (understanding), and when to use it
version: integer; raise by one on each change
---
```

Do not copy the `zoe-` skills' frontmatter as a model.

`model-kind`: see `## Models` in the instructions. Declare it when the skill runs as its
own agent; omit it when the skill runs in the manager's own context.
Keep `description` to one sentence — most hosts load it into context every session.

Body, in this order:
- Purpose: one or two lines.
- Required Reading (if any): the skills and files to read before using this one — a parent
  skill it builds on, an understanding skill, or a reference file (a skill may keep these
  in a references/ folder beside it). Name each explicitly.
- When it runs (action skills) — the trigger. (Understanding skills are read, not run; say
  when to read them instead.)
- Reads: its inputs.
- Produces: its outputs and where they go.
- Must obey: the rules and gates that apply.
- Hand off: what runs next, if anything.
State what it does, not how to think.

Two kinds of skill: action, which does something, and understanding, which is read for
orientation; use understanding skills to record what you learn about your domain.

Orthogonality: before a create or improve goes live, check it against the orthonormal-basis
rule (`## Adding to yourself` in the instructions).

Verify before it goes live: check the skill as `## Verification` in the instructions says;
where it cannot be checked, say so in the skill.

Possible actions:
- create: write a new file in this format; record where your skills are kept in your index
  if this is the first one. A create may instead be a sub-enterprise: start another
  agent under the charter and hard rules the plan derived (no looser than yours), record it
  in your index; it reports to you.
- improve: write a new version. The target may be the enterprise instructions rather than a
  skill (see `zoe-redesign`).
- delete: remove it from your active skills

How: build the new version beside the old, check it, switch to it; never edit in place a
file you are currently running on.

Never take a gated action that has not been approved.

Log every change: what, why, and the version before and after.
