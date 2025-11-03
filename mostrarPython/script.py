import os

# obtener directorio actual
directorio_actual = os.getcwd()
print("El directorio actual es:", directorio_actual)

# abrir video con vlc
os.system("vlc --fullscreen --no-sub-autodetect-file './../data/085.mp4'")
