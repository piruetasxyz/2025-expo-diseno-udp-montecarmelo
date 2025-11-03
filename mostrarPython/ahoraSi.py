# import vlc
import os
import time

# comandoPrefijo = "cvlc  --loop --fulscreen --no-sub-autodetect-file './../data/"
comandoPrefijo = "vlc --fullscreen --no-sub-autodetect-file --no-video-title-show --play-and-exit './../data/"
# comandoPrefijoLoop = "vlc --fullscreen --loop 5 --no-sub-autodetect-file --no-video-title-show --play-and-exit  './../data/"

comandoSufijo = ".mp4'"

listaVideos = ["placeholder", "085", "097"]
# Duraciones en segundos para cada video
listaVideosDuraciones = [5, 30, 57]

repeticionesMax = 5
repeticionesActual = 0

for video in range(len(listaVideos)):
    if video == 0:
        comando = comandoPrefijo + listaVideos[video] + comandoSufijo
        repeticionesActual += 1
        if (repeticionesActual >= repeticionesMax):
            break
    else:
        comando = comandoPrefijo + listaVideos[video] + comandoSufijo
    os.system(comando)
    time.sleep(listaVideosDuraciones[video])


# instancia = crearInstance()
# player = crearPlayer(instancia)

# while True:
#     print(instancia, player)

#     if player is None:
#         direccion = './../data/' + listaVideos[videoActual] + '.mp4'
#         media = crearMedia(direccion)
#         player = crearPlayer(instancia)

#         reproducirVideo(player, media)
#     else:
#         if player.is_playing() is False:
#             try: 
#                 player.stop()
#             except Exception as e:
#                 print("Error al detener el video:", e)
#             instancia = crearInstance()
#             player = None
#             videoActual = (videoActual + 1) % len(listaVideos)
