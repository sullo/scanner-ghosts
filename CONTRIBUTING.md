# Contributing to Retro Scanner Archive

Thank you for helping preserve infosec history. This document explains how to contribute effectively.

---

## Ways to Contribute

| Type | How |
| --- | --- |
| New tool entry | Copy the template, fill it out, open a PR |
| Add source code | Add the original archive to the tool's `src/` directory, record its provenance |
| Improve an entry | Correct errors, fill in gaps, add references |
| Submit a lead | Open an "Add a Tool" issue — no write-up required |
| Historical context | Improve `docs/era-overview.md` or add references |

---

## Adding a New Tool Entry

### 1. Copy the template

```
cp schema/tool-template.md tools/web/[toolname]/README.md
```

Use lowercase, hyphenated folder names. Match the tool's common name, not a version-specific one.

```
tools/web/[toolname]/
tools/web/[author]-[toolname]/   # if disambiguation is needed
```

### 2. Fill out the metadata

Each entry's metadata lives in a **`meta.yml`** sidecar next to the README
(copy `schema/meta-template.yml`). The Metadata table, the root entry table,
and the category index are all generated from it — never edit those tables by
hand.

See the field definitions in docs/taxonomy.md for the controlled vocabulary on
types, models, and status values. Frontmatter values must match that vocabulary
exactly, or CI will reject the PR.

**Required fields:** `name`, `author`, `year`, `primary_type`, `model`,
`active`, `source`, `status`.

**Everything else:** fill in what you can. Leave unknown fields as `Unknown` — do not guess or invent.

### 3. Record source provenance

Every entry's README has a `## Source Code` section — record provenance there.
Fill in the status (`Available` / `Partial` / `Not Available` / `Unknown`),
which versions are preserved or still wanted, and:

- Where you found each archive
- When you retrieved it (date matters for Wayback links)
- What's missing and why, if known

See `tools/web/nikto/README.md` and `tools/web/whisker/README.md` for examples
(including a recovery table). Keep it all in the README — do not add a separate
`SOURCES.md`.

### 4. Add source code (if available)

Keep the original archive exactly as distributed and drop it straight into the
tool's `src/` directory, named `[tool]-[version].[ext]` — for example
`src/nikto-1.015.tar.bz2` or `src/whisker-1.4.tar.gz`.

**Rules for source code:**

- Preserve exactly as found. Do not unpack, repack, fix bugs, modernize code, or change formatting.
- Keep the original archive format and compression (`.tar.gz`, `.tar.bz2`, `.gz`, etc.). Do not extract it into the repo.
- One archive per version. Add more versions as separate files in the same `src/`.
- Archives are tracked with Git LFS (see `.gitattributes`) — run `git lfs install` once before adding them.
- Note the exact retrieval source and date in the README `## Source Code` section.

### 5. Generate the tables, then check

Run the generator to fill the Metadata table, checksums, and index tables from
your meta.yml, then validate exactly as CI does:

```
python3 scripts/archive.py generate
python3 scripts/archive.py check
```

`check` must pass (exit 0) before you open the PR.

### 6. Open a pull request

PR title format: `Add: [Tool Name] ([Year])` or `Update: [Tool Name] — [what changed]`

---

## Entry Quality Levels

Entries don't have to be complete. These rough tiers help set expectations:

| Level | What it means |
| --- | --- |
| **Stub** | Name, author, year, 1–2 sentence description. Better than nothing. |
| **Basic** | All required fields, reasonable description, at least one reference link. |
| **Full** | All fields, version history, technical details, references, preservation notes. |
| **Archived** | Full entry + source code in `src/`. |

Label your PR with the appropriate level if you're unsure whether it's complete enough.

---

## Taxonomy Quick Reference

See docs/taxonomy.md for the full list. Common values:

**Primary / Secondary Types:**

- `CGI Scanner` — scans for known CGI vulnerabilities
- `Web Scanner` — broader web application scanning
- `Port Scanner` — TCP/UDP port enumeration
- `Vulnerability Scanner` — generic vuln checking
- `Fingerprinter` — identifies software, OS, versions
- `Proxy / Interceptor` — sits between client and server
- `Discovery` — brute-force or dictionary attacks
- `Crawler` — maps site structure

**Model (license/distribution):**

- `Open Source` — source available under an open license
- `Freeware` — free to use, source not available
- `Commercial` — sold for money

**Active:**

- `Yes` — still maintained
- `No` — development ended, known date if possible
- `Abandoned` — development stopped, unclear when
- `Unknown`

---

## Questions

Open an issue. If you're unsure whether something belongs here, ask.