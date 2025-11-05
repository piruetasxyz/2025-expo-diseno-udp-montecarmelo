from RaspiPrincipal import RaspiPrincipal

import time
import datetime


class Admin:
    def __init__(self):
        self.nombre = "admin"
        self.corriendo = False
        self.cliente = None
        self.ahora = datetime.datetime.now().time()
        # ahora
        self.ahoraHora = self.ahora.hour
        self.ahoraMinuto = self.ahora.minute
        self.ahoraSegundo = self.ahora.second
        # antes
        self.antesHora = self.ahoraHora
        self.antesMinuto = self.ahoraMinuto
        self.antesSegundo = self.ahoraSegundo
        self.mensajesEnviados = []

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

    def actualizarTiempo(self):
        # actualizar ahora
        self.ahora = datetime.datetime.now().time()
        # guardar ahora en anterior
        self.antesHora = self.ahoraHora
        self.antesMinuto = self.ahoraMinuto
        self.antesSegundo = self.ahoraSegundo
        # actualizar ahora
        self.ahoraHora = self.ahora.hour
        self.ahoraMinuto = self.ahora.minute
        self.ahoraSegundo = self.ahora.second

    def detectarHoraCambio(self):
        if self.ahoraHora != self.antesHora:
            return True
        else:
            return False
        
    def detectarMinutoCambio(self):
        if self.ahoraMinuto != self.antesMinuto:
            return True
        else:
            return False
        
    

    def buclear(self):
        self.iniciar()
        while self.corriendo:
            self.actualizarTiempo()
            if self.detectarMinutoCambio():
                print("ojo cambio el minuto")

            if self.detectarHoraCambio():
                print("ojo cambio la hora")
            self.cliente.enviarMensajeATodos("/admin/bucle", 1)
        # self.detener()
