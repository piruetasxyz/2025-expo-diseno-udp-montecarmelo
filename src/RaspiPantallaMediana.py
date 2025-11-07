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

        self.comandoPrefijo = "vlc --fullscreen --no-sub-autodetect-file --no-video-title-show --play-and-exit './../preguntas/"
        # self.comandoSufijo = ".mp4'"
        self.comandoSufijo = ".jpg'"
        self.listaVideos = list(preguntas.keys())
        print(self.listaVideos)
        # self.listaVideos = ["pregunta-01"]

        self.comando = self.comandoPrefijo + str(self.listaVideos[0]) + self.comandoSufijo
        print(self.comando)

        print("recuperando ip")
        if (self.eje == 1):
            print("aqui con eje 1")
            self.direccionIP = medianas["eje-1"][self.numero]
        elif (self.eje == 2):
            print("aqui con eje 2")
            self.direccionIP = medianas["eje-2"][self.numero]
        elif (self.eje == 3):
            print("aqui con eje 3")
            self.direccionIP = medianas["eje-3"][self.numero]

    def default_handler(self, address, *args):
        pass
        print("soy handler de la medianaaa")
        if (self.comando is not None):
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

    def mostrarRespuestas(self, pregunta, eje):
        # self.pregunta = Preguntas.preguntas.get(pregunta, "pucha")
        if (eje == 1):
            print("respuestas eje-1:")
        for respuesta in self.pregunta["respuestas"]["eje-1"]:
            if respuesta != 0:
                print(respuesta + ", ")
        print("posibles respuestas eje-2:")
        for respuesta in self.pregunta["respuestas"]["eje-2"]:
            if respuesta != 0:
                print(respuesta + ", ")
        print("posibles respuestas eje-3:")
        for respuesta in self.pregunta["respuestas"]["eje-3"]:
            if respuesta != 0:
                print(respuesta + ", ")
