#!/usr/bin/env bash
#
# Sync selected Obsidian course folders into Quartz's content/ directory.
#
# Each course becomes one collapsible folder in the site's explorer:
#
#   content/
#     <Course A>/ wiki/ outputs/ raw/
#     <Course B>/ wiki/ outputs/ raw/
#     Global Wiki/        <- referenced global concept pages (auto-pulled)
#
# Only the courses in COURSES and the folders in PUBLISH ever leave the machine.
# EXCLUDE_FILES are dropped from every course (e.g. the private study map).
# Re-run this whenever you want the website to reflect new vault changes.
#
set -euo pipefail

VAULT="/Users/maxwernz/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian_Vault"
SITE="$(cd "$(dirname "$0")" && pwd)"
DEST="$SITE/content"

# --- What to publish -----------------------------------------------------------
# Add more course folder names (as they appear under Classes/) to share more.
COURSES=("Understanding LLMs" "Neuropsychology")
# Subfolders of each course to publish. (outputs is intentionally NOT published;
# only the images that wiki pages actually embed get pulled in, see below.)
PUBLISH=(wiki raw)
# Files never published, in any course (matched by name anywhere in the tree).
EXCLUDE_FILES=("Course Study Map.md")

# --- Reset content (keep .gitkeep) so vault deletions propagate cleanly --------
find "$DEST" -mindepth 1 ! -name '.gitkeep' -delete 2>/dev/null || true
mkdir -p "$DEST"

# Build the rsync --exclude args for per-file exclusions.
EXCLUDE_ARGS=(--exclude '.DS_Store' --exclude '.obsidian/' --exclude 'scripts/')
for f in "${EXCLUDE_FILES[@]}"; do
  EXCLUDE_ARGS+=(--exclude "$f")
done

# --- Copy each course ----------------------------------------------------------
for course in "${COURSES[@]}"; do
  cdir="$VAULT/Classes/$course"
  if [ ! -d "$cdir" ]; then
    echo "skip    course '$course' (not found)"
    continue
  fi
  for folder in "${PUBLISH[@]}"; do
    src="$cdir/$folder"
    [ -d "$src" ] || continue
    if [ "$folder" = "wiki" ]; then
      # Dissolve the wiki/ level: its children (concepts/, source notes/) land
      # directly under the course, so they show without a redundant "wiki" node.
      target="$DEST/$course"
    else
      target="$DEST/$course/$folder"
    fi
    mkdir -p "$target"
    rsync -a "${EXCLUDE_ARGS[@]}" "$src/" "$target/"
  done
  echo "synced  $course/"

  # Per-course landing page (so clicking the course shows an overview).
  {
    echo "---"
    echo "title: $course"
    echo "---"
    echo ""
    echo "Study wiki for **$course**."
    echo ""
    echo "- [[$course/concepts|Concepts]] — concept explanations"
    echo "- [[$course/source notes|Source notes]] — per-lecture notes"
    echo "- [[$course/Source Material|Source Material]] — original lecture slides & papers"
  } > "$DEST/$course/index.md"

  # raw/ holds only PDFs (assets, no markdown), so it stays invisible in the
  # explorer. Generate a single "Source Material" PAGE one level up that links
  # to each file — a clickable page instead of an empty dropdown folder.
  rawdir="$DEST/$course/raw"
  if [ -d "$rawdir" ]; then
    {
      echo "---"
      echo "title: Source Material"
      echo "---"
      echo ""
      echo "Original lecture slides and papers for this course. Click a title to"
      echo "open it in your browser."
      echo ""
      # List every raw file (pdf, docx, …). Links point into the raw/ subfolder.
      find "$rawdir" -maxdepth 1 -type f ! -name '.*' \
        | sort | while read -r f; do
          name="$(basename "$f")"
          stem="${name%.*}"
          enc="raw/${name// /%20}"        # encode spaces; page is one level up
          echo "- [$stem]($enc)"
        done
    } > "$DEST/$course/Source Material.md"
  fi
done

# --- Site homepage: list of courses -------------------------------------------
{
  echo "---"
  echo "title: Study Wiki"
  echo "---"
  echo ""
  echo "A study wiki (M.Sc. Cognitive Science, University of Tübingen)."
  echo ""
  echo "Use the **search** or the **explorer** sidebar. Courses:"
  echo ""
  for course in "${COURSES[@]}"; do
    [ -d "$DEST/$course" ] && echo "- [[$course/index|$course]]"
  done
} > "$DEST/index.md"

# --- Pull in referenced Global Wiki pages so cross-links resolve ---------------
python3 "$SITE/sync-referenced.py" "$VAULT" "$DEST"

echo ""
echo "Done. Preview with:  cd \"$SITE\" && npx quartz build --serve"
