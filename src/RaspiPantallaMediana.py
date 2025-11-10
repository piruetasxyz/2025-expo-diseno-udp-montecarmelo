import RaspiPantalla
from Direcciones import medianas
from Preguntas import preguntas
import os


class RaspiPantallaMediana(RaspiPantalla.RaspiPantalla):
    def __init__(self, eje, numero):
        super().__init__(eje, numero)
        self.tamano = "mediana"
        self.maximoPantallas = 2

        self.preguntaActual = preguntas.get(1)
        self.preguntaAnterior = None

        self.comandoPrefijo = "vlc --fullscreen --no-video-deco --qt-minimal-view --no-sub-autodetect-file --no-video-title-show --play-and-exit './../preguntas/"
        self.comandoSufijo = ".mp4'"
        self.listaVideos = list(preguntas.keys())
        print(self.listaVideos)

        self.comando = self.comandoPrefijo + str(preguntas[self.listaVideos[0]]["archivo"]) + self.comandoSufijo
        # print(self.comando)

        print("recuperando ip")
        tmpeje = "eje-"+str(self.eje)
        # if (self.eje == 1):
        print("aqui en eje 1")
        self.direccionIP = medianas[tmpeje][self.numero]

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

    def mostrar(self, preguntaActual=None):
        self.mostrarPregunta(preguntaActual, self.eje)

    def mostrarPregunta(self, pregunta, eje):
        os.system(self.comando)
        print(self.preguntaActual["texto"])

