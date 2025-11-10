#!/usr/bin/env bash
# vlc_on_screen.sh — Play one video fullscreen on a chosen monitor (Raspberry Pi / Linux, X11)
# Usage: ./vlc_on_screen.sh <path/to/video> <screen_number>
# Notes:
#  - screen_number is 1-based, in the order reported by `xrandr --listactivemonitors`
#  - requires X11 (not Wayland) for precise window placement

set -euo pipefail

usage() {
  echo "Usage: $0 <video_file> <screen_number>"
  echo "Example: $0 /home/pi/movie.mp4 2"
  exit 1
}

[[ $# -eq 2 ]] || usage

VID="$1"
SCR_NUM="$2"

[[ -f "$VID" ]] || { echo "Error: '$VID' not found."; exit 2; }
[[ "$SCR_NUM" =~ ^[0-9]+$ ]] || { echo "Error: screen_number must be an integer (1..N)."; exit 2; }
(( SCR_NUM >= 1 )) || { echo "Error: screen_number must be >= 1."; exit 2; }

# Ensure we talk to the active X session (handy if launched via SSH)
: "${DISPLAY:=:0}"
export DISPLAY
if [[ -z "${XAUTHORITY:-}" ]]; then
  for cand in "/home/pi/.Xauthority" "$HOME/.Xauthority"; do
    [[ -r "$cand" ]] && export XAUTHORITY="$cand" && break
  done
fi

# Tools check
command -v xrandr >/dev/null 2>&1 || {
  echo "Error: xrandr is required. Install: sudo apt-get install x11-xserver-utils"
  exit 3
}
VLC_BIN="cvlc"
command -v "$VLC_BIN" >/dev/null 2>&1 || VLC_BIN="vlc"
command -v "$VLC_BIN" >/dev/null 2>&1 || {
  echo "Error: VLC not found. Install: sudo apt-get install vlc"
  exit 3
}

# Get active monitors
mapfile -t MONS < <(xrandr --listactivemonitors | tail -n +2)
MON_COUNT=${#MONS[@]}
(( MON_COUNT >= 1 )) || { echo "No active monitors found."; exit 4; }
(( SCR_NUM <= MON_COUNT )) || {
  echo "Error: requested screen $SCR_NUM but only $MON_COUNT active monitor(s) detected."
  xrandr --listactivemonitors
  exit 4
}

# Parse "WxH+X+Y" from the chosen monitor line
parse_geom() {
  # Example line:
  # ' 0: +*HDMI-1 1920/520x1080/290+0+0  HDMI-1'
  sed -E 's/.* ([0-9]+)\/[0-9]+x([0-9]+)\/[0-9]+\+([0-9]+)\+([0-9]+).*/\1 \2 \3 \4/'
}

TARGET_LINE="${MONS[$((SCR_NUM-1))]}"
read W H X Y <<<"$(parse_geom <<<"$TARGET_LINE")"

# Launch VLC on that monitor in its own instance
# Key opts:
#  --no-one-instance      allow multiple vlc instances
#  --no-video-title-show  hide OSD banner
#  --no-embedded-video    separate window (lets us position it)
#  --video-x/--video-y    place on chosen monitor
#  --width/--height       hint size (then fullscreen)
#  --fullscreen           fill that monitor
"$VLC_BIN" \
  --no-one-instance \
  --no-video-title-show \
  --no-embedded-video \
  --quiet \
  --video-x "$X" --video-y "$Y" --width "$W" --height "$H" \
  --fullscreen \
  --play-and-exit \
  -- "$VID"
