#!/usr/bin/env python3
"""Copy a built plugin into this marketplace and update its catalogue entry.

Usage:
    scripts/update-plugin.py <plugin.zip>
    scripts/update-plugin.py <plugin-directory>
    scripts/update-plugin.py <plugin.zip> --surface claude

Steps:
    1. Unpack the plugin into plugins/<surface>/<plugin-name>/, replacing whatever
       was there. --surface defaults to "claude".
    2. Copy name, version, description and author from the plugin's own
       .claude-plugin/plugin.json into its entry in .claude-plugin/marketplace.json,
       adding the entry if the plugin is not listed yet.
    3. Run scripts/validate.py.

Leaves source, category, tags and strict alone: those belong to the catalogue, not to
the plugin. Re-running on an unchanged plugin makes no change.

Exit status: 0 if validate.py passes, 1 otherwise.
"""
import argparse
import json
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOGUE = ROOT / ".claude-plugin" / "marketplace.json"
# Copied from the plugin's manifest into its catalogue entry, every time.
TRACKED = ("version", "description", "author")


def staged_plugin(src: Path, tmp: Path) -> Path:
    """Return the plugin root, unpacking a zip if needed. Tolerates one wrapper dir."""
    if src.is_file() and zipfile.is_zipfile(src):
        zipfile.ZipFile(src).extractall(tmp)
        root = tmp
    elif src.is_dir():
        root = src
    else:
        sys.exit(f"not a plugin zip or directory: {src}")

    if not (root / ".claude-plugin" / "plugin.json").is_file():
        wrapped = [d for d in root.iterdir() if d.is_dir()]
        if len(wrapped) == 1 and (wrapped[0] / ".claude-plugin" / "plugin.json").is_file():
            return wrapped[0]
        sys.exit(f"no .claude-plugin/plugin.json at {root} or in a single wrapper folder")
    return root


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("plugin", type=Path, help="built plugin: a .zip or a directory")
    ap.add_argument("--surface", default="claude", help="subdirectory of plugins/ (default: claude)")
    args = ap.parse_args()

    with tempfile.TemporaryDirectory() as td:
        src = staged_plugin(args.plugin.resolve(), Path(td))
        manifest = json.loads((src / ".claude-plugin" / "plugin.json").read_text())
        name = manifest.get("name")
        if not name:
            sys.exit("the plugin manifest has no name")

        dest = ROOT / "plugins" / args.surface / name
        if dest.exists():
            shutil.rmtree(dest)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(src, dest)
        files = sum(1 for p in dest.rglob("*") if p.is_file())
        print(f"  plugin   {name}: {files} files -> {dest.relative_to(ROOT)}")

    cat = json.loads(CATALOGUE.read_text())
    entries = cat.setdefault("plugins", [])
    entry = next((e for e in entries if e.get("name") == name), None)
    if entry is None:
        entry = {"name": name, "source": f"./plugins/{args.surface}/{name}"}
        entries.append(entry)
        print(f"  entry    added, source {entry['source']}")
    else:
        print(f"  entry    found, source {entry.get('source')}")

    for field in TRACKED:
        if field in manifest:
            was = entry.get(field)
            entry[field] = manifest[field]
            if was != manifest[field]:
                print(f"  synced   {field}: {was!r} -> {manifest[field]!r}")
        elif field in entry:
            del entry[field]
            print(f"  removed  {field}: absent from the plugin manifest")

    # Keep the entry's fields in a stable order so diffs stay readable.
    order = ["name", "description", "version", "author", "source", "category", "tags", "strict"]
    entries[entries.index(entry)] = {k: entry[k] for k in order if k in entry} | {
        k: v for k, v in entry.items() if k not in order}
    CATALOGUE.write_text(json.dumps(cat, indent=2, ensure_ascii=False) + "\n")

    print()
    return subprocess.run([str(ROOT / "scripts" / "validate.py")]).returncode


if __name__ == "__main__":
    sys.exit(main())
