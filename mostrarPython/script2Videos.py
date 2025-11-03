import vlc
import os
import time
import threading
import screeninfo

video_file_1 = './../data/085.mp4'
video_file_2 = './../data/097.mp4'

vlcs_args = None

def play_video_on_display(file_path, monitor_index, is_fullscreen=True):
    """
    reproduce un archivo de video especifico en un monitor determinado por su indice.
    """
    # obtenemos la lista de monitores disponibles
    monitors = get_monitors()
    if monitor_index >= len(monitors):
        print(f"error: el indice de monitor {monitor_index} no fue encontrado.")
        return

    monitor = monitors[monitor_index]
   
    # configuramos argumentos de vlc para posicionar la ventana en el monitor correcto
    # video-x y video-y definen la coordenada de inicio de la pantalla de destino
    vlc_args = [
        f'--video-x={monitor.x}',
        f'--video-y={monitor.y}',
        '--no-video-title-show', # opcional: oculta el titulo de la ventana
        '--embedded-video',      # opcional: previene que los controles se separen
    ]


play_video_on_display(file_path, monitor_index, is_fullscreen=True)


instance = vlc.Instance(vlc_args)
media = instance.media_new(file_path)
player = instance.media_player_new()
player.set_media(media)

player.play()

player.set_fullscreen(True)

thread1 = threading.Thread(target=play_video_on_display, args=(video_file_1, 0))
thread2 = threading.Thread(target=play_video_on_display, args=(video_file_2, 1))

thread1.start()
thread2.start()

thread1.join()
thread2.join()


# # obtener directorio actual
# directorio_actual = os.getcwd()
# print("El directorio actual es:", directorio_actual)

# comandoPrefijo = "cvlc --fullscreen --no-sub-autodetect-file  --no-play-and-exit './../data/"
# comandoSufijo = ".mp4'"

# listaVideos = ["085", "097"]

# for video in listaVideos:
#     comando = comandoPrefijo + video + comandoSufijo
#     os.system(comando)

