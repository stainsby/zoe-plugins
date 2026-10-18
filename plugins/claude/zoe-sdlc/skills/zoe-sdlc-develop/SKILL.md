---
name: zoe-sdlc-develop
kind: action
description: Run an implementation task, on its own or as a batch of related tasks delivered and checked together. For building specified behaviour — one component, or work spanning several.
version: 3
---

> SDLC Base file — read-only to adopters. Do not edit. Specialise by adding
> dependent skills; improve it by sending feedback upstream.

Required Reading: `zoe-sdlc-sequencing` (the order the work follows),
`zoe-sdlc-tasks` (what the task must record), `zoe-sdlc-components` (what is
being built), `zoe-sdlc-templates` (the task is made from a template).

Reads: the specifications of the components being changed, at their current
edition; the stories those specifications name; the dependency graph around
them.

Produces: the implementation.

An implementation task covers either one component or several.

- **One component.** The task builds a single component against its
  specification. If the work will not fit in one sitting (`zoe-sdlc-components`), the
  component is too big: change how the system is broken up, rather than letting the task run
  over.
- **Several at once.** Work spanning more than one component, or the systems
  around them. Split off whatever can be done one component at a time;
  whatever genuinely spans them all stays in this task.

## Delivering several tasks together

Sometimes related tasks — fixes, features, specification changes — only make
sense delivered as one piece. Group them into a batch: a fixed list of tasks
in dependency order, with an entry condition and a check of the whole at the
end.

- **A batch lists its tasks, and a task never names its batch**, so moving a
  task from one batch to another stays cheap.
- **Test every integration point** — network calls, inter-process messages,
  foreign-function calls. Find them while planning, and before the batch closes
  cover each with at least one automated test that makes the real call,
  unmocked.
- Anything found along the way: if it is small and directly related, do it in
  the task you are already in. Anything more becomes a new task. The batch
  only grows with a director's approval.
