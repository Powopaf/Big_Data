#!/bin/bash

APP_NAME="taxi"
INSTALL_DIR="/urs/local/bin"
SHARE_DIR="/usr/local/share/$APP_NAME"
SCRIPT_FILE="taxi.sh"
PYTHON_SCRIPT="main.py"

if [[ $EUID -ne 0 ]]; then
    echo "Please run as root: sudo ./install.sh"
    exit 1
fi
if ! command -v python3 &>/dev/null; then
    echo "Python3 is required but not install Please install first."
    exit 1
fi
mkdir -p "$SHARE_DIR"
cp "$PYTHON_FILE" "$SHARE_DIR/main.py"
cp "$SCRIPT_FILE" "$INSTALL_DIR/$SCRIPT_NAME"
chmod +x "$INSTALL_DIR/$SCRIPT_NAME"
sed -i "s|PYTHON_SCRIPT=.*|PYTHON_SCRIPT=\"$SHARE_DIR/main.py\"|" "$INSTALL_DIR/$SCRIPT_NAME"

echo "$SCRIPT_NAME installed successfully!"
echo "You can now use it by running $SCRIPT_NAME <graph> <years>"
