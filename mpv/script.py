import mpv
# from signal import pause
# import RPi.GPIO as GPIO
import time
import os
import sys

# ... your other code ...

videosGracias = [
    "../gracias/gracias-cc-bloque-1.mp4",
    "../gracias/gracias-cc-bloque-2.mp4",
    "../gracias/gracias-cc-bloque-3.mp4",
    "../gracias/gracias-cc-bloque-4.mp4",
    "../gracias/gracias-cc-bloque-5.mp4",
    "../gracias/gracias-cc-bloque-6.mp4"
]

# Set your desired rotation angle here (e.g., 90 for a vertical display)
rotation_value = 90  # Use 90, 180, or 270

videoGraciasSeleccionado = videosGracias[int(sys.argv[1])]

# The command line now includes the --rotate option
os.system(f"mpv --fullscreen --window-maximized --autofit=100% --loop --rotate={rotation_value} {videoGraciasSeleccionado}")

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# def my_callback():
#     print("Play!")
#     player.time_pos = 0

# GPIO.add_event_detect(8, GPIO.FALLING, callback=my_callback, bouncetime=300)


# player = mpv.MPV()
# player.fullscreen = False
# player.loop = True
# player.play('../gracias/gracias-cc-bloque-1.mp4')

# time.sleep(1)

# player.fullscreen = True
# player.wait_for_playback()
