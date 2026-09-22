---
name: zoe-sdlc-stories
kind: action
description: Write and maintain user stories. For capturing behaviour from the point of view of whoever wants or uses it.
version: 3
---

> SDLC Base file — read-only to adopters. Do not edit. Specialise by adding
> dependent skills; improve it by sending feedback upstream.

Stories come first. A capability names the story it serves, and an acceptance
test works through it.

Required Reading: `zoe-sdlc-templates` (a story is made from a template);
`zoe-sdlc-components` (how a capability names the story it serves).

Reads: the charter, which stories must pull toward; the stories already written
and the roles they name; the project's story template.

Produces: stories wherever the project keeps them, each with an identifier, a
named role, the story itself, a description of what the person does and sees,
its acceptance criteria, and a status. They are all listed in a single index
that also lists the project's roles.

Every story obeys:

- **One person, one goal.** Two of either means two stories.
- **Name a real role**, never "user" or "system". "Authenticated
  administrator", "third-party API consumer" — someone you could picture. The
  role is defined in the index and matched exactly in the story.
- **Say what they want, not how it works.** Naming a button, an endpoint or an
  algorithm has crossed into how it will be built. That belongs in the tasks
  that deliver the story.
- **The benefit can be proved or disproved.** You must be able to tell, through
  the same interface the story describes, whether the person got what they
  wanted.
- **Describe the interaction before writing criteria.** First how the person
  starts it and what they see back; then criteria in those same terms, never in
  terms of what happens inside. Each criterion takes the form: the starting
  situation, the action taken, the expected result. At least two per story, and
  at least one covering a case that fails or sits at a limit.
- **A story is not a work item.** No implementation notes, no test results, no
  audit findings. The only thing that changes on it is its status; the work
  happens in tasks that point at the story.
- **The project names the statuses; one meaning is fixed.** What they are
  called, and how many there are, is the project's own business. One of them
  must mean *finished, and ready to build from*. Until a story reaches it,
  nothing is built against it, and the check that compares stories with what
  was built leaves it out.
- **A story knows nothing about the solution.** No capability identifiers, no
  component references, nothing pointing downstream at all.
- **Write it in the person's own language.** The person in the role named may
  test against this story themselves, so they must be able to read and
  understand it straight away.
