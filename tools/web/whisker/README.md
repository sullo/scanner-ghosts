# Whisker

<!-- Metadata below is generated from meta.yml by scripts/archive.py — do not edit by hand. -->

## Metadata

<!-- BEGIN METADATA -->
| Field | Value |
| --- | --- |
| **Product Name** | Whisker |
| **Owner / Author** | Rain Forest Puppy |
| **Year Released** | 1999 |
| **Primary Type** | CGI Scanner |
| **Secondary Type(s)** | Web Scanner, Fingerprinter |
| **Model** | Open Source |
| **Active** | No |
<!-- END METADATA -->

---

## Description

Whisker was a CGI scanner written in Perl by the pseudonymous security researcher Rain Forest Puppy (RFP). It was notable not only for its CGI scanning capability but for introducing systematic **IDS evasion techniques** into web scanning — a significant conceptual contribution. The accompanying libwhisker library became the foundation for Nikto and influenced a generation of web security tools.

---

## Historical Context

Rain Forest Puppy was one of the most prolific web vulnerability researchers of the late 1990s. He discovered and published advisories on major vulnerabilities including multiple IIS flaws and the phf CGI bug, and is commonly known as the first person to exploit SQL injection. Whisker was both a tool and a research artifact — it demonstrated that the IDS products of the day could be  evaded by varying request formatting, encoding, and HTTP version usage.

The IDS evasion paper that accompanied Whisker ("Whisker's Anti-IDS tactics") was widely read and forced IDS vendors to reckon with evasion as a first-class problem.

Whisker was distributed via RFP's site at `wiretrip.net` and announced on Bugtraq. The libwhisker library separated the HTTP handling code from Whisker itself, allowing it to be embedded in other tools — most notably, Nikto.

---

## Version History

| Version | Year | Notes |
| --- | --- | --- |
| 1.0 | 1999 | Initial release |
| 1.1 | 1999 | Additional checks, evasion improvements |
| 1.3 | 1999 |  |
| 1.4 | 2000 |  |
| 2.0 | 2000 | Substantial rewrite, improved IDS evasion |
| 2.1 | \~2001 |  |

libwhisker was maintained separately and continued after Whisker itself was abandoned.

---

## Features

- CGI path scanning against a list of known vulnerable scripts
- **IDS evasion techniques**, including:
  - URL encoding variations
  - Double-slash paths
  - Reverse directory traversal
  - False leading filenames
  - HTTP version manipulation
  - Session splicing (premature TCP segment sending)
- Server fingerprinting via response header analysis
- HTTP/1.0 and HTTP/1.1 support
- Proxy support

---

## Technical Details

| Field | Value |
| --- | --- |
| **Language** | Perl |
| **Platform** | Unix/Linux (primarily), Windows |
| **Dependencies** | Perl 5; libwhisker (later versions) |
| **Typical Usage** | `whisker.pl -h target.example.com -T 4` |

---

## Source Code

Source code status: **Available**

See `src/` for recovered versions.

Whisker was distributed as a single Perl script in early versions, making recovery from Wayback captures more reliable than tools distributed as tarballs.

### Recovered

| Version | Source | URL | Retrieved | Notes |
|---------|--------|-----|-----------|-------|
| 1.4 | Packet Storm | https://packetstormsecurity.com/files/10276/whisker.pl.gz | 2024-01-01 | Perl script, gzipped |
| 2.0 | Wayback Machine | https://web.archive.org/web/20010601000000*/http://www.wiretrip.net/rfp/bins/whisker-2.0.tar.gz | 2024-01-01 | tarball |

Documentation: the Anti-IDS tactics paper was recovered from the Wayback Machine; README files came bundled with the tarballs.

### Wanted

- Versions 1.0, 1.1, 2.1 — not yet located
- libwhisker source tracked separately (see Nikto entry)
- Windows binary port (if one was released) — unknown/not located

### Checksums

<!-- BEGIN CHECKSUMS -->
| Archive | SHA256 |
| --- | --- |
| `src/whisker-1.4.tar.gz` | `8b86ccd8194080e86cf10ea7f3931ea4725c474949ea1f0a4febc495eb8cd3f4` |
| `src/whisker-2.0.tar.gz` | `1037e90347aa09ff347e9136ad307e610f1df30a98223028966119f73224e78a` |
<!-- END CHECKSUMS -->

---

## Screenshots / Output Examples

```
-- whisker / v1.4 / rain forest puppy / www.wiretrip.net --

= - = - = - = - = - = - = - = - = - = - = - = - = - = -
 Host: target.example.com
 Port: 80
 Server: Microsoft-IIS/4.0
= - = - = - = - = - = - = - = - = - = - = - = - = - = -

+ /cgi-bin/test.bat (IIS)
+ /scripts/..%255c../winnt/system32/cmd.exe (IIS - unicode)
+ /_vti_bin/shtml.exe
```

---

## References & Links

- [wiretrip.net (Wayback, 2000)](https://web.archive.org/web/20000815000000*/http://www.wiretrip.net/rfp/)
- [Whisker/anti-IDS tactics paper (Wayback)](https://web.archive.org/web/20010301000000*/http://www.wiretrip.net/rfp/txt/whiskerids.html)
- [Bugtraq announcement](https://seclists.org/bugtraq/1999/Oct/190)
- [Packet Storm listing](https://packetstormsecurity.com/files/search/?q=whisker)

---

## Notes

Rain Forest Puppy (later publicly identified as Jeff Forristal) kept his identity pseudonymous for much of this era. Active development of Whisker ended ~2002 in favor of libwhisker. He was active in the security community through approximately 2002–2003, then largely disappeared from public view. His research — particularly on IIS vulnerabilities and CGI scanning methodology — had outsized influence.

Libwhisker2 continued to be maintained by the Nikto project after Whisker itself was abandoned.
