---
name: zoe-sdlc-tasks
kind: understanding
description: What this process asks of every task. For planning, starting or finishing any piece of software work.
version: 2
---

> SDLC Base file — read-only to adopters. Do not edit. Specialise by adding
> dependent skills; improve it by sending feedback upstream.

## All work runs under a task

Planning, specifying, building, debugging, testing and documenting are all task
work. Work with no task has nowhere to record why it was done or what came of
it. Finding such work under way is a planning defect: give it a task before
carrying on. There are trivial exceptions, but when in doubt, it is a task.

A project keeps one standing task — one that is always open — for the project
itself, holding its overall status, its releases, and anything that spans more
than one task. That way there is never a moment with no task open and nowhere
to record a discovery.

## What every task records

Whatever its type, and wherever it is kept, a task records four things over its
life:

- **What it is for, written before the work starts** — its context and scope,
  its goal, the documents it answers to, what it is assuming, and how anyone
  will know it went well.
- **What was actually done**, with the evidence: test output, differences in
  the code, measurements. A claim with nothing behind it does not count towards
  finishing.
- **What the results mean** against that goal and those assumptions: what held
  up, what was a surprise, what is now better understood.
- **What follows** — decisions taken, further tasks worth doing, and anything
  the work suggests changing about the process itself.

These are four things to record, not a document layout. In a tracker they may
be fields and comments; in files they may be sections. Where each one lives is
settled at adoption, along with the completion criterion and the task type (see
`zoe-sdlc-adopt`). A store that cannot hold one of them is a problem to solve
then, not to discover once work is under way.

## Stopping short

A task that stops without meeting its completion criterion is abandoned, with
the reason recorded, or split. It is never quietly left open. When a task
counts as finished is `zoe-sdlc-sequencing`.

## Task types

A task type carries its own required structure and rules. Four come with this
base, one for each kind of work it knows how to run: building something
(`zoe-sdlc-develop`), fixing a defect (`zoe-sdlc-fix`), specifying
(`zoe-sdlc-specify`), and writing stories (`zoe-sdlc-stories`). Audit work runs
under a task too, but its structure is in `zoe-sdlc-audits` rather than a type
of its own. Add your own types for work these do not cover.

New work takes the most specific type that fits. If a task cannot fit its
type's structure, say so as a proposed improvement rather than quietly working
around it.
