---
name: zoe-sdlc-adopt
kind: action
description: Bring a software project — new or existing — under this process, extending `zoe-setup`. For the single pass at the start, and again only if the project's foundations genuinely shift.
version: 8
---

> SDLC Base file — read-only to adopters. Do not edit. Specialise by adding
> dependent skills; improve it by sending feedback upstream.

Required Reading: `zoe-setup`, which this extends; then `zoe-sdlc-components`,
`zoe-sdlc-tasks`, `zoe-sdlc-sequencing`, `zoe-sdlc-templates`.

Reads: the enterprise's charter; whatever the project already has — trackers,
repositories, READMEs, vision documents, conventions.

Produces:

- the approval points this project keeps, written into the charter's hard
  rules;
- the decisions listed in step 2, recorded in the index alongside the ones
  `zoe-setup` records;
- the three checks, written and runnable;
- the specifications of the top-level components;
- the project task, open.

Steps:

1. **Charter.** Nothing below the charter ever quotes it or points back at it.
   It applies to everything under it automatically.

   **This process's approval points go into its hard rules.** The instructions
   list the points where a person approves before work goes on. Ask the
   director which of them this project keeps, and write those into the
   charter's hard rules as things to ask first. Only the hard rules make an
   action gated, and they are what every agent doing the work is given,
   including one launched for a single task. An instructions file is not always
   in front of that agent.
2. **Decide these too.**

   Each one gives this project a concrete answer to something the process
   states in general, and each is recorded once, with the decisions `zoe-setup`
   already asked for. The skill named beside a decision is where it is
   explained.

   - **What the task store must hold** — the store itself is `zoe-setup`'s
     question. This process asks more of it: everything in `zoe-sdlc-tasks`.
     Record where each part lives in the chosen store, and if it will not fit,
     say so now rather than working around it later.
   - **The identifier convention** — for components and capabilities
     (`zoe-sdlc-components`).
   - **The traceability mechanism** — how code declares the capabilities it
     implements and uses (`zoe-sdlc-components`).
   - **The template forms** — what shapes each kind of structured document.
     Adopt whatever the project already uses; make one only where there is
     nothing (`zoe-sdlc-templates`).
   - **What counts as one session** — the size limit on a task and on a leaf
     component, in terms two people would agree on from the outside
     (`zoe-sdlc-components`).
   - **The engineering practices** — what this project holds code to beyond
     passing its tests (`zoe-sdlc-sequencing`).
   - **The verification setup** — how the tests are run, what "all relevant
     tests" means for a given change, and where the evidence is kept. A project
     with no way to run tests makes building one its first piece of work.
   - **The environments** — which ones the project has, which one acceptance
     testing runs against, and what makes a test environment close enough to
     production to trust its results (`zoe-sdlc-components`).
   - **How often the charter audit runs** — `zoe-setup` asks which independent
     checks this enterprise needs and how often each runs. This process brings
     four (`zoe-sdlc-audits`). Three of them start on an event; the charter
     audit has none, so it needs a time.
   - **Who provides the independent eyes for each audit** — a separate agent,
     a session that has not carried the work's context, or a different person.
     Arranging nothing is not one of the choices (`zoe-sdlc-audits`).
3. **Create three checks**, one for each of these:
   - The capability dependency graph is valid (`zoe-sdlc-components`).
   - Code and capabilities match in both directions (`zoe-sdlc-components`).
   - The references between the project's own documents resolve — a
     specification naming a component, a task citing a capability, a link to a
     template. These break silently: a document pointing at a file that no
     longer exists looks exactly like one pointing at a file that does, and a
     rename anywhere upstream is enough to cause it.

   Run them wherever the project already runs its tests.
4. **Break the system into components** per `zoe-sdlc-components`.
5. **Open the standing project task** per `zoe-sdlc-tasks`, and create the first
   real tasks. For an existing codebase, assimilation itself becomes task
   work: inventory what exists, then bring it under specification, linking,
   and test coverage incrementally — region by region under its own tasks,
   ordered by where change actually happens — rather than in one heroic
   rewrite of the project's paperwork.

Hand off: everyday work under `zoe-sdlc-sequencing` and the task-type skills;
alignment over time to the audits (`zoe-sdlc-audits`).
