# importar modulos de Python
import datetime
import random
# importar archivos del proyecto
from RaspiPrincipal import RaspiPrincipal
from RaspiPantallaChica import RaspiPantallaChica
from RaspiPantallaMediana import RaspiPantallaMediana
from RaspiPantallaGrande import RaspiPantallaGrande


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

        # pantallasChicas muestran respuestas
        self.comportamientoPantallasChicas = [
            ["minuto 0", "nada"],
            ["minuto 1", "quizasMostrar"],
            ["minuto 2", "quizasMostrar"],
            ["minuto 3", "quizasMostrar"],
            ["minuto 4", "quizasMostrar"],
            ["minuto 5", "quizasMostrar"],
            ["minuto 6", "quizasMostrar"],
            ["minuto 7", "quizasMostrar"],
            ["minuto 8", "quizasMostrar"],
            ["minuto 9", "quizasMostrar"],
            ["minuto 10", "quizasMostrar"],
            ["minuto 11", "quizasMostrar"],
            ["minuto 12", "quizasMostrar"],
            ["minuto 13", "quizasMostrar"],
            ["minuto 14", "quizasMostrar"],
            ["minuto 15", "quizasMostrar"],
            ["minuto 16", "quizasMostrar"],
            ["minuto 17", "quizasMostrar"],
            ["minuto 18", "quizasMostrar"],
            ["minuto 19", "quizasMostrar"],
            ["minuto 20", "quizasMostrar"],
            ["minuto 21", "quizasMostrar"],
            ["minuto 22", "quizasMostrar"],
            ["minuto 23", "quizasMostrar"],
            ["minuto 24", "quizasMostrar"],
            ["minuto 25", "quizasMostrar"],
            ["minuto 26", "quizasMostrar"],
            ["minuto 27", "quizasMostrar"],
            ["minuto 28", "quizasMostrar"],
            ["minuto 29", "quizasMostrar"],
            ["minuto 30", "quizasMostrar"],
            ["minuto 31", "quizasMostrar"],
            ["minuto 32", "quizasMostrar"],
            ["minuto 33", "quizasMostrar"],
            ["minuto 34", "quizasMostrar"],
            ["minuto 35", "quizasMostrar"],
            ["minuto 36", "quizasMostrar"],
            ["minuto 37", "quizasMostrar"],
            ["minuto 38", "quizasMostrar"],
            ["minuto 39", "quizasMostrar"],
            ["minuto 40", "quizasMostrar"],
            ["minuto 41", "quizasMostrar"],
            ["minuto 42", "quizasMostrar"],
            ["minuto 43", "quizasMostrar"],
            ["minuto 44", "quizasMostrar"],
            ["minuto 45", "quizasMostrar"],
            ["minuto 46", "quizasMostrar"],
            ["minuto 47", "quizasMostrar"],
            ["minuto 48", "quizasMostrar"],
            ["minuto 49", "quizasMostrar"],
            ["minuto 50", "quizasMostrar"],
            ["minuto 51", "quizasMostrar"],
            ["minuto 52", "quizasMostrar"],
            ["minuto 53", "quizasMostrar"],
            ["minuto 54", "quizasMostrar"],
            ["minuto 55", "quizasMostrar"],
            ["minuto 56", "quizasMostrar"],
            ["minuto 57", "quizasMostrar"],
            ["minuto 58", "quizasMostrar"],
            ["minuto 59", "quizasMostrar"]
        ]

        self.comportamientoPantallasMedianas = [
            ["minuto 0", "nada"],
            ["minuto 1", "quizasMostrar"],
            ["minuto 2", "quizasMostrar"],
            ["minuto 3", "quizasMostrar"],
            ["minuto 4", "quizasMostrar"],
            ["minuto 5", "quizasMostrar"],
            ["minuto 6", "quizasMostrar"],
            ["minuto 7", "quizasMostrar"],
            ["minuto 8", "quizasMostrar"],
            ["minuto 9", "quizasMostrar"],
            ["minuto 10", "quizasMostrar"],
            ["minuto 11", "quizasMostrar"],
            ["minuto 12", "quizasMostrar"],
            ["minuto 13", "quizasMostrar"],
            ["minuto 14", "quizasMostrar"],
            ["minuto 15", "quizasMostrar"],
            ["minuto 16", "quizasMostrar"],
            ["minuto 17", "quizasMostrar"],
            ["minuto 18", "quizasMostrar"],
            ["minuto 19", "quizasMostrar"],
            ["minuto 20", "quizasMostrar"],
            ["minuto 21", "quizasMostrar"],
            ["minuto 22", "quizasMostrar"],
            ["minuto 23", "quizasMostrar"],
            ["minuto 24", "quizasMostrar"],
            ["minuto 25", "quizasMostrar"],
            ["minuto 26", "quizasMostrar"],
            ["minuto 27", "quizasMostrar"],
            ["minuto 28", "quizasMostrar"],
            ["minuto 29", "quizasMostrar"],
            ["minuto 30", "quizasMostrar"],
            ["minuto 31", "quizasMostrar"],
            ["minuto 32", "quizasMostrar"],
            ["minuto 33", "quizasMostrar"],
            ["minuto 34", "quizasMostrar"],
            ["minuto 35", "quizasMostrar"],
            ["minuto 36", "quizasMostrar"],
            ["minuto 37", "quizasMostrar"],
            ["minuto 38", "quizasMostrar"],
            ["minuto 39", "quizasMostrar"],
            ["minuto 40", "quizasMostrar"],
            ["minuto 41", "quizasMostrar"],
            ["minuto 42", "quizasMostrar"],
            ["minuto 43", "quizasMostrar"],
            ["minuto 44", "quizasMostrar"],
            ["minuto 45", "quizasMostrar"],
            ["minuto 46", "quizasMostrar"],
            ["minuto 47", "quizasMostrar"],
            ["minuto 48", "quizasMostrar"],
            ["minuto 49", "quizasMostrar"],
            ["minuto 50", "quizasMostrar"],
            ["minuto 51", "quizasMostrar"],
            ["minuto 52", "quizasMostrar"],
            ["minuto 53", "quizasMostrar"],
            ["minuto 54", "quizasMostrar"],
            ["minuto 55", "quizasMostrar"],
            ["minuto 56", "quizasMostrar"],
            ["minuto 57", "quizasMostrar"],
            ["minuto 58", "quizasMostrar"],
            ["minuto 59", "quizasMostrar"]
        ]

        self.comportamientoPantallasGrandes = [
            ["minuto 0", "nada"],
            ["minuto 1", "quizasMostrar"],
            ["minuto 2", "quizasMostrar"],
            ["minuto 3", "quizasMostrar"],
            ["minuto 4", "quizasMostrar"],
            ["minuto 5", "quizasMostrar"],
            ["minuto 6", "quizasMostrar"],
            ["minuto 7", "quizasMostrar"],
            ["minuto 8", "quizasMostrar"],
            ["minuto 9", "quizasMostrar"],
            ["minuto 10", "quizasMostrar"],
            ["minuto 11", "quizasMostrar"],
            ["minuto 12", "quizasMostrar"],
            ["minuto 13", "quizasMostrar"],
            ["minuto 14", "quizasMostrar"],
            ["minuto 15", "quizasMostrar"],
            ["minuto 16", "quizasMostrar"],
            ["minuto 17", "quizasMostrar"],
            ["minuto 18", "quizasMostrar"],
            ["minuto 19", "quizasMostrar"],
            ["minuto 20", "quizasMostrar"],
            ["minuto 21", "quizasMostrar"],
            ["minuto 22", "quizasMostrar"],
            ["minuto 23", "quizasMostrar"],
            ["minuto 24", "quizasMostrar"],
            ["minuto 25", "quizasMostrar"],
            ["minuto 26", "quizasMostrar"],
            ["minuto 27", "quizasMostrar"],
            ["minuto 28", "quizasMostrar"],
            ["minuto 29", "quizasMostrar"],
            ["minuto 30", "quizasMostrar"],
            ["minuto 31", "quizasMostrar"],
            ["minuto 32", "quizasMostrar"],
            ["minuto 33", "quizasMostrar"],
            ["minuto 34", "quizasMostrar"],
            ["minuto 35", "quizasMostrar"],
            ["minuto 36", "quizasMostrar"],
            ["minuto 37", "quizasMostrar"],
            ["minuto 38", "quizasMostrar"],
            ["minuto 39", "quizasMostrar"],
            ["minuto 40", "quizasMostrar"],
            ["minuto 41", "quizasMostrar"],
            ["minuto 42", "quizasMostrar"],
            ["minuto 43", "quizasMostrar"],
            ["minuto 44", "quizasMostrar"],
            ["minuto 45", "quizasMostrar"],
            ["minuto 46", "quizasMostrar"],
            ["minuto 47", "quizasMostrar"],
            ["minuto 48", "quizasMostrar"],
            ["minuto 49", "quizasMostrar"],
            ["minuto 50", "quizasMostrar"],
            ["minuto 51", "quizasMostrar"],
            ["minuto 52", "quizasMostrar"],
            ["minuto 53", "quizasMostrar"],
            ["minuto 54", "quizasMostrar"],
            ["minuto 55", "quizasMostrar"],
            ["minuto 56", "quizasMostrar"],
            ["minuto 57", "quizasMostrar"],
            ["minuto 58", "quizasMostrar"],
            ["minuto 59", "quizasMostrar"]
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
