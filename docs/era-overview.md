# Era Overview: Web Security Scanning Before 2005

This document provides historical context for the tools archived here. Understanding why these tools were built — and what the web looked like when they were — is part of preserving them properly.

---

## The Web in the Late 1990s

The commercial web took off roughly between 1994 and 1997. By the late 1990s, organizations were rapidly deploying web servers — often without much security and  running off-the-shelf software with default configurations. WAFs didn’t exist, and even firewalls weren’t the absolute requirement they are now.

The dominant web server software of the new era was **NCSA HTTPd**,  its successor **Apache**, alongside Netscape Enterprise Server (and variants/versions in iPlanet, Sun ONE Web Server, and later Sun Java Server), the upstart **Microsoft IIS** (which became ubiquitous after Windows NT 4.0 shipped IIS 2.0 in 1996). Most of them shipped with a default set of **CGI scripts** — small programs that ran server-side to handle form submissions, counters, and other dynamic content. These scripts often contained vulnerabilities..

### The CGI Problem

CGI (Common Gateway Interface) scripts were the primary attack surface for web security in the late 1990s. Common issues:

- **Path traversal** — scripts that allowed `../../etc/passwd` style directory escaping
- **Shell injection** — scripts that passed user input directly to system commands
- **Default credentials** — admin interfaces with no or default passwords
- **Exposed configuration** — scripts that revealed server paths, software versions, or internal hostnames
- **Sample scripts left enabled** — software shipped with demo CGI scripts that were never removed
- **Sensitive Data in Web Root** — logs, user information, and other sensitive data available if you knew the correct path

Tools like PHF (`/cgi-bin/phf`), test-cgi, nph-test-cgi, and dozens of others were found on a huge proportion of web servers through the mid-to-late 1990s. A scanner that could check for their presence against a list of known paths was genuinely useful — and, for attackers, extremely effective.

---

## The Scanner Ecosystem

Web security scanners emerged in roughly three waves during this era:

### Wave 1: CGI Checkers (\~1993–1998)

The earliest tools were simple: take a list of known vulnerable CGI paths, make HTTP requests, print the response code. No intelligence, no fingerprinting — just a list and a loop.

Tools like **cgichk**, **wwwscan**, and various scripts circulated on security mailing lists and personal FTP sites. They were  written C and sometimes Perl in an afternoon and shared with attribution ranging from full authorship to anonymous.

### Wave 2: Structured Scanners (\~1998–2001)

As the CGI problem grew, more structured tools emerged with broader signature databases, better reporting, and some fingerprinting capability. **Whisker** (Rain Forest Puppy, 1999) was a landmark in this space — it introduced IDS evasion techniques alongside its scanning, and its signature database concept influenced tools that followed.

The security community was small and interconnected. Many of these tools were announced on mailing lists like **Bugtraq** (moderated by Aleph One at SecurityFocus), **Full Disclosure**, and **NTBugtraq**. Tool authors were often the same people finding the vulnerabilities the tools checked for.

### Wave 3: Consolidation (\~2001–2005)

**Nikto** (Chris Sullo, 2001) represented a new phase —  a structured plugin and database formats that supported easy updates by the maintainer and the community. It absorbed much of what Whisker had established and became a standard tool that's still maintained today.

Commercial scanners also emerged during this period — **Sanctum AppScan**, **SPI Dynamics WebInspect**, and **Watchfire** tools were sold to enterprises. 

---

## Sources

Understanding where these tools came from requires understanding the distribution channels:

- **Bugtraq** — the central nervous system of the security community. New vulnerabilities and tools were announced here.
- **Full Disclosure** — more permissive than Bugtraq, fewer editorial controls.
- **Packet Storm** (packetstormsecurity.com) — an archive of security tools and advisories, partially still accessible today.
- **rootshell.com** — another archive, now gone; some content accessible via Wayback.
- **Personal homepages** — many tools were hosted on GeoCities, Tripod, university pages, or personal domains that no longer exist.
- **SourceForge** — became important around 2000; hosts much of the early 2000s open source tooling, though many projects are in poor shape.

---

## Preservation Challenges

- **Link rot** — the original homepages for most of these tools are gone
- **Binary-only distribution** — some tools were distributed as compiled binaries with no source
- **No versioning** — many tools were distributed as a single file with no version control; multiple "versions" exist as slightly different copies with no clear lineage
- **Unsigned/unverified archives** — files found on Wayback or old FTP servers cannot always be verified as authentic
- **Fragmented documentation** — README files and man pages were sometimes separate from the tool itself
- **Countless forks** — users of the tools frequently forked them with the same or every similar names to add small featurs

See [preservation-notes.md](./preservation-notes.md) for practical guidance on finding and verifying old tools.