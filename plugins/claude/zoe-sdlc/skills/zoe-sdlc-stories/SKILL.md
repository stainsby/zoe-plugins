---
name: zoe-sdlc-stories
kind: action
description: Write and maintain user stories. For capturing behaviour from the point of view of whoever wants or uses it.
version: 2
---

> SDLC Base file — read-only to adopters. Do not edit. Specialise by adding
> dependent skills; improve it by sending feedback upstream.

Stories come first. A capability names the story it serves, and an acceptance
test works through it.

Required Reading: `zoe-sdlc-templates` (a story is made from a template);
`zoe-sdlc-components` (how a capability names the story it serves — the link a
story never holds itself).

Reads: the charter, which stories must pull toward; the stories already written
and the roles they name; the project's story template.

Produces: stories wherever the project keeps them, each with an identifier, a
named role, the story itself, a description of what the person does and sees,
its acceptance criteria, and a status. They are all listed in a single index
that also lists the project's roles.

Every story obeys:

- **One person, one goal.** Two of either means two stories. Trying to cover
  both at once produces criteria you cannot test.
- **Name a real role**, never "user" or "system". "Authenticated
  administrator", "third-party API consumer" — someone you could picture. The
  role is defined in the index and matched exactly in the story.
- **Say what they want, not how it works.** Naming a button, an endpoint or an
  algorithm has crossed into how it will be built. That belongs in the tasks
  that deliver the story.
- **The benefit can be proved or disproved.** You must be able to tell, through
  the same interface the story describes, whether the person got what they
  wanted. If you cannot, there is nothing to accept.
- **Describe the interaction before writing criteria.** First how the person
  starts it and what they see back; then criteria in those same terms, never in
  terms of what happens inside. Each criterion takes the form: the starting
  situation, the action taken, the expected result. At least two per story, and
  at least one covering a case that fails or sits at a limit. A story whose
  criteria only cover things going well is incomplete.
- **A story is not a work item.** No implementation notes, no test results, no
  audit findings. The only thing that changes on it is its status. The work
  happens in tasks that point at the story; the story stays the record of what
  was wanted.
- **The project names the statuses; one meaning is fixed.** What they are
  called, and how many there are, is the project's own business. One of them
  must mean *finished, and ready to build from*. Until a story reaches it,
  nothing is built against it, and the check that compares stories with what
  was built leaves it out — otherwise a half-written story looks the same as
  one the system was never meant to cover.
- **A story knows nothing about the solution.** No capability identifiers, no
  component references, nothing pointing downstream at all — which is what lets
  a story survive being rebuilt underneath.
- **Write it in the person's own language.** The wording is tailored to the
  role named — they may end up testing against this story themselves, so they
  have to be able to read it and understand it straight away. If they could
  not, rewrite it.
