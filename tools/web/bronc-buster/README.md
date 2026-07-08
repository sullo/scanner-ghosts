# Bronc Buster CGI Scanner

<!-- Metadata below is generated from meta.yml by scripts/archive.py — do not edit by hand. -->

## Metadata

<!-- BEGIN METADATA -->
| Field | Value |
| --- | --- |
| **Product Name** | Bronc Buster CGI Scanner |
| **Owner / Author** | Bronc Buster (LoU) |
| **Year Released** | 1999 |
| **Primary Type** | CGI Scanner |
| **Secondary Type(s)** |  |
| **Model** | Open Source |
| **Active** | No |
<!-- END METADATA -->

> **Status: source recovered (two versions).** Two builds of the scanner are held in `src/`. `cgiscan.c` is the earlier **v1.0 (Jan 1999)** release; `cgiscan_feb99.c` is the later **Updated Feb 1999** revision. See Historical Context for how this bears on the "first public CGI scanner" claim.

---

## Description

A CGI scanner written in C and attributed to **Bronc Buster of LoU** (Legions of the Underground). Several contemporaries point to it as likely the *first* public CGI scanner, predating the CKS & Fdisk / [cgichk](../cgichk/README.md) lineage. The recovered source connects to a target web server on port 80, prints the `HEAD /` server banner, then probes a fixed list of known-vulnerable CGI paths over HTTP/1.0, reporting each as found / not found.

Two versions are held in `src/`:

- **`cgiscan.c` — v1.0 (Jan 1999):** probes **21** CGI paths. Detection is by the **absence** of a `404` substring in the response (i.e. anything other than a 404 is treated as *found*). No inter-request delays. Runtime banner reads `coded by Bronc Buster of LoU - Jan 1999`.
- **`cgiscan_feb99.c` — Updated Feb 1999:** probes **23** paths (adds `cgi-dos/args.bat` and `cgi-win/uploader.exe`). Detection flips to a positive **`200`** substring match, and `system("sleep 2")` delays are inserted between requests. Runtime banner reads `coded by Bronc Buster - Updated Feb 1999`.

---

## Historical Context

This entry began as an open research question and now holds two recovered artifacts. The evidence:

- `src/cgiscan.c` is the **v1.0** release: its header comment reads *"coded by Bronc Buster of LoU - Jan 1999"* and it prints the same at runtime. It probes 21 paths and detects on the absence of a `404`. Recovered from a [Wayback Machine capture of hackersclub.com](https://web.archive.org/web/20001202132800/http://www.hackersclub.com/km/files/c_scripts/cgiscan.c) (found by Mike Shema).
- `src/cgiscan_feb99.c` is the later revision: its comment reads *"coded by Bronc Buster / Jan 1999 / Updated Feb 1999"* and it prints `coded by Bronc Buster - Updated Feb 1999`. It matches the Packet Storm [id/12206](https://packetstormsecurity.com/files/12206/) file dated **January 1999**.
- Packet Storm [id/12316](https://packetstormsecurity.com/files/12316/) code comment claiming *"coded by Bronc Buster of LoU - Nov 1998"* — which, **if verified**, would push the authorship date back to Nov 1998. That earlier copy has **not** been recovered here; the artifacts in `src/` are the Jan 1999 (v1.0) and Updated Feb 1999 versions.

---

## Features

- Probes a fixed list of known-vulnerable CGI paths (phf, test-cgi, php.cgi, faxsurvey, webgais, aglimpse, campas, FrontPage `_vti_pvt` password files, etc.) — 21 in v1.0, 23 in the Feb 1999 revision
- Prints the target's `HEAD /` server banner before scanning
- Simple HTTP/1.0 GET requests, one connection per check
- Detection by status substring match: absence of `404` in v1.0, presence of `200` in the Feb 1999 revision
- Output to stdout

---

## Technical Details

| Field | Value |
| --- | --- |
| **Language** | C |
| **Platform** | Unix/Linux (BSD sockets) |
| **Dependencies** | libc only; `gcc cgiscan.c -o cgiscan` |
| **Typical Usage** | `./cgiscan target.example.com` |

---

## Source Code

Source code status: **Available**

See `src/` — single C source files, self-contained (BSD sockets, no external libraries). Compile with `gcc cgiscan.c -o cgiscan`; run with `./cgiscan target.example.com`.

### Recovered

| Version | File | Source | Internal date | Notes |
| --- | --- | --- | --- | --- |
| v1.0 | `cgiscan.c` | [hackersclub.com via Wayback](https://web.archive.org/web/20001202132800/http://www.hackersclub.com/km/files/c_scripts/cgiscan.c) (found by Mike Shema) | Jan 1999 | Single C file; 21 CGI checks; HTTP/1.0; detects on **absence** of `404`; no request delays; banner `... of LoU - Jan 1999` |
| Updated Feb 1999 | `cgiscan_feb99.c` | Packet Storm [id/12206](https://packetstormsecurity.com/files/12206/) | Jan 1999, Updated Feb 1999 | 23 CGI checks (adds `args.bat`, `uploader.exe`); `200`-substring detection; `sleep 2` between requests |

### Wanted

- [**id/12316**](https://packetstormsecurity.com/files/12316/) — the copy carrying the *"Bronc Buster of LoU - Nov 1998"* code comment (needed to confirm the Nov 1998 claim)
- Any earlier copy, or a **dated mailing-list / newsgroup post or t-file** referencing the tool

### Checksums

<!-- BEGIN CHECKSUMS -->
| Archive | SHA256 |
| --- | --- |
| `src/cgiscan.c` | `d31323590b55c1976e01976620385f097b57421b78144bb0c0c89eabffda94fa` |
| `src/cgiscan_feb99.c` | `c62d6178c4b5ea44b60d8e433c016dcee55f3ea9036fdc47f21330b0c6fe6b76` |
<!-- END CHECKSUMS -->

---

## References & Links

- [v1.0 source — hackersclub.com via Wayback Machine](https://web.archive.org/web/20001202132800/http://www.hackersclub.com/km/files/c_scripts/cgiscan.c) (found by Mike Shema)
- [Packet Storm id/12206 (Jan 1999, "older")](https://packetstormsecurity.com/files/12206/)
- [Packet Storm id/12316 ("Nov 1998" code comment)](https://packetstormsecurity.com/files/12316/)

---

## Notes

Attribution is by handle ("Bronc Buster of LoU"). The Nov 1998 date is a claim in a code comment, not independently confirmed. If you have the source, a dated post, or a firsthand account, please open an issue.

---

*Entry status: Basic — Contributed by: [sullo](https://github.com/sullo)*