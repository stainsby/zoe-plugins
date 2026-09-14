---
name: zoe-sdlc-specify
kind: action
description: Write or update a component's specification. For any component about to be implemented, and any whose contract, dependencies or constraints have changed.
version: 3
---

> SDLC Base file — read-only to adopters. Do not edit. Specialise by adding
> dependent skills; improve it by sending feedback upstream.

Required Reading: `zoe-sdlc-components` (what is being specified),
`zoe-sdlc-templates` (a specification is made from a template),
`zoe-sdlc-stories` (what a user-facing capability names).

Reads: where the component sits in the hierarchy and the specifications either
side of it; the stories in scope; the project's specification template.

Produces: the component's specification, wherever the project keeps them.
Whatever its format, it says:

- what the component is, and where it sits in the hierarchy;
- what constrains it, including the environments it has to work in;
- every capability it owns, each with its full contract and who it serves;
- the capabilities it uses from other components;
- the same dependencies again in a form a program can read and check;
- how it will be tested — every capability it owns, both on its own and
  against the capabilities it uses.

A specification that cannot yet state a capability's contract is not ready for
review.

## Editions

Each significant revision is a numbered edition, and moves strictly in order
through: specification, human review, implementation, compliance audit,
testing. No edition's status moves except by doing the work it names. The
current edition and how far it has got are recorded with the specification.
Do not keep a history of editions in the specification unless there is a
specific rule to do so.

## Checking the graph

After writing or editing, and always before an edition's specification stage is
marked done, run the project's check of the capability dependency graph
(`zoe-sdlc-components`). Anything it reports blocks completion. Fix it in the
specifications, with the human where the fix is a design decision.
