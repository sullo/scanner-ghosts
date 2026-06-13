#!/usr/bin/env python3
"""Archive tooling: generate index tables from entry frontmatter, and validate.

Single source of truth is each tool's meta.yml sidecar
(tools/<category>/<tool>/meta.yml). Everything else — the root README entry
table, the per-category index, the per-entry Metadata table, and the source
checksums — is generated from it between BEGIN/END markers in the READMEs.

Zero dependencies: runs on a stock python3, so CI needs nothing installed.

    python3 scripts/archive.py generate   # rewrite all generated blocks
    python3 scripts/archive.py check      # validate; non-zero exit on problems

`check` is what CI runs. It fails if metadata is invalid, an internal link is
broken, a recorded checksum is stale, or any generated block is out of date
(i.e. someone edited content by hand instead of running `generate`).
"""

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"

# Controlled vocabulary — mirrors docs/taxonomy.md. Keep in sync.
TYPES = {
    "CGI Scanner", "Web Scanner", "Vulnerability Scanner", "Port Scanner",
    "Fingerprinter", "Proxy / Interceptor", "Discovery", "Crawler",
    "Exploit Framework", "Fuzzer",
}
MODELS = {"Open Source", "Freeware", "Commercial", "Unknown"}
ACTIVE = {"Yes", "No", "Abandoned", "Unknown"}
SOURCE_STATUS = {"Available", "Partial", "Not Available", "Unknown"}
ENTRY_STATUS = {"Stub", "Basic", "Full", "Archived"}

REQUIRED = ["name", "author", "year", "primary_type", "model",
            "active", "source", "status"]

# Display name per category directory.
CATEGORY_TITLES = {"web": "Web Scanners"}

ARCHIVE_SUFFIXES = (".tar.gz", ".tar.bz2", ".tgz", ".gz", ".bz2", ".zip")
# Recovered source can also be a single unpacked file (e.g. cgiscan.c), not a
# tarball. Hash those too so they show up in the checksum table.
SOURCE_SUFFIXES = (".c", ".h", ".pl", ".pm", ".py", ".sh", ".cgi", ".php",
                   ".pas", ".cpp", ".asm", ".rb")


# --------------------------------------------------------------------------- #
# Minimal metadata parsing (a small, fixed subset of YAML)
# --------------------------------------------------------------------------- #
# Each entry's metadata lives in a sidecar meta.yml file (not in the README),
# so GitHub does not auto-render it as a second table above the generated one.
def load_meta(path):
    """Parse a meta.yml file into a dict. Supports `key: value` and `[a, b]`."""
    # Normalize CRLF so Windows / autocrlf checkouts parse identically.
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    meta = {}
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, _, val = line.partition(":")
        meta[key.strip()] = _coerce(val.strip())
    return meta


def _coerce(val):
    if val.startswith("[") and val.endswith("]"):
        inner = val[1:-1].strip()
        if not inner:
            return []
        return [_unquote(p.strip()) for p in inner.split(",")]
    return _unquote(val)


def _unquote(s):
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    return s


# --------------------------------------------------------------------------- #
# Discovery
# --------------------------------------------------------------------------- #
def discover_entries():
    """Tool entries live at tools/<category>/<tool>/ with a meta.yml + README.md."""
    entries = []
    for meta_file in sorted(TOOLS.glob("*/*/meta.yml")):
        entry_dir = meta_file.parent
        readme = entry_dir / "README.md"
        if not readme.exists():
            raise SystemExit(f"ERROR: {rel(meta_file)} has no sibling README.md")
        entries.append({
            "category": entry_dir.parent.name,
            "slug": entry_dir.name,
            "dir": entry_dir,
            "readme": readme,
            "meta_file": meta_file,
            "meta": load_meta(meta_file),
            "archives": find_archives(entry_dir / "src"),
        })
    # An entry README with no meta.yml would silently vanish from every table.
    for readme in sorted(TOOLS.glob("*/*/README.md")):
        if not (readme.parent / "meta.yml").exists():
            raise SystemExit(f"ERROR: {rel(readme)} has no meta.yml")
    return entries


