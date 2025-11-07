# importar modulos de Python
import datetime
import random
# importar archivos del proyecto
from RaspiPrincipal import RaspiPrincipal
from RaspiPantallaChica import RaspiPantallaChica
from RaspiPantallaMediana import RaspiPantallaMediana
from RaspiPantallaGrande import RaspiPantallaGrande
import Guion
from Preguntas import preguntas


class Admin:
    def __init__(self):
        self.nombre = "admin"
        self.corriendo = False
        self.cliente = None
        self.ahora = datetime.datetime.now().time()
        # ahora
        self.ahoraH = self.ahora.hour
        self.ahoraM = self.ahora.minute
        self.ahoraS = self.ahora.second
        # antes
        self.antesH = self.ahoraH
        self.antesM = self.ahoraM
        self.antesS = self.ahoraS
        self.mensajesEnviados = []
        self.raspi = None
        self.puertoPrincipalEnviar = 1234
        self.puertoPantallasRecibir = 1234
        self.corriendo = True

        # cada X minutos cambia la pregunta
        self.mEntrePreguntas = 1
        self.mUltimaPregunta = self.ahoraM
        self.preguntaActual = random.randint(1, len(preguntas))
        self.preguntaAnterior = None

        # las respuestas
        self.listaRespuestas = preguntas[self.preguntaActual]["respuestas"]
        self.respuestaActual = None
        self.respuestaAnterior = None

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

        self.refresco = [
            "desierto",
            "cielo",
            "bosque",
        ]

    def calcularSiNuevaPregunta(self):
        if (self.ahoraM - self.mUltimaPregunta) >= self.mEntrePreguntas:
            
            return True
        else:
            return False

    def nuevaPregunta(self):
        # elegir nueva pregunta aleatoria
        if (self.raspi.__class__.__name__ == "RaspiPrincipal"):
            self.mUltimaPregunta = self.ahoraM
            self.preguntaAnterior = self.preguntaActual
            self.preguntaActual = random.randint(1, len(preguntas))
            self.raspi.enviarMensajeNuevaPregunta(self.preguntaActual)
            self.raspi.enviarMensajeNuevaRespuesta(self.preguntaActual)

    # def nuevaRespuesta(self):
    #     # elegir nueva respuesta aleatoria
    #     if (self.raspi.__class__.__name__ == "RaspiPrincipal"):
    #         self.raspi.enviarMensajeNuevaRespuesta(self.preguntaActual, self.respuestaActual)

    def detener(self):
        self.corriendo = False
        print("admin detenido")

    def mostrarPantallasChicas(self):
        pass

    def actualizarTiempo(self):
        # actualizar ahora
        self.ahora = datetime.datetime.now().time()
        # guardar ahora en anterior
        self.antesH = self.ahoraH
        self.antesM = self.ahoraM
        self.antesS = self.ahoraS
        # actualizar ahora
        self.ahoraH = self.ahora.hour
        self.ahoraM = self.ahora.minute
        self.ahoraS = self.ahora.second

    def detectarHoraCambio(self):
        if self.ahoraH != self.antesH:
            return True
        else:
            return False

    def detectarMinutoCambio(self):
        if self.ahoraM != self.antesM:
            return True
        else:
            return False

    def buclear(self):
        print(self.raspi.__class__.__name__)
        while self.corriendo:
            self.actualizarTiempo()
            if self.detectarMinutoCambio():
                print("nuevo minuto: " + str(self.ahoraM))
                print(self.raspi.direccionIP)
                if (self.raspi.__class__.__name__ == "RaspiPrincipal"):
                    if (self.calcularSiNuevaPregunta()):
                        self.nuevaPregunta()
                # self.raspi.mostrar()
            if self.detectarHoraCambio():
                print("nueva hora: " + str(self.ahoraH))
            # self.cliente.enviarMensajeATodos("/admin/bucle", 1)
        # self.detener()

    def crearPrincipal(self):
        self.raspi = RaspiPrincipal(self.puertoPrincipalEnviar)
        self.buclear()

    def crearChica(self, eje, numero):
        self.raspi = RaspiPantallaChica(eje, numero)
        self.raspi.handler()
        self.buclear()

    def crearMediana(self, eje, numero):
        self.raspi = RaspiPantallaMediana(eje, numero)
        self.raspi.handler()
        self.buclear()

    def crearGrande(self, eje, numero):
        self.raspi = RaspiPantallaGrande(eje, numero)
        self.raspi.handler()
        self.buclear()
