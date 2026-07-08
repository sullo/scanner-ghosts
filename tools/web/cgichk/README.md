# cgichk

<!-- Metadata below is generated from meta.yml by scripts/archive.py — do not edit by hand. -->

## Metadata

<!-- BEGIN METADATA -->
| Field | Value |
| --- | --- |
| **Product Name** | cgichk |
| **Owner / Author** | CKS & Fdisk |
| **Year Released** | 1999 |
| **Primary Type** | CGI Scanner |
| **Secondary Type(s)** |  |
| **Model** | Open Source |
| **Active** | No |
<!-- END METADATA -->

---

## Description

cgichk was a small CGI scanner written in **C** that checked web servers against a list of known vulnerable CGI scripts and paths. It originated with **CKS & Fdisk** and was repackaged and extended by others over 1999, making it one of the central codebases of the mid-1999 CGI-scanning cluster. It circulated informally on IRC, underground FTP sites, and security ezines rather than through mainstream channels.

---

## Historical Context

While tools like Whisker were announced on Bugtraq by researchers with public identities, cgichk represents a parallel tradition: tools written and shared within less formal networks, often with no documentation and attribution only by handle.

The original code is credited to **CKS & Fdisk**. Two earlier artifacts than the previously best-dated release have now been recovered from hackersclub.com's `c_scripts` directory (via the Wayback Machine):

- **`Cgichk.c`** — the CKS & Fdisk base with **no su1d modifications**: 13 checks, banner reads plainly `[CKS & Fdisk]'s CGI Checker`, no greetz block, no UnlG backdoor. This is the un-recoded original the whole lineage descends from.
- **`cgichk-11b.c`** — su1d sh3ll's recode, header labeled *"CGI scanner v1.0"* but banner/usage labeled *"CGI Checker 1.1b"*, internal timestamp `12:03 11.03.99` (11 Mar 1999), 30 checks. It adds the `UnlG1.1` backdoor probe as check #1, plus FrontPage `.pwd` and `cgi-dos`/`cgi-win` paths on top of the base.