def find_archives(src_dir):
    if not src_dir.is_dir() or src_dir.is_symlink():
        return []
    out = []
    for f in sorted(src_dir.rglob("*")):
        # Skip symlinks: never hash a file that points outside the entry's
        # own src/ tree (information leak), and avoid symlink-cycle traversal.
        if f.is_symlink():
            continue
        if f.is_file() and f.name.lower().endswith(
                ARCHIVE_SUFFIXES + SOURCE_SUFFIXES):
            out.append(f)
    return out


def rel(p):
    return str(Path(p).resolve().relative_to(ROOT))


def sort_key(entry):
    # Index tables are ordered alphabetically by tool name (case-insensitive).
    return str(entry["meta"].get("name", "")).lower()


def year_sort_key(entry):
    # Root table is ordered oldest-first by year, then alphabetically on ties.
    digits = re.sub(r"\D", "", str(entry["meta"].get("year", "")))
    return (int(digits) if digits else 0, sort_key(entry))


def name_cell(entry, link):
    """Tool name, linked to its page when that page exists, else plain text."""
    name = entry["meta"].get("name", "")
    if entry["readme"].exists():
        return f"[{name}]({link})"
    return name


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #
def render_metadata_block(meta):
    sec = meta.get("secondary_types", [])
    sec = ", ".join(sec) if isinstance(sec, list) else str(sec)
    rows = [
        ("Product Name", meta.get("name", "")),
        ("Owner / Author", meta.get("author", "")),
        ("Year Released", meta.get("released", meta.get("year", ""))),
        ("Primary Type", meta.get("primary_type", "")),
        ("Secondary Type(s)", sec),
        ("Model", meta.get("model", "")),
        ("Active", meta.get("active", "")),
    ]
    lines = ["| Field | Value |", "| --- | --- |"]
    lines += [f"| **{k}** | {v} |" for k, v in rows]
    return "\n".join(lines)


def render_checksums_block(archives, entry_dir):
    if not archives:
        return "_No source archives recorded._"
    lines = ["| Archive | SHA256 |", "| --- | --- |"]
    for a in archives:
        data = a.read_bytes()
        if data[:45].startswith(b"version https://git-lfs.github.com/spec"):
            raise SystemExit(
                f"ERROR: {rel(a)} is an unresolved Git LFS pointer — "
                f"run `git lfs pull` (CI: set lfs: true on checkout)")
        digest = hashlib.sha256(data).hexdigest()
        name = str(a.relative_to(entry_dir))
        lines.append(f"| `{name}` | `{digest}` |")
    return "\n".join(lines)


def render_root(entries):
    out = []
    by_cat = {}
    for e in entries:
        by_cat.setdefault(e["category"], []).append(e)
    for cat in sorted(by_cat):
        out.append(f"### {CATEGORY_TITLES.get(cat, cat.title() + ' Tools')}")
        out.append("")
        out.append("| Tool | Author | Year | Source Available |")
        out.append("| --- | --- | --- | --- |")
        for e in sorted(by_cat[cat], key=year_sort_key):
            m = e["meta"]
            link = f"tools/{e['category']}/{e['slug']}/README.md"
            out.append(f"| {name_cell(e, link)} | {m['author']} "
                       f"| {m['year']} | {m['source']} |")
        out.append("")
    return "\n".join(out).rstrip()


def render_index(category, entries):
    out = ["| Tool | Author | Year | Primary Type | Model | Source | Status |",
           "| --- | --- | --- | --- | --- | --- | --- |"]
    for e in sorted(entries, key=sort_key):
        m = e["meta"]
        link = f"{e['slug']}/README.md"
        out.append(f"| {name_cell(e, link)} | {m['author']} | {m['year']} "
                   f"| {m['primary_type']} | {m['model']} | {m['source']} "
                   f"| {m['active']} |")
    return "\n".join(out)


# --------------------------------------------------------------------------- #
# Block replacement
# --------------------------------------------------------------------------- #
def replace_block(text, tag, new_content):
    begin = f"<!-- BEGIN {tag} -->"
    end = f"<!-- END {tag} -->"
    pattern = re.compile(
        re.escape(begin) + r".*?" + re.escape(end), re.DOTALL)
    if not pattern.search(text):
        raise SystemExit(f"ERROR: missing block markers for {tag}")
    return pattern.sub(f"{begin}\n{new_content}\n{end}", text)


