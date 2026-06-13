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

The original code is credited to **CKS & Fdisk**. The best-dated surviving artifact is **cgichk v1.34.2**, repackaged by **su1d sh3ll** — 60 CGI checks, an internal code timestamp of `13.05.99`, posted to Packet Storm ([id/11875](https://packetstormsecurity.com/files/11875/)) on 1999-08-17. Later iterations of the same codebase include **CGI Checker v1.35** (65 checks, published in HWA ezine #19) and **cgichk v2.6.0**. These are documented here as versions of one lineage rather than separate entries.

This places cgichk firmly in the May–August 1999 cluster of CGI-scanner activity. It is the earliest *precisely dated* tool in that branch, though it is likely **not** the first public CGI scanner — see the [Bronc Buster](../bronc-buster/README.md) candidate and the Research section of the [top-level README](../../../README.md).

---

## Version History

| Version | Date | Notes |
| --- | --- | --- |
| v1 | \~1999 | Original CKS & Fdisk release. Not located. |
| v1.34.2 | 1999-08-17 | su1d sh3ll repackaging; 60 checks; internal timestamp `13.05.99`; Packet Storm [id/11875](https://packetstormsecurity.com/files/11875/) |
| CGI Checker v1.35 | 1999 | 65 checks; published in HWA ezine #19 |
| v2.6.0 | \~1999–2000 | Later iteration of the same codebase |

---

## Features

- Probes \~60 known-vulnerable CGI paths (incl. UnlG/THC backdoors, phf, test-cgi, php.cgi, webgais, etc.)
- Simple HTTP/1.0 requests, `200`-substring detection, results to stdout
- Optional `-d` debug mode (`cgichk host -d`)
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

See `src/cgichk1.34.2.c` — the su1d sh3ll recode of the CKS & Fdisk source, a single self-contained C file (BSD sockets, no external libraries). Its header comment reads *"CGI scanner v1.34, m0dify and recode by su1d sh3ll //UnlG 1999 … Source c0de by \[CKS & Fdisk\]"* with an internal timestamp of `12:00 13.05.99`. Compile with `gcc cgichk1.34.2.c -o cgichk`; run with `./cgichk host`.

### Recovered

| Version | Source | Internal date | Notes |
| --- | --- | --- | --- |
| v1.34.2 | Packet Storm [id/11875](https://packetstormsecurity.com/files/11875/) | `13.05.99` | su1d sh3ll recode; single C file; \~60 CGI checks; HTTP/1.0; `200`-substring detection |

### Wanted

- **v1** — the original CKS & Fdisk release (pre-1.34.2), not yet located
- **CGI Checker v1.35** — as published in HWA ezine #19

Have either? Add the source to `src/` and update the status.

### Checksums

<!-- BEGIN CHECKSUMS -->
| Archive | SHA256 |
| --- | --- |
| `src/cgichk1.34.2.c` | `49f75ad6e520c8b96c4615f896c59d4508cb0dd96c285d3065cc79180cbef9ff` |
<!-- END CHECKSUMS -->

---

## References & Links

- [Packet Storm id/11875 — cgichk v1.34.2 (su1d sh3ll)](https://packetstormsecurity.com/files/11875/)
- [HWA ezine #19 — CGI Checker v1.35 su1d sh3ll //UnlG](http://web.textfiles.com/ezines/HWA/hwa-hn19.txt)

---

## Notes

**Conflicting attribution — to research.** A separately circulated copy of cgichk is attributed to `sasha / ussr.labs` in its file headers. Its origin is unknown: it may be a relabeling of the CKS & Fdisk lineage, or a distinct tool that happened to share the name (common in this era). Treated here as an open question until source or a dated post resolves it.

Dates above mix three things that can differ by months: the **internal** code timestamp (`13.05.99`), the **posting** date (1999-08-17), and the actual **authorship** date. Treat them accordingly.

---

*Entry status: Basic — Contributed by: [sullo](https://github.com/sullo)*