import mpv
# from signal import pause
# import RPi.GPIO as GPIO
import time
import os
import sys

videosGracias = [
    "../gracias/gracias-cc-bloque-1.mp4",
    "../gracias/gracias-cc-bloque-2.mp4",
    "../gracias/gracias-cc-bloque-3.mp4",
    "../gracias/gracias-cc-bloque-4.mp4",
    "../gracias/gracias-cc-bloque-5.mp4",
    "../gracias/gracias-cc-bloque-6.mp4"
]

videoGraciasSeleccionado = videosGracias[sys.argv[1]]

# use os to call terminal to play video with mpv
os.system(f"mpv --fullscreen --window-maximized --autofit=100% --loop {videoGraciasSeleccionado}")

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