def build_targets(entries):
    """Return {path: new_text} for every file with generated blocks."""
    targets = {}

    for e in entries:
        text = e["readme"].read_text(encoding="utf-8")
        text = replace_block(text, "METADATA", render_metadata_block(e["meta"]))
        text = replace_block(
            text, "CHECKSUMS", render_checksums_block(e["archives"], e["dir"]))
        targets[e["readme"]] = text

    root_readme = ROOT / "README.md"
    targets[root_readme] = replace_block(
        root_readme.read_text(encoding="utf-8"), "ENTRYTABLE",
        render_root(entries))

    by_cat = {}
    for e in entries:
        by_cat.setdefault(e["category"], []).append(e)
    for cat, cat_entries in by_cat.items():
        index = TOOLS / cat / "README.md"
        if index.exists():
            targets[index] = replace_block(
                index.read_text(encoding="utf-8"), f"INDEX:{cat}",
                render_index(cat, cat_entries))
    return targets


# --------------------------------------------------------------------------- #
# Validation
# --------------------------------------------------------------------------- #
LINK_RE = re.compile(r"\]\(([^)]+)\)")


def validate(entries):
    problems = []

    for e in entries:
        m, where = e["meta"], rel(e["meta_file"])
        # Every required field must be present AND a scalar string. A YAML list
        # (e.g. `model: [x]`) coerces to a Python list, which is unhashable for
        # the `in SET` checks below — flag it here instead of crashing later.
        for key in REQUIRED:
            v = m.get(key)
            if not v:
                problems.append(f"{where}: missing required field '{key}'")
            elif not isinstance(v, str):
                problems.append(
                    f"{where}: field '{key}' must be a single value, not a list")
        # Vocabulary checks. Guard isinstance(str) so a non-string value can
        # never reach `in SET` (TypeError: unhashable type) — it was already
        # reported above. Empty/missing values were also reported above.
        for key, vocab in (("primary_type", TYPES), ("model", MODELS),
                           ("active", ACTIVE), ("source", SOURCE_STATUS),
                           ("status", ENTRY_STATUS)):
            v = m.get(key)
            if isinstance(v, str) and v and v not in vocab:
                problems.append(f"{where}: invalid {key} '{v}'")
        sec = m.get("secondary_types") or []
        if isinstance(sec, str):
            sec = [sec]
        for s in sec:
            if not isinstance(s, str) or s not in TYPES:
                problems.append(f"{where}: invalid secondary type '{s}'")

    # Internal relative links must resolve to a real file.
    for md in sorted(ROOT.glob("**/*.md")):
        if ".git" in md.parts:
            continue
        try:
            md_text = md.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            problems.append(f"{rel(md)}: not valid UTF-8")
            continue
        for target in LINK_RE.findall(md_text):
            link = target.split("#")[0].split("?")[0].strip()
            # Only verify internal links to Markdown docs. Skip external URLs,
            # GitHub shortcuts (../../issues/...), and directory placeholders.
            if not link.endswith(".md") or "://" in link:
                continue
            if not (md.parent / link).exists():
                problems.append(f"{rel(md)}: broken link -> {link}")

    return problems


# --------------------------------------------------------------------------- #
# Entrypoints
# --------------------------------------------------------------------------- #
def cmd_generate():
    entries = discover_entries()
    problems = validate(entries)
    if problems:
        print("Refusing to generate — fix metadata first:\n  "
              + "\n  ".join(problems))
        sys.exit(1)
    for path, text in build_targets(entries).items():
        if path.read_text(encoding="utf-8") != text:
            path.write_text(text, encoding="utf-8")
            print(f"updated {rel(path)}")
    print("generate: done")


def cmd_check():
    entries = discover_entries()
    problems = validate(entries)
    # Only render generated blocks once metadata is known-valid; build_targets
    # direct-indexes required fields and would crash on invalid input.
    if not problems:
        for path, text in build_targets(entries).items():
            if path.read_text(encoding="utf-8") != text:
                problems.append(f"{rel(path)}: generated content stale — "
                                f"run `python3 scripts/archive.py generate`")
    if problems:
        print("CHECK FAILED:\n  " + "\n  ".join(problems))
        return 1
    print(f"check: OK ({len(entries)} entries)")
    return 0


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "generate":
        cmd_generate()
    elif cmd == "check":
        sys.exit(cmd_check())
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == "__main__":
    main()
