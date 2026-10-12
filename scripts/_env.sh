# Loads Arrest Records tokens from a private file outside the repo.
ENV_FILE="$HOME/.config/arrest-records/env"
[ -f "$ENV_FILE" ] || { echo "Missing $ENV_FILE (see README: Tokens)"; exit 1; }
set -a; . "$ENV_FILE"; set +a
