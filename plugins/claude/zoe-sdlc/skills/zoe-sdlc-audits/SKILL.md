---
name: zoe-sdlc-audits
kind: understanding
description: Perform charter, fulfilment and compliance audits, and acceptance testing. For planning, running or judging any of them, and for working out which one you need.
version: 5
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

Each check sweeps the whole project, and runs once when due — not once per
release or other piece of work. Its record names the pieces of work it clears
and those it does not, with the finding that holds each open. Clearing a piece
of work means only that this check's comparison held for it.

When more than one is due, run them in that order where a finding from an
earlier check can be fixed before the next runs, so effort is not spent
checking what may change as a result; where it cannot, they may run together.

## Rules all audits share

- **Both directions, always.** Work down from what was wanted to what was
  built, then back up from what was built to what was wanted, and bring the two
  into one list of findings. Below, these two directions are called
  **top-down** and **bottom-up**. Anything left out of either sweep is listed
  with the reason.
- **Every finding is settled one of three ways.** Change the higher document,
  change the lower one, or accept the difference and record why. The exception
  is an **orphan** — work that serves nothing anyone asked for. Whether that is
  scope creep, or something someone wanted and never wrote down, is the
  human's call, never the auditor's.
- **Neither side is assumed correct.** An audit can find that the charter or a
  specification, not the work, is what drifted.
- **Structure before content.** Start with a quick pass comparing each
  document against the template it was made from. It is also where a document
  or code file that has grown too large to read whole, or a leaf component past
  the project's size limit, is picked up, and recorded as a finding like any
  other.
- **Repeatable.** Write down the procedure — what was read, in what order, and
  what was asked of each — and keep it with the audit, so two runs over an
  unchanged project reach the same findings.
- **Audits read; only the acceptance test runs anything.** An audit that starts
  running code, or an acceptance test that starts reading specifications to
  decide what should happen, is doing the other job. Stop and switch.
- **Fresh eyes.** A full audit starts from scratch rather than editing its
  predecessor, and is run by independent eyes chosen at adoption
  (`zoe-sdlc-adopt`).

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
something (`zoe-sdlc-adopt`) — using only the access and knowledge that role would
really have. Reading the specifications, using a developer tool, or going in by
a back way that role has no access to makes the result worthless. Every attempt
produces evidence an independent reader could judge — recordings, transcripts,
captures, or witnessed sign-off — and is recorded as pass, partial, fail, or
blocked.

This does not replace the other three checks, or the automated tests. Audits
passing while acceptance fails, or the other way round, both need acting on.
