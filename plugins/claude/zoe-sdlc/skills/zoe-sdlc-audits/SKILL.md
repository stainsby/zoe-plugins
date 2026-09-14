---
name: zoe-sdlc-audits
kind: understanding
description: Perform charter, fulfilment and compliance audits, and acceptance testing. For planning, running or judging any of them, and for working out which one you need.
version: 4
---

> SDLC Base file — read-only to adopters. Do not edit. Specialise by adding
> dependent skills; improve it by sending feedback upstream.

## The four checks

Four things have to stay lined up: what the project set out to do, what its
users asked for, what it was specified to do, and what it actually does. Each
check compares one of them with the next, in **both directions**:

| Check | Compares | When it is due |
|---|---|---|
| Charter audit | the charter against the user stories | when the charter changes, and otherwise on the cycle set at adoption |
| Fulfilment audit | the stories against the capabilities | when the stories or the user-facing capabilities have changed |
| Compliance audit | the capabilities against the code | at the close of a specification edition |
| Acceptance test | the stories against the running system | before work reaches the people the stories name |

When more than one is due, run them in that order, so that anything found out
of line early is fixed before effort goes into checking things that may change
as a result.

## Rules all audits share

- **Both directions, always.** Work down from what was wanted to what was
  built, then back up from what was built to what was wanted, and bring the two
  into one list of findings. Below, these two directions are called
  **top-down** and **bottom-up**. Going one way only hides half the problem:
  down alone misses work nobody asked for, up alone misses what was asked for
  and never done. Anything left out of either sweep is listed with the reason —
  leaving it out silently reads as having checked it.
- **Every finding is settled one of three ways.** Change the higher document,
  change the lower one, or accept the difference and record why. The exception
  is an **orphan** — work that serves nothing anyone asked for. Whether that is
  scope creep, or something someone wanted and never wrote down, is the
  human's call, never the auditor's.
- **Neither side is assumed correct.** The upper document is one side of the
  comparison, not the reference; an audit can find that the charter or a
  specification, not the work, is what drifted.
- **Structure before content.** Start with a quick pass comparing each
  document against the template it was made from. That separates "the shape of
  this document has drifted" from "what it says is wrong", before the slower
  reading starts. It is also where a document or code file that
  has grown too large to read whole is picked up, and recorded as a finding
  like any other.
- **Repeatable.** Write down the procedure — what was read, in what order, and
  what was asked of each — and keep it with the audit. Two runs over an
  unchanged project should reach the same findings; without a procedure they
  will not, and nobody can tell whether the project improved or the auditor's
  mood did.
- **Audits read; only the acceptance test runs anything.** An audit that starts
  running code, or an acceptance test that starts reading specifications to
  decide what should happen, is doing the other job. Stop and switch.
- **Fresh eyes.** A full audit starts from scratch rather than editing its
  predecessor. Who provides the independent eyes — a separate agent, a session
  that has not carried the work's context, a different person — is chosen at
  adoption and recorded there. Arranging nothing is not one of the choices.

## Per-activity specifics

- **Charter audit.** Top-down: for each part of the charter, are the stories
  pulling toward it — covered, partial, missing, or contradicted?
  This is coverage and direction, not item matching: the charter sets the
  destination, not a list. Bottom-up: for each story, the audit works out
  which part of the charter it serves — the link is made here, by the audit,
  and is never carried in the story. A story that fits nowhere is an orphan.
- **Fulfilment audit.** Top-down: every story is cited by at least one
  user-facing capability, the recorded roles match the story's role, and the
  citing capabilities together cover the story's description of what the person
  does and sees, and its acceptance criteria — classify covered, partial,
  missing, or misaligned. Bottom-up: sweep user-facing capabilities only; each
  cites real, in-scope stories with matching roles. A capability citing no real
  story is an orphan (scope creep, or a story that should exist but was never
  written); a non-user-facing capability citing stories is mismarked.
- **Compliance audit.** Top-down: every in-scope capability has an
  implementation honouring its contract, linked back to its identifier.
  Bottom-up: enumerate **everything** under version control in scope —
  source, tests, configuration, pipelines, infrastructure, assets, docs —
  and find each one's covering capability. Includes a check of the capability
  dependency graph; an invalid graph fails the audit. The evidence it reads:
  capability links, mapping tables, code excerpts, and records the project's
  automated build-and-test system has already produced.

## Acceptance testing

The acceptance test exercises each user story in the story's named role,
through the interface as it stands in the environment chosen for this at
adoption — the one judged close enough to production for a pass to mean
something (see `zoe-sdlc-adopt`) — using only the access and knowledge that
role would really have. Reading the specifications, using a developer tool, or
going in by a back way that role has no access to makes the result worthless:
it no longer shows whether a real person could do this. Every attempt produces
evidence an independent reader could judge — recordings, transcripts, captures,
or witnessed sign-off — and is recorded as pass, partial, fail, or blocked.

This does not replace the other three checks, or the automated tests. Audits
that pass while acceptance fails mean the documents agree with each other and
the software still does not work. The other way round means something has gone
wrong that has not reached anyone yet. Both need acting on.
