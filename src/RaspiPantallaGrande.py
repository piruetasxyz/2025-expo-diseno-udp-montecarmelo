import RaspiPantalla
from Direcciones import grandes
from Preguntas import preguntas
import os


class RaspiPantallaGrande(RaspiPantalla.RaspiPantalla):
    def __init__(self, eje, numero):
        super().__init__(eje, numero)
        self.tamano = "grande"
        self.maximoPantallas = 4

        self.comandoPrefijo = "vlc --fullscreen --no-video-deco --qt-minimal-view --no-sub-autodetect-file --no-video-title-show --play-and-exit './../generativas/horizontal-1-arica/"
        self.comandoSufijo = ".mov'"

        print("recuperando ip")
        if (self.eje == 1):
            print("aqui en eje 1")
            self.direccionIP = grandes["eje-1"][self.numero]
        elif (self.eje == 2):
            print("aqui en eje 2")
            self.direccionIP = grandes["eje-2"][self.numero]
        elif (self.eje == 3):
            print("aqui en eje 3")
            self.direccionIP = grandes["eje-3"][self.numero]

    def default_handler(self, address, *args):
        if (address.startswith("/paraGrandes/generativas/")):
            print("soy handler de la grande")
            self.comando = self.comandoPrefijo + str(0) + self.comandoSufijo
            os.system(self.comando)
        else:
            print("pucha os.system(self.comando) era None")

    def mostrarEscena(self, escena):
        print(
            "pantalla grande, eje " +
            str(self.convertirComputadorHumano(self.eje)) +
            ", numero " + str(self.convertirComputadorHumano(self.numero)) +
            "de un maximo de " + str(self.maximoPantallas) +
            ", escena: " + str(self.convertirComputadorHumano(escena))
            )
