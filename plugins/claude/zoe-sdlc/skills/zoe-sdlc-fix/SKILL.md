---
name: zoe-sdlc-fix
kind: action
description: Fix a defect — evidence first, then a failing test, then the fix, with the cause recorded. For anything behaving differently from what a document says it should, whether the fault turns out to be in the code or in the document, and whether it lives in code, a specification, documentation, tooling or a process.
version: 2
---

> SDLC Base file — read-only to adopters. Do not edit. Specialise by adding
> dependent skills; improve it by sending feedback upstream.

Required Reading: `zoe-sdlc-tasks` (what a task records), `zoe-sdlc-sequencing`
(tests before code, and what "complete" means), `zoe-sdlc-templates`.

Reads: what was actually observed; the documents that say what should happen
in that area; anything nearby that might share the same cause.

Produces: the fix, the test that catches it, and the record of what allowed it.

- **Capture what happened before planning anything.** Exactly what was
  observed, not a summary of it. That is also how you know when you are done:
  the fix works when what you captured no longer happens.
- **Try to reproduce it** before fixing it. If you cannot, record what you
  tried.
- **Write the failing test first**, then fix until it passes. Where the fault
  is in a document or a process, the test is whatever repeatable check would
  have caught it — build that instead.
- **Leave it better, but only nearby.** Where it is directly related to the
  defect, clear up whatever caused the confusion — a name, a document, an
  error message — and remove any extra step it forced on people. Anything
  wider becomes its own task.
