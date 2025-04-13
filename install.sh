#!/bin/bash

SCRIPT_NAME="taxi"
INSTALL_DIR="/usr/local/bin"
SHARE_DIR="/usr/local/$SCRIPT_NAME"
SCRIPT_FILE="taxi.sh"
PYTHON_FILE="main.py"

if [[ $EUID -ne 0 ]]; then
    echo "Please run as root: sudo ./install.sh"
    exit 1
fi
if ! command -v python3 &>/dev/null; then
    echo "python3 is required bu not install"
    exit 1
fi
mkdir -p "$SHARE_DIR"
sudo touch "$SHARE_DIR/__init__.py"
cp "$PYTHON_FILE" "$SHARE_DIR/main.py"
cp "$SCRIPT_FILE" "$INSTALL_DIR/$SCRIPT_NAME"
chmod +x "$INSTALL_DIR/$SCRIPT_NAME"
sed -i "s|PYTHON_FILE=.*|PYTHON_FILE=\"$SHARE_DIR/main.py\"|" "$INSTALL_DIR/$SCRIPT_NAME"
echo "$SCRIPT_NAME installed!"
