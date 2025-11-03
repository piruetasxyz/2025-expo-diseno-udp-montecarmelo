import os

# obtener directorio actual
directorio_actual = os.getcwd()
print("El directorio actual es:", directorio_actual)

comandoPrefijo = "vlc --fullscreen --no-sub-autodetect-file --play-and-exit './../data/"
comandoSufijo = ".mp4"

listaVideos = ["085", "097"]

for video in listaVideos:
    comando = comandoPrefijo + video + comandoSufijo
    os.system(comando)


# # abrir video con vlc
# os.system("vlc --fullscreen --no-sub-autodetect-file --play-and-exit './../data/085.mp4'")
