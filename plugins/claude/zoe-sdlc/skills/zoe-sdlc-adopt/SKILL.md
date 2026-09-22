---
name: zoe-sdlc-adopt
kind: action
description: Bring a software project — new or existing — under this process, extending `zoe-setup`. For the single pass at the start, and again only if the project's foundations genuinely shift.
version: 9
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

   **This process's approval points go into its hard rules.** Ask the director
   which of the points the instructions list this project keeps, and write
   those into the charter's hard rules as things to ask first. Only the hard
   rules make an action gated, and every agent doing the work is given them,
   including one launched for a single task, which might not be given an
   instructions file.
2. **Decide these too.** Each is recorded once, with the decisions `zoe-setup`
   made; the skill named beside it explains it.

   - **What the task store must hold** — the store itself is chosen in
     `zoe-setup`. This process asks more of it: everything in `zoe-sdlc-tasks`.
     Record where each part lives in the chosen store, and if it will not fit,
     say so now rather than working around it later.
   - **The identifier convention** — for components and capabilities
     (`zoe-sdlc-components`).
   - **The traceability mechanism** — how code declares the capabilities it
     implements and uses (`zoe-sdlc-components`).
   - **The template forms** — what shapes each kind of structured document.
     Adopt whatever the project already uses; make one only where there is
     nothing (`zoe-sdlc-templates`).
   - **The size limit** — how much fits in one sitting, for a task and a leaf
     component, in terms two people would agree on from the outside; or that it
     cannot yet be set, and why (`zoe-sdlc-components`).
   - **The engineering practices** — what this project holds code to beyond
     passing its tests (`zoe-sdlc-sequencing`).
   - **The verification setup** — how the tests are run, what "all relevant
     tests" means for a given change, and where the evidence is kept. A project
     with no way to run tests makes building one its first piece of work.
   - **The environments** — which ones the project has, which one acceptance
     testing runs against, and what makes a test environment close enough to
     production to trust its results (`zoe-sdlc-components`,
     `zoe-sdlc-audits`).
   - **How often the charter audit runs** — the other three checks start on an
     event; this one has none, so it needs a time (`zoe-sdlc-audits`).
   - **Who provides the independent eyes for each audit** — a separate agent,
     a fresh conversation that has not carried the work's context, or a
     different person. Arranging nothing is not one of the choices
     (`zoe-sdlc-audits`).
3. **Create three checks**, one for each of these:
   - The capability dependency graph is valid (`zoe-sdlc-components`).
   - Code and capabilities match in both directions (`zoe-sdlc-components`).
   - The references between the project's own documents resolve — a
     specification naming a component, a task citing a capability, a link to a
     template. These break silently.

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
