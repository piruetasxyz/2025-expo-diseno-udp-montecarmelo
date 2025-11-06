import RaspiPantalla


class RaspiPantallaGrande(RaspiPantalla.RaspiPantalla):
    def __init__(self, eje, numero):
        super().__init__(eje, numero)
        self.tamano = "grande"
        self.maximoPantallas = 4

    def mostrarEscena(self, escena):
        print(
            "pantalla grande, eje " +
            str(self.convertirComputadorHumano(self.eje)) +
            ", numero " + str(self.convertirComputadorHumano(self.numero)) +
            "de un maximo de " + str(self.maximoPantallas) +
            ", escena: " + str(self.convertirComputadorHumano(escena))
            )
