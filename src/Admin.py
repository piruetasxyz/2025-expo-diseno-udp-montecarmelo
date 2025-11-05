from RaspiPrincipal import RaspiPrincipal

import time


class Admin:
    def __init__(self):
        self.nombre = "admin"
        self.corriendo = False
        self.cliente = None

    def iniciar(self):
        self.corriendo = True
        print("admin iniciado")

    def detener(self):
        self.corriendo = False
        print("admin detenido")

    def crearCliente(self, port):
        print("tratando de crear cliente")
        self.cliente = RaspiPrincipal(port)
        print("cliente creado")
        self.cliente.enviarMensajeATodos("/admin/init", 1)

    def buclear(self):
        self.iniciar()
        while self.corriendo:
            self.cliente.enviarMensajeATodos("/admin/bucle", 1)
            time.sleep(5)
        self.detener()
