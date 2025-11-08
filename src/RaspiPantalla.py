from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server
import os

# from pythonosc.osc_server import BlockingOSCUDPServer
# from Direcciones import chicas, medianas, grandes


class RaspiPantalla:
    def __init__(self, eje, numero):
        self.eje = int(eje)
        self.numero = int(numero)
        self.tamano = None
        self.parser = None
        self.server = None
        self.dispatcher = None
        self.maximoPantallas = None
        self.corriendo = True
        self.direccionIP = None

        self.comandoPrefijo = None
        self.comandoSufijo = None
        self.comando = None
        self.listaVideos = None

        # probabilidades
        self.probChicas = 0.8
        # self.probMedianas = 0.3
        self.probGrandes = 0.2

    # def handlerNuevaPregunta(self, address, *args):
    #     pass
    #     # print("soy handler nueva pregunta")
    #     # print(f"DEFAULT {address}: {args}")

    # def handlerNuevaRespuesta(self, address, *args):
    #     pass
    #     # print("soy handler nueva respuesta")
    #     # print(f"DEFAULT {address}: {args}")

    # def buclear(self):
    #     pass

    def print_handler(self, unused_addr, args):
        print(f"{unused_addr}: {args}")

    def default_handler(self, address, *args):
        pass

    def print_compute_handler(self, unused_addr, args, volume):
        try:
            print("[{0}] ~ {1}".format(args[0], args[1](volume)))
        except ValueError:
            pass

    def handler(self):

        self.dispatcher = Dispatcher()

        self.dispatcher.set_default_handler(self.default_handler)
        self.server = osc_server.ThreadingOSCUDPServer(
            (self.direccionIP,
             1234), self.dispatcher)
        self.server.serve_forever()  # Blocks forever

        # self.server = osc_server.ThreadingOSCUDPServer(
        #     ("127.0.0.1", 1234), self.dispatcher)
        # print("Serving on {}".format(self.server.server_address))
        # self.server.serve_forever()

    def mostrar(self):
        print("metodo no implementado en clase base")

    def convertirComputadorHumano(self, valor):
        return valor + 1

    def convertirHumanoComputador(self, valor):
        return valor - 1
