import RaspiPantalla
from Direcciones import chicas
from Preguntas import preguntas
from Respuestas import respuestas
import os


class RaspiPantallaChica(RaspiPantalla.RaspiPantalla):
    def __init__(self, eje, numero):
        super().__init__(eje, numero)
        self.tamano = "chica"
        self.maximoPantallas = 4

        self.comandoPrefijo = "vlc --fullscreen --no-sub-autodetect-file --no-video-title-show --play-and-exit './../respuestas/"
        self.comandoSufijo = ".mp4'"
        self.listaVideos = list(respuestas.keys())
        print("lista respuestas:", self.listaVideos)
        # self.listaVideos = ["01"]

        # self.comando = self.comandoPrefijo + str(self.listaVideos[0].archivo) + self.comandoSufijo
        print(self.comando)

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
        print("soy handler de la chicaaa")
        if (args is not None):
            print(preguntas[args[0]]["respuestas"])
            if (self.eje == 1):
                print(preguntas[args[0]]["respuestas"]["eje-1"])
            elif (self.eje == 2):
                print(preguntas[args[0]]["respuestas"]["eje-2"])
            elif (self.eje == 3):
                print(preguntas[args[0]]["respuestas"]["eje-3"])
            # self.comando = self.comandoPrefijo + str(respuestas[args[0]]["archivo"]) + self.comandoSufijo
            # os.system(self.comando)
        # else:
        #     print("pucha os.system(self.comando) era None")
        # print(f"DEFAULT {address}: {args}")

    def mostrarEscena(self, escena):
        print(
            "pantalla chica, eje " + 
            str(self.convertirComputadorHumano(self.eje)) +
            ", numero " + str(self.convertirComputadorHumano(self.numero)) +
            " de un maximo de " + str(self.maximoPantallas) +
            ", escena: " + str(self.convertirComputadorHumano(escena))
            )
