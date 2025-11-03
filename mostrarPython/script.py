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
player.play()

# esperar a que termine la reproduccion
time.sleep(10)  # ajustar el tiempo segun la duracion del video

while player.is_playing():
    # nothing
    print("Reproduciendo...")
    # time.sleep(1)

player.set_media(media1)
player.play()



# # obtener directorio actual
# directorio_actual = os.getcwd()
# print("El directorio actual es:", directorio_actual)

# comandoPrefijo = "cvlc --fullscreen --no-sub-autodetect-file  --no-play-and-exit './../data/"
# comandoSufijo = ".mp4'"

# listaVideos = ["085", "097"]

# for video in listaVideos:
#     comando = comandoPrefijo + video + comandoSufijo
#     os.system(comando)

