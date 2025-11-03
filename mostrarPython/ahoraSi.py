# import vlc
import os
import time

# comandoPrefijo = "cvlc  --loop --fulscreen --no-sub-autodetect-file './../data/"
comandoPrefijo = "vlc --fullscreen --no-sub-autodetect-file --play-and-exit './../data/"
comandoPrefijoLoop = "vlc --fullscreen --no-sub-autodetect-file --play-and-exit --loop './../data/"

comandoSufijo = ".mp4'"

listaVideos = ["placeholder", "085", "097"]

repeticionesMax = 5
repeticionesActual = 0

for video in range(len(listaVideos)):
    if video == 0:
        comando = comandoPrefijoLoop + listaVideos[video] + comandoSufijo
        repeticionesActual += 1
        if (repeticionesActual >= repeticionesMax):
            os.system("pkill vlc")
    else:
        comando = comandoPrefijo + listaVideos[video] + comandoSufijo
    os.system(comando)


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
