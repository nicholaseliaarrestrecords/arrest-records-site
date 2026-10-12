#!/usr/bin/env bash
# One manual production deploy of ./public to Netlify (no Git link, no build step).
set -euo pipefail
cd "$(dirname "$0")/.."
. scripts/_env.sh                      # sets NETLIFY_AUTH_TOKEN (Arrest Records only)
python3 -I src/build.py
SITE_ID=22c99773-f9ec-4161-abed-f7bcaaecd5a5   # Netlify project: arrest-records-site
netlify deploy --prod --dir=public --site="$SITE_ID" --no-build
