import RaspiPantalla
from Direcciones import chicas
from Preguntas import preguntas, faltantes
import os
import random
import subprocess
import re


class RaspiPantallaChica(RaspiPantalla.RaspiPantalla):
    def __init__(self, eje, numero):
        super().__init__(eje, numero)
        self.tamano = "chica"
        self.maximoPantallas = 4

        # --------------------------
        # Detect monitors and positions
        # --------------------------
        self.monitores = self.detectar_monitores()
        print("Monitores detectados:", self.monitores)

        # Define geometry strings for MPV
        if len(self.monitores) >= 2:
            geom1 = self.monitores[0]["geometry"]
            geom2 = self.monitores[1]["geometry"]
        elif len(self.monitores) == 1:
            geom1 = self.monitores[0]["geometry"]
            geom2 = "1920x1080+1920+0"  # fallback for single display
        else:
            geom1 = "1920x1080+0+0"
            geom2 = "1920x1080+1920+0"

        # --------------------------
        # MPV base command prefixes
        # --------------------------
        self.comandoPrefijoPantalla1 = [
            "mpv", "--no-terminal", "--fs", "--no-border", "--quiet",
            f"--geometry={geom1}"
        ]
        self.comandoPrefijoPantalla2 = [
            "mpv", "--no-terminal", "--fs", "--no-border", "--quiet",
            f"--geometry={geom2}"
        ]

        self.carpeta_videos = os.path.join(os.path.dirname(__file__), "../respuestas/")
        self.comandoSufijo = ".mp4"

        # Set IP mapping
        if self.eje == 1:
            self.direccionIP = chicas["eje-1"][self.numero]
        elif self.eje == 2:
            self.direccionIP = chicas["eje-2"][self.numero]
        elif self.eje == 3:
            self.direccionIP = chicas["eje-3"][self.numero]

    # --------------------------
    # Detect connected monitors with geometry
    # --------------------------
    def detectar_monitores(self):
        """Detect connected monitors and their geometry using xrandr."""
        monitores = []
        try:
            salida = subprocess.check_output(["xrandr"]).decode("utf-8")
            # Example match: HDMI-1 connected 1920x1080+0+0
            patron = re.compile(r"(\S+) connected.*?(\d+)x(\d+)\+(\d+)\+(\d+)")
            for nombre, ancho, alto, x, y in patron.findall(salida):
                geometry = f"{ancho}x{alto}+{x}+{y}"
                monitores.append({
                    "nombre": nombre,
                    "x": int(x),
                    "y": int(y),
                    "ancho": int(ancho),
                    "alto": int(alto),
                    "geometry": geometry
                })
            if not monitores:
                # fallback in case xrandr fails
                monitores = [
                    {"nombre": "HDMI-1", "geometry": "1920x1080+0+0"},
                    {"nombre": "HDMI-2", "geometry": "1920x1080+1920+0"},
                ]
        except Exception as e:
            print("Error detectando monitores:", e)
            monitores = [
                {"nombre": "HDMI-1", "geometry": "1920x1080+0+0"},
                {"nombre": "HDMI-2", "geometry": "1920x1080+1920+0"},
            ]
        return monitores

    # --------------------------
    # OSC message handler
    # --------------------------
    def default_handler(self, address, *args):
        if address.startswith("/paraChicas/nuevaRespuesta"):
            print("Handler de chica")
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
                    # Launch MPV videos
                    # --------------------------
                    if numeroRespuesta1 and numeroRespuesta1 not in faltantes:
                        path1 = os.path.join(self.carpeta_videos, f"{numeroRespuesta1}{self.comandoSufijo}")
                        print("Pantalla 1 →", path1)
                        subprocess.Popen(self.comandoPrefijoPantalla1 + [path1])

                    if numeroRespuesta2 and numeroRespuesta2 not in faltantes:
                        path2 = os.path.join(self.carpeta_videos, f"{numeroRespuesta2}{self.comandoSufijo}")
                        print("Pantalla 2 →", path2)
                        subprocess.Popen(self.comandoPrefijoPantalla2 + [path2])

                elif self.eje == 2:
                    print(preguntas[args[0]]["respuestas"]["eje-2"])
                elif self.eje == 3:
                    print(preguntas[args[0]]["respuestas"]["eje-3"])

    # --------------------------
    # Utility
    # --------------------------
    def mostrarEscena(self, escena):
        print(
            f"Pantalla chica, eje {self.convertirComputadorHumano(self.eje)}, "
            f"numero {self.convertirComputadorHumano(self.numero)} "
            f"de un maximo de {self.maximoPantallas}, escena: "
            f"{self.convertirComputadorHumano(escena)}"
        )
