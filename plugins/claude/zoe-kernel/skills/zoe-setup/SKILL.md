---
name: zoe-setup
description: First setup, with a director — write the charter and index and make a blank enterprise runnable. Also used when the director revises the charter.
---

> ZOE Core file — read-only.

You run with a director present: at first setup, when a director revises the charter, or
when `zoe-orient`'s wiring check fails (fix what it found, then hand back). Reconciling an
existing enterprise to a new kernel version is `zoe-reconcile`, not this skill.

Read: the charter, index and enterprise instructions templates under this skill in `assets`.

Open the conversation yourself: say you have no goal yet and invite the director to
describe what they want, however loosely; build the charter from that with the steps
below, guiding it to a vision level.

Do, with a director, through negotiation:

- Use the charter template to create the charter.
  - Ask where the charter should live.
- If the enterprise already has assets or running processes — documents, code, accounts,
  habits — record them in the index and treat them as inherited state to bring under
  management, not to ignore.
- Task tracking: adopt any tracker already in use, else decide the store now; record it
  under `where tasks are kept` (see `zoe-tasks`).
- Storage: for each kind of record the enterprise will produce — state, log, audit
  findings, tasks, anything else — ask where it is kept, who needs to read it, and whether
  several sessions will write it at once. Record each answer in the index; one place for
  everything is allowed as a recorded decision, never a silent default.
- Decide where new skills should be created.
- **Set up the agents.** A ZOE runs as three: a **manager** that runs the cycle, a
  **redesigner** that decides what to change in its own skills, and an **assessor** that
  judges the results; the last two are read-only to the work and run as separate agents
  (`## Conduct` in the instructions). How an agent is declared is the host's business —
  work it out with the director; the ZOE project's `hosts/` folder shows worked examples,
  not a specification. Check each agent is visible and can be dispatched before you
  finish. If the host cannot run separate agents, a ZOE can still run on the manager's
  discipline alone; record that in the index as a known weakness.
- Ask whether this host can run the enterprise on a schedule with nobody present, and how it
  is started; record the answer, or a plain "no", in the index under `running unattended`.
- Create a new skill that **is** the index — a skill, not a plain file, so every host shows
  it to you. Copy the index template into its `assets`; check the skill is visible to you
  as a skill (the director may need to help); fill in the charter location and the kernel
  version (`VERSION` beside the kernel) at once.
- Create the enterprise instructions from the template in `assets`. Ask the director for any
  standing directions to start it with. Record where the file is in the index, and make sure
  this host loads it every session, the same way it loads the kernel's instructions.
- Ask whether records should quote a director's words exactly, or only say what they
  decided or asked. A quote lets a later reader check that what was said was recorded
  faithfully, but where there are several directors, each one's words are read by the rest.
  Record the answer in the index.
- Charter: ask for their vision, scope (in and out), what success looks like, constraints,
  and the hard rules — what the agent must never do, and what must get director approval
  first. Ask separately whether each of these needs approval: an agent checking its own
  work because nothing independent can; a change to the enterprise's own skills. Write the
  charter from their answers. They own and approve it; you invent neither
  the goal nor the hard rules. Where more than one director will direct the
  enterprise, ask how someone becomes one, if it is OK if any one of them can approve
  anything, and if their actions need to be audited. With more than one, agree
  too where the director-specific index and state of each are kept, record it in the
  index, and encourage each to keep a single copy of the enterprise's files.
  Ask as well who may open a management session — one standing director, a
  rota, a scheduled unattended run, whatever suits them — and record it in the index's
  `schedule` line, and make sure the task store and log will show who is working on what.
  Settle the index's `sessions` line with them too.
- Verification & checks plan, as important as the goal: for each strand of success agree
  the most checkable measure (`## Verification` in the instructions) and how often it is
  taken, and the independent audits the enterprise needs and their schedules; a blind spot
  is named, not given a number. A director reviews this.
- Ask what triggers an assessment, and what triggers a redesign.
  Record both answers in the index's `schedule` line.
- Your index: fill in what is known now — the enterprise name, the schedule, upstream, the
  director channel with its approval route explicit and how each director is identified on
  it, where feedback arrives; leave the rest for the cycle to fill as it creates things.
- Upgrade-checking: ask for a schedule or a deliberate "no" (`zoe-upgrade` says what it
  covers), record it in the index, and record the setup date in state as `last upgrade
  check`.

Hand off: once the charter is written and approved, the normal cycle takes
over at redesign (`zoe-redesign`).
