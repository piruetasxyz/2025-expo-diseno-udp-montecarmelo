import RaspiBase


class RaspiPantallaMediana(RaspiBase.RaspiBase):
    def __init__(self, eje, numero):
        super().__init__(eje, numero)
        super().tamano = "mediana"
