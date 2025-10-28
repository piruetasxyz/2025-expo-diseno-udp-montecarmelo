import mpv
# from signal import pause
# import RPi.GPIO as GPIO
import time
import os

# use os to call terminal to play video with mpv
os.system("mpv --fullscreen --window-maximized --autofit=100% --loop ../gracias/gracias-cc-bloque-1.mp4") 

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
