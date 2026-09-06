#!/usr/bin/env python3
"""Check this marketplace: the catalogue file, and every plugin it lists.

Usage:
    scripts/validate.py

Checks that the catalogue parses, has the required fields, and lists no duplicate
plugin names. Then for each entry: the source path stays inside the repository, the
plugin directory exists, its .claude-plugin/plugin.json is present and parses, and the
entry's name, version, description and author match it. Finally runs
`claude plugin validate --strict` if the claude CLI is installed, and says so if it is
not, rather than passing quietly.

Prints one PASS or FAIL line per check, with what it compared.

Exit status: 0 if every check passes, 1 otherwise.
"""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOGUE = ROOT / ".claude-plugin" / "marketplace.json"
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

failures = []


def check(name, ok, detail):
    print(f"  {'PASS' if ok else 'FAIL'}  {name}: {detail}")
    if not ok:
        failures.append(name)


def main():
    print(f"marketplace: {ROOT}")

    if not CATALOGUE.exists():
        print(f"  FAIL  catalogue exists: {CATALOGUE} not found")
        return 1
    try:
        cat = json.loads(CATALOGUE.read_text())
    except json.JSONDecodeError as e:
        print(f"  FAIL  catalogue parses: {e}")
        return 1
    check("catalogue parses", True, f"{CATALOGUE.relative_to(ROOT)}")

    # --- the catalogue itself -------------------------------------------------
    missing = [f for f in ("name", "owner", "plugins") if f not in cat]
    check("required fields present", not missing,
          "name, owner, plugins" if not missing else f"missing {missing}")

    check("marketplace name is kebab-case", bool(KEBAB.match(cat.get("name", ""))),
          repr(cat.get("name")))

    entries = cat.get("plugins", [])
    check("catalogue lists at least one plugin", len(entries) > 0, f"{len(entries)} listed")

    names = [e.get("name") for e in entries]
    dupes = {n for n in names if names.count(n) > 1}
    check("no duplicate plugin names", not dupes,
          f"{len(names)} names, {len(set(names))} distinct"
          + (f", duplicated: {sorted(dupes)}" if dupes else ""))

    # --- each entry, against the plugin it points at --------------------------
    checked = 0
    for e in entries:
        name = e.get("name", "<unnamed>")
        src = e.get("source")

        if not KEBAB.match(name or ""):
            check(f"[{name}] name is kebab-case", False,
                  "claude.ai marketplace sync requires kebab-case")

        if not isinstance(src, str):
            check(f"[{name}] source is a path in this repository", False,
                  f"got {type(src).__name__}; this marketplace hosts its plugins itself")
            continue
        if not src.startswith("./"):
            check(f"[{name}] source starts with ./", False, repr(src))
            continue

        plugin_dir = (ROOT / src[2:]).resolve()
        inside = ROOT in plugin_dir.parents or plugin_dir == ROOT
        check(f"[{name}] source stays inside the repository", inside, src)
        if not inside:
            continue

        check(f"[{name}] plugin directory exists", plugin_dir.is_dir(),
              str(plugin_dir.relative_to(ROOT)) if plugin_dir.exists() else f"{src} not found")
        if not plugin_dir.is_dir():
            continue

        manifest = plugin_dir / ".claude-plugin" / "plugin.json"
        check(f"[{name}] plugin.json at the plugin root", manifest.is_file(),
              str(manifest.relative_to(ROOT)) if manifest.exists() else "not found")
        if not manifest.is_file():
            continue

        try:
            pj = json.loads(manifest.read_text())
        except json.JSONDecodeError as err:
            check(f"[{name}] plugin.json parses", False, str(err))
            continue

        check(f"[{name}] entry name matches plugin.json", pj.get("name") == name,
              f"entry {name!r} vs manifest {pj.get('name')!r}")

        # A version in the entry overrides the manifest's, with no error, so a stale
        # one leaves adopters on a cached copy.
        if "version" in e:
            check(f"[{name}] entry version matches plugin.json",
                  e["version"] == pj.get("version"),
                  f"entry {e['version']!r} vs manifest {pj.get('version')!r}")

        # Shown while browsing the catalogue; the manifest's copy is shown after install.
        if "description" in e:
            check(f"[{name}] entry description matches plugin.json",
                  e["description"] == pj.get("description"),
                  "identical" if e["description"] == pj.get("description")
                  else f"entry {len(e['description'])} chars vs manifest "
                       f"{len(pj.get('description') or '')} chars")
        if "author" in e:
            check(f"[{name}] entry author matches plugin.json",
                  e["author"] == pj.get("author"),
                  "identical" if e["author"] == pj.get("author")
                  else f"entry {e['author']} vs manifest {pj.get('author')}")

        # `claude plugin validate` warns if these appear in a plugin manifest:
        # "belongs in the marketplace entry (marketplace.json), not plugin.json".
        misplaced = [f for f in ("category", "tags", "source", "strict") if f in pj]
        check(f"[{name}] plugin.json carries no catalogue-only fields", not misplaced,
              "none" if not misplaced else f"{misplaced} belong in the entry and are ignored here")

        # Documented rejection for organisation distribution.
        check(f"[{name}] no top-level bin/", not (plugin_dir / "bin").is_dir(),
              "absent" if not (plugin_dir / "bin").is_dir() else "present — rejected on install")

        files = sum(1 for p in plugin_dir.rglob("*") if p.is_file())
        check(f"[{name}] plugin has files", files > 0, f"{files} files")
        checked += 1

    check("every listed plugin was checked", checked == len(entries),
          f"{checked} of {len(entries)}")

    # --- the vendor's own validator, if it is here ----------------------------
    if shutil.which("claude"):
        r = subprocess.run(["claude", "plugin", "validate", "--strict", str(ROOT)],
                           capture_output=True, text=True)
        check("claude plugin validate --strict", r.returncode == 0,
              (r.stdout + r.stderr).strip().splitlines()[-1] if (r.stdout + r.stderr).strip() else "no output")
    else:
        print("  SKIP  claude plugin validate --strict: claude is not installed here")
        print("        NOT VALIDATED by the vendor's own checker — do not read this run as a full pass")

    print()
    if failures:
        print(f"FAIL — {len(failures)} check(s) failed: {', '.join(failures)}")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
