import RaspiPantalla
import Preguntas


class RaspiPantallaMediana(RaspiPantalla.RaspiPantalla):
    def __init__(self, eje, numero):
        super().__init__(eje, numero)
        self.tamano = "mediana"
        self.maximoPantallas = 2

    def mostrarEscena(self, escena):
        print(
            "pantalla mediana, eje " +
            str(self.convertirComputadorHumano(self.eje)) +
            ", numero " + str(self.convertirComputadorHumano(self.numero)) +
            "de un maximo de " + str(self.maximoPantallas) +
            ", escena: " + str(self.convertirComputadorHumano(escena))
            )
    
    def mostrarPregunta(self, pregunta, eje):
        self.pregunta = Preguntas.preguntas.get(pregunta, "pucha")
        print(self.pregunta)

    def mostrarRespuestas(self, pregunta, eje):
        self.pregunta = Preguntas.preguntas.get(pregunta, "pucha")
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
