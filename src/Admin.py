class Admin:
    def __init__(self):
        self.nombre = "admin"
        self.corriendo = False

    def iniciar(self):
        self.corriendo = True
        print("admin iniciado")

    def detener(self):
        self.corriendo = False
        print("admin detenido")


