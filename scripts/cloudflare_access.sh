#!/usr/bin/env bash
# One-time: lock the dashboard's Cloudflare Pages site to the PM's email with Cloudflare Access. Idempotent.
# Needs CLOUDFLARE_API_TOKEN (Pages:Edit, Access Apps and Policies:Edit) and CLOUDFLARE_ACCOUNT_ID. Prints no secrets.
set -euo pipefail
: "${CLOUDFLARE_API_TOKEN:?}" "${CLOUDFLARE_ACCOUNT_ID:?}"
HOST="${DASHBOARD_HOST:-socialus-plan-dashboard.pages.dev}"
EMAIL="${DASHBOARD_EMAIL:-mrlafranchi@gmail.com}"
API="https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/access/apps"
H=(-H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" -H "Content-Type: application/json")
existing=$(curl -fsS "${H[@]}" "$API" | jq -r --arg d "$HOST" '.result[]? | select(.domain==$d) | .id' | head -1)
body=$(jq -n --arg d "$HOST" --arg e "$EMAIL" '{name:"SocialUs dashboard",domain:$d,type:"self_hosted",session_duration:"168h",
  self_hosted_domains:[$d,("*."+$d)],
  policies:[{name:"PM only",decision:"allow",include:[{email:{email:$e}}]}]}')
if [ -n "$existing" ]; then curl -fsS -X PUT "${H[@]}" "$API/$existing" -d "$body" >/dev/null; echo "Access app updated."
else curl -fsS -X POST "${H[@]}" "$API" -d "$body" >/dev/null; echo "Access app created."; fi
