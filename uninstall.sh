#!/bin/bash

INSTALL_DIR="/usr/local/bin/taxi"
SHARE_DIR="/urs/local/share/taxi"

if [[ $EUID -ne 0 ]]; then
    echo "Please run as root: sudo ./uninstall.sh"
    exit 1
fi
rm -f "$INSTALL_DIR"
rm -rf "$SHARE_DIR"

echo "taxi command uninstalled successfully"
