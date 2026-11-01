> Copy this into your own index and fill it in at setup. The AI keeps it current afterwards.
> Source template: zoe-setup/assets/index.template.md

# Index

Where everything is, and the settings you run by.

Three rules for this file. Write down where things are and what they are set to; how they
work belongs in a skill. Write only what is true now; what changed belongs in the log. Where
you know you will need somewhere to keep something but have not set it up yet, keep the line
and write "not yet created".

## Core

- enterprise name: {a name for this enterprise}
- where the charter is: {the file or place holding it}
- where the enterprise instructions are: {the file}
- how to reach a director: {how you contact them, how they answer, and how each director is
  identified there (for example, the host's sign-in)}
- directors: {who they are, or how someone becomes one (for example, anyone with access to a
  named channel); where several, the arrangement if not "any one can do anything a director
  can do"}
- quote directors: {"yes" if records quote a director's words exactly, "no" if they only say
  what was decided or asked. "no" unless a director chooses otherwise.}
- where feedback arrives: {where messages from people using your work come in. Write "none"
  if there is nowhere yet.}
- schedule: {what "due" and "this cycle" mean here, what triggers an assessment and what
  triggers a redesign (they need not be the same), who may open a management session (with one
  director, them), and how often you run feedback and your checks. Checking for a new kernel
  has its own line below.}
- sessions: {what counts as one conversation: a sitting, a chat thread or a meeting. What
  else ends a session, such as a quiet period or a maximum length. Who is warned first, if
  anyone. Whether a session ended that way counts as closed without a director's word. In a
  director's own sittings: "a sitting; ends on their word".}
- date and time: {the timezone to use — normally the director's — and the format, such as
  2026-06-14T07:38:29+08:00}
- kernel version: {which version of the ZOE kernel you run on}
- where the kernel came from: {the ZOE project, or the enterprise above you. If you build
  your own kernel, say so. If you started from a ready-made enterprise design, you have two
  sources — list both, each with its version.}
- where the kernel's changelog is: {the list of what changed in each kernel version}
- how often to check for a newer kernel: {see `zoe-upgrade`}
- host packaging: {where the per-host files live — the stubs, README and settings that let a
  particular AI platform run this. They sit beside the kernel, never inside it.}
- which model does which job: {the real model for each kind your skills
  ask for; see `## Models` in the instructions}
- agents this enterprise runs: {which ones, and where their definitions live}
- running unattended: {whether this host can run this enterprise on a schedule with nobody
  present, and how it is started. Write "no" if it cannot.}
- concurrency limit: {how many workers may run at once, and how long each may run}
- known weaknesses: {anything about this setup that will keep looking like a fault but is
  not — for example a host that cannot run separate agents. Recorded here so it is not
  reported afresh every session.}
- where state is kept: {what is currently true}
- where the log is kept: {what has happened}
- where tasks are kept: {see `zoe-tasks` for what the store must provide}
- where plans are kept: {redesign plans and the approvals they need}
- where reports are kept: {assessments}
- where audit findings are kept:
- where your own skills are kept: {keep them separate from the ZOE skills}
- enterprises below you: {for each one, where its charter is and how it reports to you}
- tools: {how you reach the outside world}

## Other

{anything else this enterprise needs a home for}
