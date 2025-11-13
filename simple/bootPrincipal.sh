#!/bin/bash

# sleep for a while
sleep 30

# Set the desktop color to black
pcmanfm --set-wallpaper-mode color --set-wallpaper '#000000'

# CONFIGURATION
WIFI_NAME="TP-Link_A9A4"
TARGET_DIR="$HOME/2025-expo-diseno-udp-montecarmelo/simple"
PYTHON_SCRIPT="main.py"
TERMINAL_CMD="lxterminal"

# --- Wait until connected to the correct WiFi ---
echo "Waiting to connect to WiFi: $WIFI_NAME ..."
while true; do
    CURRENT_WIFI=$(iwgetid -r)
    if [ "$CURRENT_WIFI" == "$WIFI_NAME" ]; then
        echo "success, connected to $WIFI_NAME!"
        break
    else
        echo "Currently connected to: $CURRENT_WIFI. Retrying in 5 seconds..."
        sleep 5
    fi
done

# --- Open a new terminal and run commands inside it ---
$TERMINAL_CMD -e "bash -c '
    echo Connected. Starting update...
    cd \"$TARGET_DIR\" || exit 1
    echo Pulling latest changes from git...
    git pull

    echo Running Python script...
    source env/bin/activate
    python3 \"$PYTHON_SCRIPT\"

    echo Done.
    exec bash
'"