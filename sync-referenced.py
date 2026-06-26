#!/usr/bin/env python3
"""
Pull referenced pages and media into the Quartz content tree.

Called by sync-content.sh after the course wiki/raw folders are copied. For the
published pages it resolves two kinds of references and copies in just what they
actually use, so nothing breaks even though whole folders (outputs/) are not
published:

1. Global Wiki pages — any `[[link]]` that points to a page under the vault's
   `Global Wiki/` is copied into a top-level `Global Wiki/` folder (and its own
   links are followed too). Only Global Wiki files are added; links to other
   courses' local pages are never followed, so nothing else leaks in.

2. Embedded media — images/videos that wiki pages embed (e.g. via
   `![](../../outputs/images/...png)` or `![[clip.mp4]]`) are copied to the
   path the link expects. Only the referenced files come along, not the rest of
   outputs/, and since no markdown lands in outputs/ it stays invisible in the
   explorer.

Usage: sync-referenced.py <vault_path> <content_dest>
"""
import os
import re
import sys
import shutil
import urllib.parse

EXCLUDE_NAMES = {"Course Study Map.md"}
MEDIA_EXT = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp",
             ".pdf", ".mp4", ".mov", ".webm", ".m4v"}

WIKILINK = re.compile(r"(!?)\[\[([^\]\n]+?)\]\]")          # [[x]] and ![[x]]
MDLINK = re.compile(r"!?\[[^\]]*\]\(<?([^)>]+?)>?\)")      # [t](p) and ![a](p)


def norm(target):
    """Strip alias/heading, decode, and tidy a link target."""
    target = target.split("|")[0].split("#")[0].strip()
    target = urllib.parse.unquote(target)
    return target.strip()


def index_dir(root):
    """Map every lookup key a link might use -> absolute file path (lowercased)."""
    idx = {}

    def add(key, path):
        idx.setdefault(key.lower(), path)

    for dp, _, files in os.walk(root):
        for fn in files:
            if fn.startswith("."):
                continue
            full = os.path.join(dp, fn)
            rel = os.path.relpath(full, root)
            stem = os.path.splitext(fn)[0]
            add(fn, full)
            add(stem, full)
            add(rel, full)
            add(os.path.splitext(rel)[0], full)
    return idx


def main():
    vault, dest = sys.argv[1], sys.argv[2]
    gw_root = os.path.join(vault, "Global Wiki")
    gw_idx = index_dir(gw_root) if os.path.isdir(gw_root) else {}
    gw_out = os.path.join(dest, "Global Wiki")

    media_idx_cache = {}  # workspace path -> basename index

    def origin_of(content_file):
        """Vault file a synced content file was copied from (for relative links).

        Handles the dissolved wiki/ level: a content file at <course>/concepts/X
        came from Classes/<course>/wiki/concepts/X.
        """
        rel = os.path.relpath(content_file, dest)
        parts = rel.split(os.sep)
        candidates = [
            os.path.join(vault, "Classes", rel),                      # <course>/...
            os.path.join(vault, rel),                                 # Global Wiki/...
        ]
        if len(parts) > 1:                                            # re-insert wiki/
            with_wiki = os.path.join(parts[0], "wiki", *parts[1:])
            candidates.append(os.path.join(vault, "Classes", with_wiki))
        for cand in candidates:
            if os.path.isfile(cand):
                return cand
        return None

    def workspace_of(content_file):
        """(workspace dir in vault, prefix under content) for a content file."""
        rel = os.path.relpath(content_file, dest)
        seg0 = rel.split(os.sep)[0]
        if seg0 == "Global Wiki":
            return os.path.join(vault, "Global Wiki"), "Global Wiki"
        return os.path.join(vault, "Classes", seg0), seg0

    def copy_in(src, target):
        if os.path.abspath(target).startswith(os.path.abspath(dest)) \
                and not os.path.exists(target):
            os.makedirs(os.path.dirname(target), exist_ok=True)
            shutil.copy2(src, target)
            return True
        return False

    queue = []
    for dp, _, files in os.walk(dest):
        for fn in files:
            if fn.endswith(".md"):
                queue.append(os.path.join(dp, fn))

    pages_added = 0
    media_added = 0
    seen_pages = set()

    while queue:
        path = queue.pop()
        try:
            text = open(path, encoding="utf-8").read()
        except (OSError, UnicodeDecodeError):
            continue

        origin = origin_of(path)
        ws_root, ws_prefix = workspace_of(path)

        # --- 1. Global Wiki page references --------------------------------
        for bang, raw in WIKILINK.findall(text):
            key = norm(raw)
            ext = os.path.splitext(key)[1].lower()
            if ext in MEDIA_EXT:
                continue  # handled as media below
            src = gw_idx.get(key.lower())
            if not src or src in seen_pages:
                continue
            if os.path.basename(src) in EXCLUDE_NAMES:
                continue
            rel = os.path.relpath(src, gw_root)
            target = os.path.join(gw_out, rel)
            if copy_in(src, target):
                seen_pages.add(src)
                if src.endswith(".md"):
                    pages_added += 1
                    queue.append(target)

        # --- 2a. Embedded media via relative markdown links ----------------
        if origin:
            for raw in MDLINK.findall(text):
                if "://" in raw:
                    continue
                p = norm(raw)
                if os.path.splitext(p)[1].lower() not in MEDIA_EXT:
                    continue
                src = os.path.normpath(os.path.join(os.path.dirname(origin), p))
                if os.path.isfile(src):
                    target = os.path.normpath(
                        os.path.join(os.path.dirname(path), p))
                    if copy_in(src, target):
                        media_added += 1

        # --- 2b. Embedded media via ![[basename.ext]] ----------------------
        for bang, raw in WIKILINK.findall(text):
            name = norm(raw)
            if os.path.splitext(name)[1].lower() not in MEDIA_EXT:
                continue
            if ws_root not in media_idx_cache:
                media_idx_cache[ws_root] = (
                    index_dir(ws_root) if os.path.isdir(ws_root) else {})
            src = media_idx_cache[ws_root].get(name.lower())
            if src and os.path.isfile(src):
                rel = os.path.relpath(src, ws_root)
                target = os.path.join(dest, ws_prefix, rel)
                if copy_in(src, target):
                    media_added += 1

    print(f"synced  references ({pages_added} Global Wiki pages, "
          f"{media_added} embedded media files)")


if __name__ == "__main__":
    main()
