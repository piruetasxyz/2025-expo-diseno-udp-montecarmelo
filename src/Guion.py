
class Guion:
    def __init__(self, nombre):
        self.comportamientoRaspisPantallaChica = []
        self.comportamientoRaspisPantallaMediana = []
        self.comportamientoRaspisPantallaGrande = []

        self.nombre = nombre
        self.pasos = []

    def agregarPaso(self, paso):
        self.pasos.append(paso)