That `11.03.99` timestamp moves the earliest *precisely dated* artifact of this branch back from May to **March 1999**, ~2 months before **cgichk v1.34.2** (`13.05.99`; 60 checks; Packet Storm [id/11875](https://packetstormsecurity.com/files/11875/); posted 1999-08-17). Later iterations of the same codebase include **CGI Checker v1.35** (65 checks, published in HWA ezine #19) and **cgichk v2.6.0**. All are documented here as versions of one lineage rather than separate entries.

This places cgichk firmly in the early-1999 CGI-scanner cluster. It is now among the earliest *precisely dated* tools in that branch, though it is likely **not** the first public CGI scanner — see the [Bronc Buster](../bronc-buster/README.md) candidate and the Research section of the [top-level README](../../../README.md).

---

## Version History

| Version | Date | Notes |
| --- | --- | --- |
| CKS & Fdisk base (`Cgichk.c`) | \~1999 | Un-recoded original; 13 checks; no su1d credit. **Recovered** (hackersclub.com) |
| v1.0 / 1.1b (`cgichk-11b.c`) | 1999-03-11 | su1d sh3ll recode; header `v1.0`, banner `1.1b`; 30 checks; internal timestamp `12:03 11.03.99`. **Recovered** (hackersclub.com) |
| v1.34.2 | 1999-08-17 | su1d sh3ll repackaging; 60 checks; internal timestamp `13.05.99`; Packet Storm [id/11875](https://packetstormsecurity.com/files/11875/). **Recovered** |
| CGI Checker v1.35 | 1999 | 65 checks; published in HWA ezine #19. Not located. |
| v2.6.0 | \~1999–2000 | Later iteration of the same codebase. Not located. |

---

## Features

- Probes a hardcoded list of known-vulnerable CGI paths — **13** in the CKS & Fdisk base (`Cgichk.c`), **30** in the 1.1b recode (`cgichk-11b.c`), **60** in v1.34.2 (phf, test-cgi, php.cgi, webgais, faxsurvey, wwwboard.pl, etc.)
- 1.1b adds the `UnlG1.1` backdoor probe (check #1), FrontPage `_vti_pvt/*.pwd`, and `cgi-dos/args.bat` / `cgi-win/uploader.exe`
- Interactive flow: `HEAD /` banner grab first (prints httpd version), then `getchar()` prompts to step through the CGI scan
- Simple HTTP/1.0 requests, `200`-substring detection (`strstr(buf,"200")`), results to stdout
- Optional `-d` debug mode dumps each raw response (`cgichk host -d`)
- Target port hardcoded to 80 in source (edit `htons(80)` to change)

---

## Technical Details

| Field | Value |
| --- | --- |
| **Language** | C |
| **Platform** | Unix/Linux (tested per source on Slackware/RH/FreeBSD/IRIX) |
| **Dependencies** | libc only; `gcc cgichk1.34.2.c -o cgichk` |
| **Typical Usage** | `./cgichk target.example.com` |

---

## Source Code

Source code status: **Partial**

Three points in the lineage are preserved in `src/`, each a single self-contained C file (BSD sockets, libc only, `void main`). Compile any with `gcc <file> -o cgichk`; run with `./cgichk host` (add `-d` for debug):

- **`Cgichk.c`** — the CKS & Fdisk base, no su1d recode. Header is just `/* Tested on Slackware linux with kernel 2.0.35 */`; banner prints `[CKS & Fdisk]'s CGI Checker`. 13 checks.
- **`cgichk-11b.c`** — su1d sh3ll's recode. Header reads *"CGI scanner v1.0, m0dify and recode by su1d sh3ll //UnlG 1999 … Source c0de by \[CKS & Fdisk\]"* with a footer timestamp `12:03 11.03.99`; usage banner prints `CGI Checker 1.1b`. 30 checks.
- **`cgichk1.34.2.c`** — later su1d recode. Header *"CGI scanner v1.34 … Source c0de by \[CKS & Fdisk\]"*, internal timestamp `12:00 13.05.99`. \~60 checks.

The three share the same skeleton — parallel `buff[]`/`cginame[]` arrays, a `HEAD /` banner grab, then a `getchar()`-gated loop doing HTTP/1.0 `GET`s and matching `200` via `strstr`. The diff between them is purely the length of the probe list, which is a clean window into how the CGI-vuln corpus grew through 1999.

### Recovered

| Version | Source | Internal date | Notes |
| --- | --- | --- | --- |
| CKS & Fdisk base (`Cgichk.c`) | hackersclub.com `c_scripts` ([Wayback](https://web.archive.org/web/20001007050131id_/http://www.hackersclub.com/km/files/c_scripts/Cgichk.c)) | — | un-recoded original; 13 checks; no su1d credit |
| v1.0 / 1.1b (`cgichk-11b.c`) | hackersclub.com `c_scripts` ([Wayback](https://web.archive.org/web/20001007045048id_/http://www.hackersclub.com/km/files/c_scripts/cgichk-11b.c)) | `11.03.99` | su1d sh3ll recode; 30 checks; adds UnlG backdoor + FrontPage + cgi-dos/win |
| v1.34.2 | Packet Storm [id/11875](https://packetstormsecurity.com/files/11875/) | `13.05.99` | su1d sh3ll recode; \~60 CGI checks; HTTP/1.0; `200`-substring detection |

### Wanted

- **CGI Checker v1.35** — as published in HWA ezine #19 (65 checks)
- **cgichk v2.6.0** — later iteration of the same codebase

Have either? Add the source to `src/` and update the status.

_Note: `Cgichk.c` is the un-recoded CKS & Fdisk base and is the strongest candidate yet for the "v1" original, but it carries no version string or date of its own — treat "the original release" as still nominally open until a dated post confirms it._

### Checksums

<!-- BEGIN CHECKSUMS -->
| Archive | SHA256 |
| --- | --- |
| `src/Cgichk.c` | `272e93c20790d0f245215a950c51579adb7ffd6701bab4f7f1ea880190a00a8f` |
| `src/cgichk-11b.c` | `289ccef98ee4ca8a5f039edc0623aab9f0065cf3796ef53400e16dd6fc106e46` |
| `src/cgichk1.34.2.c` | `49f75ad6e520c8b96c4615f896c59d4508cb0dd96c285d3065cc79180cbef9ff` |
<!-- END CHECKSUMS -->

---

## References & Links

- [Packet Storm id/11875 — cgichk v1.34.2 (su1d sh3ll)](https://packetstormsecurity.com/files/11875/)
- [HWA ezine #19 — CGI Checker v1.35 su1d sh3ll //UnlG](http://web.textfiles.com/ezines/HWA/hwa-hn19.txt)
- [hackersclub.com `c_scripts/cgichk-11b.c` — v1.0 / 1.1b (Wayback, raw)](https://web.archive.org/web/20001007045048id_/http://www.hackersclub.com/km/files/c_scripts/cgichk-11b.c)
- [hackersclub.com `c_scripts/Cgichk.c` — CKS & Fdisk base (Wayback, raw)](https://web.archive.org/web/20001007050131id_/http://www.hackersclub.com/km/files/c_scripts/Cgichk.c)

---

## Notes

**Conflicting attribution — to research.** A separately circulated copy of cgichk is attributed to `sasha / ussr.labs` in its file headers. Its origin is unknown: it may be a relabeling of the CKS & Fdisk lineage, or a distinct tool that happened to share the name (common in this era). Treated here as an open question until source or a dated post resolves it.

Dates above mix three things that can differ by months: the **internal** code timestamp (`13.05.99`), the **posting** date (1999-08-17), and the actual **authorship** date. Treat them accordingly.

---

*Entry status: Full — Contributed by: [sullo](https://github.com/sullo)*