# import vlc
import os
import time

comandoPrefijo = "cvlc --fullscreen --loop --no-sub-autodetect-file './../data/"
comandoSufijo = ".mp4'"

listaVideos = ["085", "097"]

for video in listaVideos:
    comando = comandoPrefijo + video + comandoSufijo
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
