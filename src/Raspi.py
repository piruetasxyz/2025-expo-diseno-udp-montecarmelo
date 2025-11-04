
class Raspi:
    def __init__(self, eje, numero):
        self.nombre = "Raspberry Pi"
        self.eje = eje
        self.numero = numero
        self.conectado = False

    def conectar(self):
        print("tratando de conectar")