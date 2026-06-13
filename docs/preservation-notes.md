# Preservation Notes

Practical guidance on finding, retrieving, and verifying old security tools.

---

## Where to Look

### Wayback Machine (web.archive.org)

The first stop. Strategies:

- Search the tool name directly
- Try known old domains: `packetstorm.security.nl`, `rootshell.com`, `l0pht.com`, author personal pages
- Use the CDX API to enumerate all captures of a URL: `http://web.archive.org/cdx/search/cdx?url=example.com/tool/*&output=text`
- Check early captures — 1996–2002 captures are often more complete than later ones
- Download files from captures, not just pages; check linked `.tar.gz`, `.zip`, `.pl`, `.c` files

**Always record the full timestamped Wayback URL**, e.g.: `https://web.archive.org/web/19991204153012/http://www.wiretrip.net/rfp/p/doc.asp?id=21`

### Packet Storm

`packetstormsecurity.com` has been archiving security tools since 1998. Many early tools are still there. The site changed hands several times — early content may also be findable via Wayback at the old domain `packetstorm.security.nl`.

### SourceForge

Many tools moved to SourceForge around 2000–2003. Even abandoned projects often still have their file releases available for download. Browse: `https://sourceforge.net/projects/[toolname]/files/`

SourceForge also retains CVS history for many old projects.

### GitHub

Some tools or their successors were eventually pushed to GitHub, sometimes by the original author and sometimes by third parties. Check for forks and historical imports.

### FTP Archives

Several university and ISP FTP sites mirrored security tools in the late 1990s. Many are gone but some Wayback captures of FTP listings survive. Search for:

- `ftp.replay.com` (Netherlands mirror, archived many tools)
- CERT/CC archives
- University CS department FTP sites

### Mailing List Archives

Tool release announcements on Bugtraq often included the tool itself as an attachment or inline paste. Archives:

- `seclists.org` — archived Bugtraq and many other lists
- `securityfocus.com/archive` — Bugtraq archive with search
- MARC (marc.info) — general mailing list archive

Look for announcement threads, then check if the tool was attached or if a URL was given (then Wayback that URL).

### Personal Contact

If the author is identifiable and still reachable:

- LinkedIn, Twitter/X, personal blogs
- Their current employer's contact page
- GitHub profile

Be respectful. Explain the preservation goal. Many authors are glad to know someone cares, and may have copies of old files they thought were lost.

---

## Verifying What You Find

Provenance matters. When you find a file:

1. **Note the exact source URL and retrieval date.** Record this in the entry's README `## Source Code` section.
2. **Check for multiple copies.** If the same version exists in multiple places, note whether they're identical (compare hashes) or divergent.
3. **Look for checksums.** Some distributions included MD5 sums in README files or announcement posts. If you find one, verify it.
4. **Be skeptical of very clean copies.** A `.tar.gz` with a suspiciously recent modification date may have been repacked.
5. **Preserve what you found, not what you think it should be.** Don't clean up the code, fix encoding issues, or normalize line endings before archiving.

Record file hashes alongside the provenance notes in the README `## Source Code` section:

```
SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
MD5: d41d8cd98f00b204e9800998ecf8427e
```

---

## When Source Isn't Available

Not finding source code is a valid and important finding. Document it:

- Was the tool ever distributed with source? (Check release announcements)
- Was it binary-only for a specific platform?
- Did the author mention plans to release source that never materialized?
- Is it possible the source exists but hasn't been found?

A "Not Available" entry with good documentation of *why* it's not available is valuable. It tells future preservationists what's been tried.

---

## Legal and Ethical Considerations

- **Preserving for historical/archival purposes** is generally treated differently from distributing for use.
- **Respect explicit author requests.** If an author has asked that their old work not be redistributed, note this in the entry and don't include the source.
- **Abandonware is a grey area.** For tools that were commercial or closed-source, inclusion here is done in good faith for preservation. If a rights holder objects, files will be removed and the entry will be updated to note their existence without the content.
- **Don't include tools that are still commercially sold.** Even old versions.
- This archive does not advocate for using these tools. Many target vulnerabilities that have long since been patched.