import mpv
import time
import os
import sys

# List of videos
videosGracias = [
    "../gracias/gracias-cc-bloque-1.mp4",
    "../gracias/gracias-cc-bloque-2.mp4",
    "../gracias/gracias-cc-bloque-3.mp4",
    "../gracias/gracias-cc-bloque-4.mp4",
    "../gracias/gracias-cc-bloque-5.mp4",
    "../gracias/gracias-cc-bloque-6.mp4"
]

# Set your desired rotation angle here (e.g., 90 for a vertical display)
rotation_value = 90  # Can be 90, 180, or 270

# Ensure the argument is provided and valid
if len(sys.argv) < 2:
    print("Please provide an index for the video selection (e.g., python script.py 0).")
    sys.exit(1)

index = int(sys.argv[1])

# Validate that the index is within the range of the list
if index < 0 or index >= len(videosGracias):
    print(f"Invalid index. Please choose a number between 0 and {len(videosGracias)-1}.")
    sys.exit(1)

# Select the video based on the index
videoGraciasSeleccionado = videosGracias[index]

# Run the video using mpv with rotation
os.system(f"mpv --fullscreen --window-maximized --autofit=100% --loop --video-rotate={rotation_value} {videoGraciasSeleccionado}")

# If you want to do something with GPIO or further logic, you can add it here
# Example (currently commented out):
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
