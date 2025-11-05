import RaspiPantalla


class RaspiPantallaMediana(RaspiPantalla.RaspiPantalla):
    def __init__(self, eje, numero):
        super().__init__(eje, numero)
        self.tamano = "mediana"
        self.maximoPantallas = 2

    def mostrarEscena(self, escena):
        print(
            "pantalla chica, eje " + str(self.convertirComputadorHumano(self.eje)) +
            ", numero " + str(self.convertirComputadorHumano(self.numero)) +
            "de un maximo de " + str(self.maximoPantallas) +
            ", escena: " + str(self.convertirComputadorHumano(escena))
            )
