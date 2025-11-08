import RaspiPantalla
from Direcciones import chicas
from Preguntas import preguntas, faltantes
# from Respuestas import respuestas
import os
import random
import subprocess


class RaspiPantallaChica(RaspiPantalla.RaspiPantalla):
    def __init__(self, eje, numero):
        super().__init__(eje, numero)
        self.tamano = "chica"
        self.maximoPantallas = 4

        # --------------------------
        # OLD CODE (commented out — now ignored)
        # --------------------------
        # self.comandoPrefijo = "vlc --fullscreen --no-sub-autodetect-file --no-video-title-show --play-and-exit './../respuestas/"
        # self.comandoPrefijoPantalla1 = "vlc --no-one-instance --qt-fullscreen-screennumber='2' --qt-minimal-view   --no-sub-autodetect-file --no-video-title-show --play-and-exit './../respuestas/"
        # self.comandoPrefijoPantalla2 = "vlc --no-one-instance --qt-fullscreen-screennumber='7' --qt-minimal-view   --no-sub-autodetect-file --no-video-title-show --play-and-exit './../respuestas/"
        # self.comandoPrefijoPantalla1 = "vlc --video-x=0--video-y=0  --qt-minimal-view   --no-sub-autodetect-file --no-video-title-show --play-and-exit './../respuestas/"
        # self.comandoPrefijoPantalla2 = "vlc --video-x=0 --video-y=3000 --qt-minimal-view   --no-sub-autodetect-file --no-video-title-show --play-and-exit './../respuestas/"
        # self.comandoPrefijoPantalla1 = "vlc --video-x=0 --video-y=0 --no-one-instance --qt-minimal-view --no-sub-autodetect-file --no-video-title-show './../respuestas/"
        # self.comandoPrefijoPantalla2 = "vlc --video-x=0 --video-y=3000 --no-one-instance --qt-minimal-view --no-sub-autodetect-file --no-video-title-show  './../respuestas/"

        # --------------------------
        # NEW: clean, safe VLC commands as lists
        # --------------------------
        self.comandoPrefijoPantalla1 = [
            "vlc", "--no-one-instance", "--no-playlist-enqueue",
            "--qt-minimal-view", "--no-sub-autodetect-file",
            "--no-video-title-show", "--fullscreen",
            "--video-x=0", "--video-y=0"
        ]

        self.comandoPrefijoPantalla2 = [
            "vlc", "--no-one-instance", "--no-playlist-enqueue",
            "--qt-minimal-view", "--no-sub-autodetect-file",
            "--no-video-title-show", "--fullscreen",
            "--video-x=1920", "--video-y=0"  # adjust for your second monitor
        ]

        # Folder and suffix for videos
        self.carpeta_videos = os.path.join(os.path.dirname(__file__), "../respuestas/")
        self.comandoSufijo = ".mp4"

        # self.listaVideos = list(respuestas.keys())
        # print("lista respuestas:", self.listaVideos)
        # self.listaVideos = ["01"]

        self.comandoPantalla1 = None
        self.comandoPantalla2 = None
        self.numeroRespuesta1 = None
        self.numeroRespuesta2 = None

        # self.comando = self.comandoPrefijo + str(self.listaVideos[0].archivo) + self.comandoSufijo
        # print(self.comando)

        print("recuperando ip")
        if (self.eje == 1):
            print("aqui con eje 1")
            self.direccionIP = chicas["eje-1"][self.numero]
        elif (self.eje == 2):
            print("aqui con eje 2")
            self.direccionIP = chicas["eje-2"][self.numero]
        elif (self.eje == 3):
            print("aqui con eje 3")
            self.direccionIP = chicas["eje-3"][self.numero]


    def default_handler(self, address, *args):
        if (address.startswith("/paraChicas/nuevaRespuesta")):
            print("soy handler de la chicaaa")
            if (args is not None):
                print(preguntas[args[0]]["respuestas"])
                if (self.eje == 1):
                    if len(preguntas[args[0]]["respuestas"]["eje-1"]) > 0:
                        self.numeroRespuesta1 = preguntas[args[0]]["respuestas"]["eje-1"][random.randint(0, len(preguntas[args[0]]["respuestas"]["eje-1"]) - 1)]
                        self.numeroRespuesta2 = preguntas[args[0]]["respuestas"]["eje-1"][random.randint(0, len(preguntas[args[0]]["respuestas"]["eje-1"]) - 1)]
                    else:
                        self.numeroRespuesta1 = None
                        self.numeroRespuesta2 = None

                    # if len(preguntas[args[0]]["respuestas"]["eje-1"]) > 1:
                    #     self.numeroRespuesta2 = preguntas[args[0]]["respuestas"]["eje-1"][1]
                    # else:
                    #     self.numeroRespuesta2 = None

                    # --------------------------
                    # NEW: build file paths and run VLC subprocesses
                    # --------------------------
                    if (self.numeroRespuesta1 not in faltantes):
                        path1 = os.path.join(self.carpeta_videos, f"{self.numeroRespuesta1}{self.comandoSufijo}")
                        print("Pantalla 1 →", path1)
                        subprocess.Popen(self.comandoPrefijoPantalla1 + [path1])
                    if (self.numeroRespuesta2 not in faltantes):
                        path2 = os.path.join(self.carpeta_videos, f"{self.numeroRespuesta2}{self.comandoSufijo}")
                        print("Pantalla 2 →", path2)
                        subprocess.Popen(self.comandoPrefijoPantalla2 + [path2])

                    # --------------------------
                    # OLD: os.system / string commands (commented out)
                    # --------------------------
                    # if (self.numeroRespuesta1 not in faltantes):
                    #     self.comandoPantalla1 = self.comandoPrefijoPantalla1 + str(self.numeroRespuesta1) + self.comandoSufijo
                    #     print("comandoPantalla1: " + self.comandoPantalla1)
                    # else:
                    #     self.comandoPantalla1 = None
                    # if (self.numeroRespuesta2 not in faltantes):
                    #     self.comandoPantalla2 = self.comandoPrefijoPantalla2 + str(self.numeroRespuesta2) + self.comandoSufijo
                    #     print("comandoPantalla2: " + self.comandoPantalla2)
                    # else:
                    #     self.comandoPantalla2 = None
                    # if (self.comandoPantalla1 is not None):
                    #      p1 = subprocess.Popen(self.comandoPantalla1, shell=True)
                    # if (self.comandoPantalla2 is not None):
                    #      p2 = subprocess.Popen(self.comandoPantalla2, shell=True)

                elif (self.eje == 2):
                    print(preguntas[args[0]]["respuestas"]["eje-2"])
                elif (self.eje == 3):
                    print(preguntas[args[0]]["respuestas"]["eje-3"])


    def mostrarEscena(self, escena):
        print(
            "pantalla chica, eje " + 
            str(self.convertirComputadorHumano(self.eje)) +
            ", numero " + str(self.convertirComputadorHumano(self.numero)) +
            " de un maximo de " + str(self.maximoPantallas) +
            ", escena: " + str(self.convertirComputadorHumano(escena))
        )
