#!/usr/bin/env bash
set -euo pipefail

if [[ $EUID -ne 0 ]]; then
  echo "Please run with sudo: sudo $0"
  exit 1
fi

SERVICE_NAME="leetcode-qa-client.service"
SOURCE_FILE="/home/jingyi/PycharmProjects/leetcode-qa/client/leetcode-qa-client.service"
TARGET_FILE="/etc/systemd/system/${SERVICE_NAME}"

cp "${SOURCE_FILE}" "${TARGET_FILE}"
systemctl daemon-reload
systemctl enable "${SERVICE_NAME}"
systemctl restart "${SERVICE_NAME}"

echo "Installed and enabled ${SERVICE_NAME}"
systemctl status --no-pager "${SERVICE_NAME}" | sed -n '1,12p'
