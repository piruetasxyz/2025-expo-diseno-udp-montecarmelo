#!/usr/bin/env bash
# dual_vlc_preguntas.sh — Play two videos on two different displays with two VLC instances (Raspberry Pi / Linux, X11)

set -euo pipefail

usage() {
  echo "Usage: $0 <video_for_screen_1> <video_for_screen_2>"
  exit 1
}

[[ $# -eq 2 ]] || usage

VID1="$1"
VID2="$2"

[[ -f "$VID1" ]] || { echo "Error: '$VID1' not found."; exit 2; }
[[ -f "$VID2" ]] || { echo "Error: '$VID2' not found."; exit 2; }

# Ensure we can talk to the local X session (useful if launched via SSH)
: "${DISPLAY:=:0}"
export DISPLAY
if [[ -z "${XAUTHORITY:-}" ]]; then
  # Try common locations (adjust user if needed)
  for cand in "/home/pi/.Xauthority" "$HOME/.Xauthority"; do
    [[ -r "$cand" ]] && export XAUTHORITY="$cand" && break
  done
fi

# Need xrandr to detect monitor geometries
if ! command -v xrandr >/dev/null 2>&1; then
  echo "Error: xrandr is required. Install with: sudo apt-get install x11-xserver-utils"
  exit 3
fi

# Parse monitor geometries from xrandr --listactivemonitors
# Example line: ' 0: +*HDMI-1 1920/520x1080/290+0+0  HDMI-1'
readarray -t MONS < <(xrandr --listactivemonitors | tail -n +2)

if [[ ${#MONS[@]} -lt 2 ]]; then
  echo "Error: fewer than 2 active monitors detected."
  xrandr --listactivemonitors
  exit 4
fi

parse_geom() {
  # Extract WxH+X+Y
  # shellcheck disable=SC2001
  local line="$1"
  local geom
  geom=$(sed -E 's/.* ([0-9]+)\/[0-9]+x([0-9]+)\/[0-9]+\+([0-9]+)\+([0-9]+).*/\1 \2 \3 \4/' <<<"$line")
  echo "$geom"
}

read W1 H1 X1 Y1 <<<"$(parse_geom "${MONS[0]}")"
read W2 H2 X2 Y2 <<<"$(parse_geom "${MONS[1]}")"

# Choose vlc (GUI suppressed) for clean video-only windows
# You can swap cvlc->vlc if you prefer, options are identical here.
VLC_BIN="cvlc"

# Common options:
#  --no-video-title-show : hide OSD filename banner
#  --no-embedded-video   : force separate video window (lets us position it)
#  --fullscreen          : go fullscreen on the screen where the window is placed
#  --video-x/--video-y   : initial window position (top-left of the target monitor)
#  --width/--height      : initial size (helps some WMs choose the right screen)
#  --no-one-instance     : allow multiple instances
COMMON_OPTS_0=(
  --no-video-title-show
  --no-embedded-video
  --no-one-instance
  --quiet
)

COMMON_OPTS_1=(
  --no-video-title-show
  --no-embedded-video
  --no-one-instance
  --quiet
  --no-audio  
)

# Launch first video on monitor 1
"$VLC_BIN" "${COMMON_OPTS_0[@]}" \
  --video-x "$X1" --video-y "$Y1" --width "$W1" --height "$H1" \
  --fullscreen \
  --play-and-exit \
  --video-filter=transform --transform-type=0
  -- "$VID1" &

PID1=$!

# Launch second video on monitor 2
"$VLC_BIN" "${COMMON_OPTS_1[@]}" \
  --video-x "$X2" --video-y "$Y2" --width "$W2" --height "$H2" \
  --fullscreen \
  --play-and-exit \
  --video-filter=transform --transform-type=0
  -- "$VID2" &

PID2=$!

echo "Launched VLC instances: $PID1 (screen 1), $PID2 (screen 2)."
wait $PID1 $PID2
