import RaspiPantalla
from Preguntas import preguntas
from Respuestas import respuestas
from Direcciones import chicas


class RaspiPantallaChica(RaspiPantalla.RaspiPantalla):
    def __init__(self, eje, numero):
        super().__init__(eje, numero)
        self.tamano = "chica"
        self.maximoPantallas = 4

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
        pass
        # print(f"DEFAULT {address}: {args}")

    def mostrarEscena(self, escena):
        print(
            "pantalla chica, eje " + 
            str(self.convertirComputadorHumano(self.eje)) +
            ", numero " + str(self.convertirComputadorHumano(self.numero)) +
            " de un maximo de " + str(self.maximoPantallas) +
            ", escena: " + str(self.convertirComputadorHumano(escena))
            )
