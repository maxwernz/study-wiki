#!/usr/bin/env bash
#
# One command to push vault changes to the live site.
#
#   ./publish.sh                 # sync + commit + push (auto message)
#   ./publish.sh "added X notes"  # ... with your own commit message
#
# It re-syncs the selected vault folders into the site, commits the result, and
# pushes. The push triggers the GitHub Actions deploy (~1.5 min), after which the
# changes are live at https://maxwernz.github.io/cogsci-wiki/.
#
set -euo pipefail
cd "$(dirname "$0")"

echo "1/3  Syncing vault → site ..."
bash sync-content.sh

echo ""
echo "2/3  Committing ..."
git add -A
if git diff --cached --quiet; then
  echo "     No changes since last publish — nothing to do."
  exit 0
fi
msg="${1:-Update content ($(date +%Y-%m-%d))}"
git commit -q -m "$msg"

echo "3/3  Pushing (triggers deploy) ..."
git push -q

echo ""
echo "Done. Deploy is running — live in ~1-2 min at:"
echo "  https://maxwernz.github.io/cogsci-wiki/"
echo "Watch it with:  gh run watch --repo maxwernz/cogsci-wiki"
