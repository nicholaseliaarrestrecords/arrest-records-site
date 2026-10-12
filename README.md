# Arrest Records — arrest-records.com

Static site migrated from GoDaddy Website Builder (Oct 12, 2026). Only `public/` is ever deployed.

- **GitHub** (`nicholaseliaarrestrecords/arrest-records-site`): record of our work only.
  NOT connected to Netlify. Never link it (pushes would trigger builds and use credits).
- **Netlify** project `arrest-records-site` (site ID `22c99773-f9ec-4161-abed-f7bcaaecd5a5`):
  deployed by hand, one upload per release, no build step.

## Edit
- Page content: `src/blocks/<page>-1.html` (main block), `-0` (marquee), `-2` (footer).
- Shared layout, nav, cookie banner: `src/build.py`. Styles/JS: `public/style.css`, `public/site.js`.
- Images: `public/images/` (originals live in `Static & Gold/` in the parent folder).
- Regenerate pages: `python3 -I src/build.py` (the `public/*.html` files are generated).
- Check numbers against the YouTube channel (@ArrestRecords) before each update.

## Deploy (Claude, via the Arrest Records Chrome profile; no tokens needed)
1. `scripts/make-zip.sh` builds `~/Desktop/arrest-records-site.zip` from `public/`.
2. Upload the zip at https://app.netlify.com/projects/arrest-records-site/deploys.
   (Optional: `scripts/deploy.sh` does the same via CLI if `NETLIFY_AUTH_TOKEN` is in
   `~/.config/arrest-records/env`.)

## Record
Commit locally, then upload changed files at
https://github.com/nicholaseliaarrestrecords/arrest-records-site/upload/main/<folder>
(or `scripts/push.sh` if `GITHUB_TOKEN` is set in the same env file).
