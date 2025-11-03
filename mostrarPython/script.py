import vlc
import os
import time

# crear player
player = vlc.Instance('--fullscreen').media_player_new()

# crear media
media0 = vlc.Instance().media_new('./../data/085.mp4')
media1 = vlc.Instance().media_new('./../data/097.mp4')

# asignar media al player
player.set_media(media0)

# reproducir media
try:
    player.play()
except Exception as e:
    print("Error al reproducir el video:", e)

# esperar a que termine la reproduccion
time.sleep(10)  # ajustar el tiempo segun la duracion del video

while player.is_playing():
    # nothing
    print("Reproduciendo...")
    time.sleep(1.0)

player = vlc.Instance('--fullscreen').media_player_new()
player.set_media(media1)

try:
    player.play()
except Exception as e:
    print("Error al reproducir el video:", e)


# # obtener directorio actual
# directorio_actual = os.getcwd()
# print("El directorio actual es:", directorio_actual)

# comandoPrefijo = "cvlc --fullscreen --no-sub-autodetect-file  --no-play-and-exit './../data/"
# comandoSufijo = ".mp4'"

# listaVideos = ["085", "097"]

# for video in listaVideos:
#     comando = comandoPrefijo + video + comandoSufijo
#     os.system(comando)

