import RaspiPantalla


class RaspiPantallaGrande(RaspiPantalla.RaspiPantalla):
    def __init__(self, eje, numero):
        super().__init__(eje, numero)
        self.tamano = "grande"
