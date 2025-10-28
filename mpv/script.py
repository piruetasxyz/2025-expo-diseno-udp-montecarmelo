import mpv
# from signal import pause
# import RPi.GPIO as GPIO
import time

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def my_callback():
    print("Play!")
    player.time_pos = 0

# GPIO.add_event_detect(8, GPIO.FALLING, callback=my_callback, bouncetime=300)


player = mpv.MPV()
player.fullscreen = False
player.loop = True
player.play('video.mp4')

time.sleep(1)

player.fullscreen = True
player.wait_for_playback()
