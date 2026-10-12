#!/usr/bin/env bash
# Push to the Arrest Records GitHub repo using its own token (not the gh login).
set -euo pipefail
cd "$(dirname "$0")/.."
. scripts/_env.sh                      # sets GITHUB_TOKEN (this repo only)
git push "https://x-access-token:${GITHUB_TOKEN}@github.com/nicholaseliaarrestrecords/arrest-records-site.git" main
git fetch -q origin
