# Taxonomy

This document defines the controlled vocabulary for all metadata fields in the archive. Use these exact values in tool profiles. If something doesn't fit, open an issue before inventing a new term.

---

## Primary Type / Secondary Type(s)

These values apply to both `Primary Type` and `Secondary Type(s)`. A tool has exactly one Primary Type and zero or more Secondary Types.

| Value | Definition |
| --- | --- |
| `CGI Scanner` | Scans web servers for known vulnerable CGI scripts and paths. The dominant web scanner type of the late 1990s. |
| `Web Scanner` | Broader web application scanning — may include CGI checks but also covers other web-layer vulnerabilities. |
| `Vulnerability Scanner` | General-purpose vulnerability identification, typically across multiple services or protocols. |
| `Port Scanner` | Enumerates open TCP/UDP ports on a target host. |
| `Fingerprinter` | Identifies software types, versions, OS, or server configurations without necessarily probing for vulnerabilities. |
| `Proxy / Interceptor` | Operates as a proxy between a browser and a server, capturing or modifying traffic. |
| `Discovery` | Performs brute-force, dictionary, or credential-stuffing attacks against authentication systems. |
| `Crawler` | Maps the structure of a web application by following links; may feed data to other scanners. |
| `Exploit Framework` | Provides a platform for launching known exploits, beyond simple scanning. |
| `Fuzzer` | Sends malformed or unexpected input to identify parser bugs, crashes, or unexpected behavior. |

---

## Model

Describes how the tool was licensed and distributed.

| Value | Definition |
| --- | --- |
| `Open Source` | Source code was publicly available under an explicit open source license (GPL, BSD, MIT, etc.). |
| `Freeware` | Free to use or download, but source code was not made available. |
| `Commercial` | Sold for money; source code not publicly available. |
| `Unknown` | License terms are not known or were never specified. |

---

## Active

Current status of the tool.

| Value | Definition |
| --- | --- |
| `Yes` | Still actively maintained and receiving updates. |
| `No` | Development officially ended. Use a note to record the approximate end date if known. |
| `Abandoned` | Development stopped without announcement; no updates for a significant period. |
| `Unknown` | Status cannot be determined. |

---

## Source Code Status

Used in the Source Code section of a tool profile.

| Value | Definition |
| --- | --- |
| `Available` | Source code is preserved in the `src/` directory for at least one version. |
| `Partial` | Source exists for some versions but not all, or only portions of the source are available. |
| `Not Available` | Source code could not be found. Binary-only, lost, or never released. |
| `Unknown` | It is unclear whether source was ever made available. |

---

## Entry Status

Used at the bottom of each tool profile.

| Value | Definition |
| --- | --- |
| `Stub` | Name, author, year, and a brief description only. |
| `Basic` | All required fields complete, reasonable description, at least one reference. |
| `Full` | All fields, version history, technical details, complete references and notes. |
| `Archived` | Full entry plus source code in `src/`. |

---

## Notes on Dating

- Use `YYYY` for year-only dates.
- Use `YYYY-MM-DD` for precise dates.
- Use `~YYYY` for approximate years.
- Do not use date ranges (e.g., `1998–1999`) in the Year Released field; use the earliest known release date and note uncertainty in the Version History or Notes section.