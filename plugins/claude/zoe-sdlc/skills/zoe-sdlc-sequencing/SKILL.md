---
name: zoe-sdlc-sequencing
kind: understanding
description: The order every change follows, and what "complete" means. For any task that will change software, and for judging whether one is finished.
version: 2
---

> SDLC Base file — read-only to adopters. Do not edit. Specialise by adding
> dependent skills; improve it by sending feedback upstream.

## Specifications are the source of truth

Code exists to satisfy specifications. Work with no specification has no
definition of correct, so specify first.

When something is unclear, prefer answers in this order:

1. the requirements and specifications;
2. anything else in the project's own repository;
3. documentation and searches outside it;
4. last, what you already know — and say openly when you are relying on that.

Specifications and what is actually built are kept in step in both directions.
When they disagree, either correct the code to match the specification, or
change the specification deliberately to record what was learned. What is not
allowed is letting them quietly drift apart.

## The sequence

Every change follows this order. A step is skipped only by explicit human
decision, never just because the work was already moving.

1. **Write or update the story** — where the change is something a person or
   another system outside will notice. The story says what is wanted and in
   whose terms, and the capability that delivers it names the story it serves
   (`zoe-sdlc-stories`). A change nothing outside will notice needs no story.
2. **Specify** — the components and capabilities being changed are specified,
   or their specifications updated, before anything else.
3. **Plan the tests** — decide what will show the change is correct: which
   kinds of test apply, and what they have to cover.
4. **Check it fits the architecture** — before writing tests or code, confirm
   the structure you intend (module boundaries, which way dependencies point,
   patterns) matches the specification. Any departure from it is written down
   before it is taken. A shortcut is not taken merely because it would work.
5. **Write the tests** — before the code, against the capability contracts, so
   they exist independently of whatever ends up being written to satisfy them.
6. **Write the code** — satisfying the tests and the specification, linked to
   the capabilities it implements and uses, and meeting the project's
   engineering practices (`zoe-sdlc-adopt`).
7. **Verify** — check it matches the specification, run all the relevant tests,
   and bring every document it affected back into step.

## What "complete" means

Complete means three different things at three levels, and passing the lowest
does not earn the highest.

- **A task, component or capability** is complete when all its relevant tests
  pass and every document it affected says what was actually built. Never on
  intention or assertion. Untested code counts as not yet written: it cannot be
  the basis for calling anything done.
- **A specification edition** — one numbered revision of a specification
  (`zoe-sdlc-specify`) — is complete when it has also passed a compliance audit
  (`zoe-sdlc-audits`).
- **A release, or the project itself,** is complete only when all four checks
  have passed for the work in question (`zoe-sdlc-audits`). Tests passing says
  the code does what the specification asked. It says nothing about whether the
  specification was what anybody wanted, and that is what the four checks are
  for.
