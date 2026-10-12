#!/usr/bin/env bash
# Fallback when the CLI is not logged in: zips ./public to drag into
# https://app.netlify.com/projects/arrest-records-site/deploys
set -euo pipefail
cd "$(dirname "$0")/../public"
python3 -I ../src/build.py
rm -f ~/Desktop/arrest-records-site.zip
zip -qr ~/Desktop/arrest-records-site.zip . -x '.DS_Store'
echo "Wrote ~/Desktop/arrest-records-site.zip"
