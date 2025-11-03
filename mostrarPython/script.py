import os

# obtener directorio actual
directorio_actual = os.getcwd()
print("El directorio actual es:", directorio_actual)

# abrir video con vlc
os.system("vlc --video-filter 'transform' --transform-type '270' './../data/085.mp4'")