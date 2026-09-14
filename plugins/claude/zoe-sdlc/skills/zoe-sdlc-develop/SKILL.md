---
name: zoe-sdlc-develop
kind: action
description: Run an implementation task, on its own or as a batch of related tasks delivered and checked together. For building specified behaviour — one component, or work spanning several.
version: 1
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
  specification. If the work will not fit in one session, the component is too
  big: change how the system is broken up, rather than letting the task run
  over.
- **Several at once.** Work spanning more than one component, or the systems
  around them. Split off whatever can be done one component at a time;
  whatever genuinely spans them all stays in this task.

## Delivering several tasks together

Sometimes related tasks — fixes, features, specification changes — only make
sense delivered as one piece. Group them into a batch: a fixed list of tasks,
ordered so that nothing starts before what it depends on, with a stated
condition for starting and a check of the whole thing at the end.

- **Moving a task from one batch to another should be cheap**, because it
  happens often. So the link goes one way only: a batch lists its tasks, and a
  task never names its batch.
- **Wherever one piece of software talks to another, both sides are assuming
  something about the other and nobody has checked.** So find those points
  while planning — calls over a network, messages between running programs,
  calls across a language boundary — and before the batch closes, make sure at
  least one automated test makes the real call across each of them.
- Anything found along the way: if it is small and directly related, do it in
  the task you are already in. Anything more becomes a new task. The batch
  only grows with human approval.
