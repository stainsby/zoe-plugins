---
name: zoe-sdlc-components
kind: understanding
description: How a software project is broken into components, what a capability is, and how both are named — so that parts can be worked on separately, and every document can refer to the same units. For specifying, breaking up or restructuring a system, and for any task that implements part of one.
version: 6
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
  that edge can carry, not a separate branch of the hierarchy. It says where a
  component sits, not who it is for: who a capability serves is recorded on the
  capability itself (below), and a component well inside the system can own
  capabilities that serve real people.

## Sizing

A **leaf component** (one with no sub-components) is sized so the human or agent
doing the work can fully specify, implement and test it in one sitting — one
stretch of work with the whole of it in mind, within what an AI assistant can
hold in its context and a human's attention span. A sitting is not the
kernel's session, which can run many tasks. A component too large for one
sitting is broken into sub-components; an oversized leaf is a defect.

How much fits in a sitting differs by project, person and assistant, so each
project records its size limit at adoption (`zoe-sdlc-adopt`), in terms two
people could agree on from the outside. Until it is recorded, this rule is
unchecked, not met. A project that cannot yet set a limit records that, and
why, instead.

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
  held, and the role recorded must match the role in the story it names.
- **internal** — consumed only by other capabilities.
- **composition** — it bundles other capabilities (a release, for example) and
  is neither user-facing nor independently implemented.

## The capability dependency graph

How the whole system connects together is held as a single **dependency
graph**. It has two kinds of entry: components point to the capabilities they
provide, and capabilities point to the capabilities they consume from other
components. Each specification declares what its component points at — for each
capability it owns, which other components' capabilities it depends on — in a
form **a program can read**, so the whole graph can be assembled and checked
automatically. The concrete format (a data block in each
specification, a tracker's link fields, a manifest) is the project's choice;
that a program can read it is not.

The graph is valid only when:

- it has **no loops** — no capability depends, however indirectly, on itself;
- every consumed capability is **provided by some component** — no dangling
  references;
- no component is **disconnected** — left with nothing pointing at it and
  nothing it points at, without a recorded reason;
- no capability depends on another capability of its own component — that is
  the component's internal structure, not a dependency between components.

Validity is checked mechanically whenever the declared connections change, and
always before implementation work relies on it. An invalid graph blocks the work
that depends on the affected region, exactly as a failing test blocks
completion.

Writing that check is a step of `zoe-sdlc-adopt`; an example to start from is
`assets/validate_capability_graph.py`.

## Linking code to capabilities

Every non-private code unit — function, class, module, endpoint, package —
declares the capabilities it fully or partly **implements** and the
capabilities it **uses** to function. The declaration mechanism is whatever
the language and toolchain make durable and searchable — doc comments,
annotations, metadata files — decided at adoption. Either way, the link is
written where the code lives, uses the capability identifiers from the
specifications, and is readable by a program.

Code with no capability link is **dangling**: nothing in the specifications
explains why it exists. Dangling code is a compliance finding — it gets
linked, or it gets removed; it is never quietly kept. The same check runs the
other way: a capability whose specification says it is implemented, but which
no code claims, is an unimplemented claim. Writing that check, in whatever form
the chosen way of declaring links allows, is a step of `zoe-sdlc-adopt`.

## Environments

Which environments a project has — a developer's machine, a test system,
production, whatever an agent runs inside — is settled at adoption
(`zoe-sdlc-adopt`). Each component's specification says which of them it has to
work in and what each requires of it. Where an external component behaves
differently from one environment to another, the tests are designed for that
difference.
