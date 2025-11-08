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
        # OLD VLC COMMANDS (kept for reference)
        # --------------------------
        # self.comandoPrefijo = "vlc --fullscreen --no-sub-autodetect-file --no-video-title-show --play-and-exit './../respuestas/"
        # self.comandoPrefijoPantalla1 = "vlc --video-x=0 --video-y=0 --no-one-instance --qt-minimal-view --no-sub-autodetect-file --no-video-title-show './../respuestas/"
        # self.comandoPrefijoPantalla2 = "vlc --video-x=1920 --video-y=0 --no-one-instance --qt-minimal-view --no-sub-autodetect-file --no-video-title-show './../respuestas/"

        # --------------------------
        # NEW MPV COMMANDS (dynamic geometry)
        # --------------------------
        # Detect connected displays and their positions
        self.monitores = self.detectar_monitores()
        print("Monitores detectados:", self.monitores)

        # Build command prefixes for each detected monitor
        # Default fallback geometry if only one monitor is found
        if len(self.monitores) >= 2:
            geom1 = f"{self.monitores[0]['x']}:{self.monitores[0]['y']}"
            geom2 = f"{self.monitores[1]['x']}:{self.monitores[1]['y']}"
        elif len(self.monitores) == 1:
            geom1 = "0:0"
            geom2 = "1920:0"
        else:
            geom1 = "0:0"
            geom2 = "1920:0"

        self.comandoPrefijoPantalla1 = [
            "mpv", "--no-terminal", "--fs", "--no-border", "--quiet", "--hwdec=auto",
            f"--geometry={geom1}"
        ]
        self.comandoPrefijoPantalla2 = [
            "mpv", "--no-terminal", "--fs", "--no-border", "--quiet", "--hwdec=auto",
            f"--geometry={geom2}"
        ]

        # Folder where the videos are stored
        self.carpeta_videos = os.path.join(os.path.dirname(__file__), "../respuestas/")
        self.comandoSufijo = ".mp4"

        # self.listaVideos = list(respuestas.keys())
        # print("lista respuestas:", self.listaVideos)
        # self.listaVideos = ["01"]

        print("recuperando ip")
        if self.eje == 1:
            print("aqui con eje 1")
            self.direccionIP = chicas["eje-1"][self.numero]
        elif self.eje == 2:
            print("aqui con eje 2")
            self.direccionIP = chicas["eje-2"][self.numero]
        elif self.eje == 3:
            print("aqui con eje 3")
            self.direccionIP = chicas["eje-3"][self.numero]

    # --------------------------
    # NEW HELPER FUNCTION: detect monitors via xrandr
    # --------------------------
    def detectar_monitores(self):
        """Parse xrandr output to get monitor names and positions."""
        monitores = []
        try:
            salida = subprocess.check_output(["xrandr"]).decode("utf-8").splitlines()
            for linea in salida:
                if " connected " in linea:
                    partes = linea.split()
                    nombre = partes[0]
                    for p in partes:
                        if "+" in p and "x" in p:
                            # Example: 1920x1080+0+0
                            res, x, y = p.replace("x", " ").replace("+", " ").split()
                            monitores.append({
                                "nombre": nombre,
                                "ancho": int(res),
                                "alto": int(x),
                                "x": int(y),
                                "y": int(partes[-1]) if partes[-1].isdigit() else 0
                            })
                            break
            # Fallback if parsing fails
            if not monitores:
                monitores = [{"nombre": "HDMI-1", "x": 0, "y": 0},
                             {"nombre": "HDMI-2", "x": 1920, "y": 0}]
        except Exception as e:
            print("Error detectando monitores:", e)
            monitores = [{"nombre": "HDMI-1", "x": 0, "y": 0},
                         {"nombre": "HDMI-2", "x": 1920, "y": 0}]
        return monitores

    def default_handler(self, address, *args):
        if address.startswith("/paraChicas/nuevaRespuesta"):
            print("soy handler de la chicaaa")
            if args is not None:
                print(preguntas[args[0]]["respuestas"])

                if self.eje == 1:
                    respuestas_eje = preguntas[args[0]]["respuestas"]["eje-1"]
                    if len(respuestas_eje) > 0:
                        numeroRespuesta1 = random.choice(respuestas_eje)
                        numeroRespuesta2 = random.choice(respuestas_eje)
                    else:
                        numeroRespuesta1 = None
                        numeroRespuesta2 = None

                    # --------------------------
                    # NEW MPV LAUNCH
                    # --------------------------
                    if numeroRespuesta1 and numeroRespuesta1 not in faltantes:
                        path1 = os.path.join(self.carpeta_videos, f"{numeroRespuesta1}{self.comandoSufijo}")
                        print("Pantalla 1 →", path1)
                        subprocess.Popen(self.comandoPrefijoPantalla1 + [path1])

                    if numeroRespuesta2 and numeroRespuesta2 not in faltantes:
                        path2 = os.path.join(self.carpeta_videos, f"{numeroRespuesta2}{self.comandoSufijo}")
                        print("Pantalla 2 →", path2)
                        subprocess.Popen(self.comandoPrefijoPantalla2 + [path2])

                    # --------------------------
                    # OLD VLC LOGIC (kept)
                    # --------------------------
                    # if (self.numeroRespuesta1 not in faltantes):
                    #     self.comandoPantalla1 = self.comandoPrefijoPantalla1 + str(self.numeroRespuesta1) + self.comandoSufijo
                    #     print("comandoPantalla1: " + self.comandoPantalla1)
                    # if (self.numeroRespuesta2 not in faltantes):
                    #     self.comandoPantalla2 = self.comandoPrefijoPantalla2 + str(self.numeroRespuesta2) + self.comandoSufijo
                    # if (self.comandoPantalla1 is not None):
                    #      p1 = subprocess.Popen(self.comandoPantalla1, shell=True)
                    # if (self.comandoPantalla2 is not None):
                    #      p2 = subprocess.Popen(self.comandoPantalla2, shell=True)

                elif self.eje == 2:
                    print(preguntas[args[0]]["respuestas"]["eje-2"])
                elif self.eje == 3:
                    print(preguntas[args[0]]["respuestas"]["eje-3"])

    def mostrarEscena(self, escena):
        print(
            "pantalla chica, eje " +
            str(self.convertirComputadorHumano(self.eje)) +
            ", numero " + str(self.convertirComputadorHumano(self.numero)) +
            " de un maximo de " + str(self.maximoPantallas) +
            ", escena: " + str(self.convertirComputadorHumano(escena))
        )
