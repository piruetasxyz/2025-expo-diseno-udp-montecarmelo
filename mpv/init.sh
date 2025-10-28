#!/bin/bash
python -m venv env
cd home/discusiones04/2025-expo-diseno-udp-montecarmelo/mpv
activate() {
. /home/discusiones04/2025-expo-diseno-udp-montecarmelo/mpv/env/bin/activate
}
activate
which python
python script.py