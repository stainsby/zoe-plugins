---
name: zoe-sdlc-components
kind: understanding
description: How a software project is broken into components, what a capability is, and how both are named — so that parts can be worked on separately, and every document can refer to the same units. For specifying, breaking up or restructuring a system, and for any task that implements part of one.
version: 5
---

> SDLC Base file — read-only to adopters. Do not edit. Specialise by adding
> dependent skills; improve it by sending feedback upstream.

## Components

A component is a structural unit of the system, organised by **containment**:
components may have sub-components, and the project itself is always the
top-level component that binds all others together. Three classes matter:

- **Internal components** — defined, owned, and implemented within the project.
- **External components** — libraries, services, platforms, and environments the
  project uses but does not implement. They are modelled as components too:
  what the project consumes from them is documented, in the project's own
  terms, from the internal components that depend on them — never the other
  way around. Before adopting one, check its current stable version by
  searching; never rely on what you remember.
- **User-facing components** — those sitting at the edge of the system, where
  something outside it arrives: a person at a screen, another system calling
  in, an operator at a command line, an agent. This is a label any component at
  that edge can carry; it is not a separate branch of the hierarchy. It says
  where a component sits, not who it is for. A component well inside the system
  can still own capabilities that serve real people — in a layered design that
  is the normal case — and there is no contradiction in that, because who a
  capability serves is recorded on the capability itself (below).

## Sizing

A **leaf component** (one with no sub-components) is sized so it can be fully
specified, implemented, and tested within a single working session of the human
or agent doing the work — this is what keeps each unit within what an AI
assistant can hold in its context at once, as well as within a human's
attention span. A component too large for that should be broken into
sub-components. An oversized leaf should be treated as a defect.

What counts as one session differs by project, by person and by assistant.
Each project settles it at adoption and records it (see `zoe-sdlc-adopt`),
in a form two people could agree on from the outside.

## Identity

Every component and every capability carries a **stable, unique, hierarchical
identifier**, so that specifications, tasks, tests, and code can reference them
unambiguously and traceability can be checked mechanically. The identifier
convention — prefixes, separators, casing — is chosen once at adoption and used
consistently. What must hold either way is that identifiers are stable (renames
are deliberate, tracked events), hierarchical (a child's identifier locates it
under its parent), and distinguish internal from external components. A
dot-delimited upper-case scheme such as `CMP.PARENT.CHILD` with an `X.` prefix
for external components is a workable default, not a requirement.

## Capabilities

A **capability** is a specific behaviour or service a component provides to its
users — humans, agents, or other components. Capabilities are how the parts of a
system connect: a component provides capabilities, and works by using the
capabilities of other components. Each capability is owned by exactly one
component and scoped by it; a component with sub-components documents only the
capabilities it directly owns — a child's capabilities live with the child.

Every capability states a contract: what it takes in, what it gives back, what
must be true before it is used and after it has run, and how it fails. The
contract is what tests are written against, so it has to be complete before the
code exists. A capability nobody can state a contract for is not yet understood
well enough to build.

Each capability also declares who it serves, in exactly one of three ways:

- **user-facing** — it fulfils one or more user stories, named here. This is
  the only place the link between a story and the thing that serves it is
  held, and the role recorded must match the role in the story it names. It
  says whose intent the capability serves; it does not make its component a
  user-facing component.
- **internal** — consumed only by other capabilities.
- **composition** — it bundles other capabilities (a release, for example) and
  is neither user-facing nor independently implemented.

## The capability dependency graph

How the whole system connects together is held as a single **dependency
graph** — a graph here being nothing more than a map of what points at what. It
has two kinds of entry: components point to the capabilities they provide, and
capabilities point to the capabilities they consume from other components. Each
specification declares what its component points at — for each capability it
owns, which other components' capabilities it depends on — in a form **a program
can read**, so the whole graph can be assembled and checked automatically rather
than by someone reading it. The concrete format (a data block in each
specification, a tracker's link fields, a manifest) is the project's choice;
that a program can read it is not.

The graph is valid only when:

- it has **no loops** — following what a capability depends on, and what
  that depends on in turn, never leads back to where you started;
- every consumed capability is **provided by some component** — no dangling
  references;
- no component is **disconnected** — left with nothing pointing at it and
  nothing it points at, without a recorded reason;
- no capability depends on another capability of its own component — a
  component's internal structure is not a dependency between components, and
  does not belong in this graph.

Validity is checked mechanically whenever the declared connections change, and
always before implementation work relies on it. An invalid graph blocks the work
that depends on the affected region, exactly as a failing test blocks
completion.

The usual way to hold this is a script, run wherever the project already runs
its tests, that reads the declared connections and reports the failures above. An
example that may be used as a starting point is provided here:
`assets/validate_capability_graph.py`. Writing the check is a step of
`zoe-sdlc-adopt`.

## Linking code to capabilities

Every non-private code unit — function, class, module, endpoint, package —
declares the capabilities it fully or partly **implements** and the
capabilities it **uses** to function. The declaration mechanism is whatever
the language and toolchain make durable and searchable — doc comments,
annotations, metadata files — decided at adoption. However it is done, the
link should be written where the code lives, use the capability identifiers
from the specifications, and be readable by a program.

Code with no capability link is **dangling**: nothing in the specifications
explains why it exists. Dangling code is a compliance finding — it gets
linked, or it gets removed; it is never quietly kept. The same check runs the
other way: a capability whose specification says it is implemented, but which
no code claims, is an unimplemented claim. Checking both directions is what
lets a program do this work, instead of somebody reading through the code to
work out what belongs to what. Writing that check is a step of
`zoe-sdlc-adopt`. Its form follows whatever way of declaring the links was
chosen there, so no example can be given here.

## Environments

Software is typically built, tested and run in different places — a developer's
PC, a test system, production, whatever an agent runs inside. Which of these a
project actually has, which one acceptance testing runs against, and what makes
a test environment close enough to production to trust its results are all
settled at adoption (`zoe-sdlc-adopt`).

Each environment puts its own demands on a component, and its specification
says which environments it has to work in and what each one requires of it.
Where an external component behaves differently from one to another, that
difference is taken into account when the tests are designed.
