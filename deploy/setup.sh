#!/usr/bin/env bash
# Run on the existing memi.click server (Caddy + uv + memi user already set up).
# Usage: WEBHOOK_SECRET=xxxx bash setup.sh
set -euo pipefail

: "${WEBHOOK_SECRET:?Set WEBHOOK_SECRET (the GitHub webhook secret) before running}"

REPO=https://github.com/filias/memi-ml.git
APP_DIR=/opt/memi-ml

git clone "$REPO" "$APP_DIR"
chown -R memi:memi "$APP_DIR"

cd "$APP_DIR"
sudo -u memi uv sync

cp deploy/memi-ml.service /etc/systemd/system/memi-ml.service

echo "WEBHOOK_SECRET=${WEBHOOK_SECRET}" > /etc/memi-ml-webhook.env
chmod 600 /etc/memi-ml-webhook.env
cp deploy/memi-ml-webhook.service /etc/systemd/system/memi-ml-webhook.service

systemctl daemon-reload
systemctl enable --now memi-ml memi-ml-webhook

cat >> /etc/caddy/Caddyfile <<'EOF'

ml.memi.click {
    handle /deploy {
        reverse_proxy localhost:9009
    }
    handle {
        reverse_proxy localhost:8089
    }
}
EOF
systemctl reload caddy

echo ""
echo "Done."
echo "1. DNS A record for ml.memi.click -> this server."
echo "2. GitHub webhook at https://github.com/filias/memi-ml/settings/hooks"
echo "   URL: https://ml.memi.click/deploy   secret: \$WEBHOOK_SECRET   event: push"
