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

> **Status: source recovered.** A copy of the scanner (`cgiscan.c`) has been located and is held in `src/`. Its internal comment dates it **Jan 1999, Updated Feb 1999** — see Historical Context for how this bears on the "first public CGI scanner" claim.

---

## Description

A CGI scanner written in C and attributed to **Bronc Buster of LoU** (Legions of the Underground). Several contemporaries point to it as likely the *first*public CGI scanner, predating the CKS & Fdisk / [cgichk](../cgichk/README.md)lineage. The recovered source, `cgiscan.c`, connects to a target web server on port 80, prints the `HEAD /` server banner, then probes a fixed list of 23 known-vulnerable CGI paths over HTTP/1.0, reporting each as found / not found based on a `200` substring in the response.

---

## Historical Context

This entry began as an open research question and now holds a recovered artifact. The evidence:

- The recovered `src/cgiscan.c` carries the comment *"coded by Bronc Buster / Jan 1999 / Updated Feb 1999"* and prints `coded by Bronc Buster - Updated Feb 1999` at runtime. This matches the Packet Storm [id/12206](https://packetstormsecurity.com/files/12206/) file dated **January 1999**.
- Packet Storm [id/12316](https://packetstormsecurity.com/files/12316/) code comment claiming *"coded by Bronc Buster of LoU - Nov 1998"* — which, **if verified**, would push the authorship date back to Nov 1998. That earlier copy has **not** been recovered here; the artifact in `src/` is the Jan/Feb 1999 version.

---

## Features

- Probes a fixed list of 23 known-vulnerable CGI paths (phf, test-cgi, php.cgi, faxsurvey, webgais, aglimpse, campas, FrontPage `_vti_pvt` password files, etc.)
- Prints the target's `HEAD /` server banner before scanning
- Simple HTTP/1.0 GET requests, one connection per check
- Detection by `200` substring match in the response
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

See `src/cgiscan.c` — a single C source file, self-contained (BSD sockets, no external libraries). Compile with `gcc cgiscan.c -o cgiscan`; run with `./cgiscan target.example.com`.

### Recovered

| Version | Source | Internal date | Notes |
| --- | --- | --- | --- |
| cgiscan.c | Packet Storm [id/12206](https://packetstormsecurity.com/files/12206/) | Jan 1999, Updated Feb 1999 | Single C file; 23 CGI checks; HTTP/1.0; `200`-substring detection |

### Wanted

- [**id/12316**](https://packetstormsecurity.com/files/12316/) — the copy carrying the *"Bronc Buster of LoU - Nov 1998"* code comment (needed to confirm the Nov 1998 claim)
- Any earlier copy, or a **dated mailing-list / newsgroup post or t-file** referencing the tool

### Checksums

<!-- BEGIN CHECKSUMS -->
| Archive | SHA256 |
| --- | --- |
| `src/cgiscan.c` | `c62d6178c4b5ea44b60d8e433c016dcee55f3ea9036fdc47f21330b0c6fe6b76` |
<!-- END CHECKSUMS -->

---

## References & Links

- [Packet Storm id/12206 (Jan 1999, "older")](https://packetstormsecurity.com/files/12206/)
- [Packet Storm id/12316 ("Nov 1998" code comment)](https://packetstormsecurity.com/files/12316/)

---

## Notes

Attribution is by handle ("Bronc Buster of LoU"). The Nov 1998 date is a claim in a code comment, not independently confirmed. If you have the source, a dated post, or a firsthand account, please open an issue.

---

*Entry status: Basic — Contributed by: [sullo](https://github.com/sullo)*