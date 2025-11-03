# import vlc
import os
import time

# comandoPrefijo = "cvlc  --loop --fulscreen --no-sub-autodetect-file './../data/"
# comandoPrefijo = "vlc --fullscreen --no-sub-autodetect-file --no-video-title-show --play-and-exit './../data/"
comandoPrefijo = "vlc --fullscreen --no-sub-autodetect-file --no-video-title-show './../data/"

# comandoPrefijoLoop = "vlc --fullscreen --loop 5 --no-sub-autodetect-file --no-video-title-show --play-and-exit  './../data/"

comandoSufijo = ".mp4'"

listaVideos = ["placeholder", "085", "097"]
# Duraciones en segundos para cada video
listaVideosDuraciones = [5, 30, 57]

repeticionesMax = 5

for video in range(len(listaVideos)):
    if video == 0:
        for i in range(repeticionesMax):
            comando = comandoPrefijo + listaVideos[video] + comandoSufijo
            try:
                os.system(comando)
                time.sleep(listaVideosDuraciones[video])
            except Exception as e:
                print("Error al reproducir el video en bucle:", e)
    else:
        try:
            comando = comandoPrefijo + listaVideos[video] + comandoSufijo
            os.system(comando)
        except Exception as e:
            print("Error al reproducir el video:", e)

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
