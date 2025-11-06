# importar modulos de Python
import datetime
import random
# importar archivos del proyecto
from RaspiPrincipal import RaspiPrincipal
from RaspiPantallaChica import RaspiPantallaChica
from RaspiPantallaMediana import RaspiPantallaMediana
from RaspiPantallaGrande import RaspiPantallaGrande
import Guion


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
        self.raspi = None
        self.puertoPrincipalEnviar = 1234
        self.puertoPantallasRecibir = 1234
        self.corriendo = True

        # guion
        self.comportamientoRaspisPantallaChica = []
        self.comportamientoRaspisPantallaMediana = []
        self.comportamientoRaspisPantallaGrande = []

        # probabilidades
        self.probabilidadMostrarPantallasChicas = 0.5
        self.probabilidadMostrarPantallasMedianas = 0.3
        self.probabilidadMostrarPantallasGrandes = 0.2

        # configuracion del sistema
        self.servidores = []
        self.numeroPantallasChicas = 10

        self.comportamientos = [
            "negro",
            "mostrarPregunta",
            "mostrarRefresco",
        ]

        self.preguntas = [
            "¿Te gusta el arte?",
            "¿Cuál es tu color favorito?",
            "¿Prefieres el mar o la montaña?",
        ]

        self.respuestas = [
            "respuesta 1",
            "2,",
            "3",

        ]

        self.refresco = [
            "desierto",
            "cielo",
            "bosque",
        ]


    def detener(self):
        self.corriendo = False
        print("admin detenido")

    def mostrarPantallasChicas(self):
        pass

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
        print(self.raspi.__class__.__name__)
        while self.corriendo:
            self.actualizarTiempo()
            if self.detectarMinutoCambio():
                print("nuevo minuto: " + str(self.ahoraMinuto))

            if self.detectarHoraCambio():
                print("nueva hora: " + str(self.ahoraHora))
            # self.cliente.enviarMensajeATodos("/admin/bucle", 1)
        # self.detener()

    def crearPrincipal(self):
        self.raspi = RaspiPrincipal(self.puertoPrincipalEnviar)
        self.buclear()

    def crearChica(self, eje, numero):
        self.raspi = RaspiPantallaChica(eje, numero)
        self.buclear()

    def crearMediana(self, eje, numero):
        self.raspi = RaspiPantallaMediana(eje, numero)
        self.buclear()

    def crearGrande(self, eje, numero):
        self.raspi = RaspiPantallaGrande(eje, numero)
        self.buclear()
