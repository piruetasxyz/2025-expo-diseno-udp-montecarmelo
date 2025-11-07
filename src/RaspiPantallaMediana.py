import RaspiPantalla
from Preguntas import preguntas
from Direcciones import medianas


class RaspiPantallaMediana(RaspiPantalla.RaspiPantalla):
    def __init__(self, eje, numero):
        super().__init__(eje, numero)
        self.tamano = "mediana"
        self.maximoPantallas = 2
       
        self.preguntaActual = preguntas.get(1)
        self.preguntaAnterior = None
        
        # print("recuperando ip")
        if (self.eje == 1):
            # print("aqui con eje 1")
            self.direccionIP = medianas["eje-1"][self.numero]
        elif (self.eje == 2):
            # print("aqui con eje 2")
            self.direccionIP = medianas["eje-2"][self.numero]
        elif (self.eje == 3):
            # print("aqui con eje 3")
            self.direccionIP = medianas["eje-3"][self.numero]
    
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
