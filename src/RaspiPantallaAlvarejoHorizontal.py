import RaspiPantalla
from Direcciones import medianas
import os
import random


class RaspiPantallaAlvarejo(RaspiPantalla.RaspiPantalla):
    def __init__(self, eje, numero):
        super().__init__(eje, numero)
        self.tamano = "alvarejo"

        self.comandoPrefijo = "vlc --fullscreen --no-video-deco --qt-minimal-view --no-sub-autodetect-file --no-video-title-show --play-and-exit './../refrescos/01_arica_horizontal/"
        self.comandoSufijo = ".mov'"

        self.comando = self.comandoPrefijo + self.get_random_file("./refrescos/01_arica_horizontal/1_I_ARICA_HORIZONTAL") + self.comandoSufijo
        # print(self.comando)

        print("recuperando ip")

    # def handlerNuevaPregunta(self, address, *args):
    #     print("soy pantalla mediana y me pidieron nueva pregunta")

    def default_handler(self, address, *args):
        if (address.startswith("/paraMedianas/nuevaPregunta/")):
            print("soy handler de la medianaaa")
            if (args is not None):
                # print(args[0])

                # print(preguntas[args[0]]["archivo"])
                # print(type(args[2]))
                self.comando = self.comandoPrefijo + str(preguntas[args[0]]["archivo"]) + self.comandoSufijo
                os.system(self.comando)
            else:
                print("pucha os.system(self.comando) era None")
            print(f"DEFAULT {address}: {args}")

    def mostrarEscena(self, escena):
        print(
            "pantalla mediana, eje " +
            str(self.convertirComputadorHumano(self.eje)) +
            ", numero " + str(self.convertirComputadorHumano(self.numero)) +
            "de un maximo de " + str(self.maximoPantallas) +
            ", escena: " + str(self.convertirComputadorHumano(escena))
            )


