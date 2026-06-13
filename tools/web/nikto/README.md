# Nikto

<!-- Metadata below is generated from meta.yml by scripts/archive.py — do not edit by hand. -->

## Metadata

<!-- BEGIN METADATA -->
| Field | Value |
| --- | --- |
| **Product Name** | Nikto |
| **Owner / Author** | Chris Sullo |
| **Year Released** | 2001-12-27 |
| **Primary Type** | Web Scanner |
| **Secondary Type(s)** | CGI Scanner, Fingerprinter |
| **Model** | Open Source |
| **Active** | Yes |
<!-- END METADATA -->

---

## Description

Nikto is a web server scanner that performs tests against web servers for multiple items, including over 7,000 potentially dangerous files/CGIs, checks for outdated versions of over 1,250 servers, and version-specific problems on over 270 servers. It is one of the few tools from this era that is still actively maintained and developed.

Nikto was heavily influenced by and built upon the work of Rain Forest Puppy's Whisker and libwhisker, using the libwhisker library for HTTP handling.

---

## Historical Context

Nikto arrived at a transitional point in web security. The CGI scanning era was winding down as dynamic application frameworks became dominant, but web servers were still misconfigured and running default content at massive scale. Nikto consolidated the accumulated knowledge of the CGI scanning era into a single, maintained, community-updateable tool.

Its structured plugin and database format made it easier for the community to contribute signatures without needing to modify core code. This was novel for the time and contributed to its longevity.

Nikto was announced on Bugtraq and quickly became a standard component in penetration testers' toolkits. Unlike many of its predecessors, it had a clear maintainer and a home on CIRT.net that stayed up.

---

## Version History

| Version | Release | Notes |
| --- | --- | --- |
| 1.00 | 2001-12-27 | Initial Public Release |

---

## Features

- Checks for thousands of potentially dangerous files and CGIs
- Identifies outdated server software versions
- Checks server configuration issues (directory listing, HTTP methods, etc.)
- SSL support (early versions basic, improved later)
- Multiple output formats: plain text, CSV, HTML
- Supports HTTP proxies
- IDS evasion techniques inherited from libwhisker
- Tunable scan options to run specific check categories
- Plugin architecture allowing community database updates

---

## Technical Details

| Field | Value |
| --- | --- |
| **Language** | Perl |
| **Platform** | Unix/Linux, Windows |
| **Dependencies** | Perl 5, libwhisker (bundled in early versions) |

---

## Source Code

### Available

- Earliest version available: 1.015

### Wanted

- Version 1.00

### Checksums

<!-- BEGIN CHECKSUMS -->
| Archive | SHA256 |
| --- | --- |
| `src/nikto-1.015.tar.bz2` | `d9aef251a781a1f253d24aadca97ee38b413ee435ebb4710a264a8bb6324b907` |
<!-- END CHECKSUMS -->

---

## Screenshots / Output Examples

```
- Nikto v1.00/1.00    example.com:80
+ Target IP:        10.0.0.1
+ Target Hostname:  example.com
+ Target Port:      80
+ Start Time:       Thu Oct 11 14:22:48 2001
---------------------------------------------------------------------------
+ Server: Apache/1.3.20 (Unix) mod_ssl/2.8.4 OpenSSL/0.9.6b
+ mod_ssl/2.8.4 - mod_ssl 2.8.7 and lower are vulnerable to a remote
  buffer overflow which may allow a remote shell (difficult). CVE-2002-0082
+ Apache/1.3.20 - Apache 1.x up 1.3.26 are vulnerable to a remote DoS
  and possible code execution. CAN-2002-0392.
+ /cgi-bin/phf: This might be interesting...
+ /cgi-bin/test-cgi: This might be interesting...
```

---

## References & Links

- [CIRT.net Nikto page (archived)](https://web.archive.org/web/20020603175243/http://www.cirt.net/code/nikto.shtml)
- [Original Bugtraq announcement, 2001](https://seclists.org/bugtraq/2001/Dec/264)
- [Nikto GitHub (current, active)](https://github.com/sullo/nikto)
- [libwhisker by Rain Forest Puppy](../whisker/README.md)
- [Nikto Versions](https://github.com/sullo/nikto-versions) - Older Releases Archive by the author
- [Nikto on Wikipedia](https://en.wikipedia.org/wiki/Nikto_\(vulnerability_scanner\))

---

## Notes

Nikto remains actively maintained over 25 years after its initial release. The current codebase has been substantially rewritten in v2 in 2006, and a large update of v2.5.0 in 2023. A 25th anniversary release, v2.6.0, was made in 2026.

---

*Entry status: Full — Contributed by: [sullo](https://github.com/sullo)*
