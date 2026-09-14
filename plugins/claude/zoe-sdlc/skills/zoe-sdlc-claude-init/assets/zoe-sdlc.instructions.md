> SDLC Base file — read-only to adopters. Do not edit. Specialise by adding
> dependent skills or your own project instructions alongside; improve it by
> sending feedback upstream.

# ZOE SDLC - Instructions

## Oversight

By default, human approval is needed at these points in this process:

- a new or changed user story or specification, before implementation starts;
- skipping a step in the order every change follows (`zoe-sdlc-sequencing`);
- a proposed departure from the architecture a specification sets out;
- adopting an external component — something the project uses but does not build
  itself (`zoe-sdlc-components`);
- adding a task to a batch of work already under way (`zoe-sdlc-develop`);
- deleting or weakening a test;
- deciding what a piece of work that serves no recorded intent actually means,
  when an audit finds one.

An adopter can give the AI more autonomy than this, or less. The points a
project keeps go into its charter's hard rules, which every agent doing the work
is given (`zoe-sdlc-adopt`). Where a skill asks for one of these approvals, it
asks only while the project keeps that point.

## Style

- Everything a project produces under this process is written plainly, at the
  level a business analyst would be comfortable reading and writing. Use a
  technical term only where the subject genuinely needs one.
  This holds just as much for files only an AI will ever
  read: the words in them shape the words it writes back to people.
- Professional tone; no emojis in project documents.
