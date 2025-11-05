from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server
# from pythonosc.osc_server import BlockingOSCUDPServer


class RaspiPantalla:
    def __init__(self, eje, numero):
        self.eje = eje
        self.numero = numero
        self.tamano = None
        self.parser = None
        self.server = None
        self.dispatcher = None
        self.maximoPantallas = None

    def print_handler(self, unused_addr, args):
        print(f"{unused_addr}: {args}")

    def default_handler(self, address, *args):
        print(f"DEFAULT {address}: {args}")

    def print_compute_handler(self, unused_addr, args, volume):
        try:
            print("[{0}] ~ {1}".format(args[0], args[1](volume)))
        except ValueError:
            pass

    def handler(self):

        self.dispatcher = Dispatcher()
        self.dispatcher.map("/admin/bucle/*", self.print_handler)
        self.dispatcher.set_default_handler(self.default_handler)
        self.server = osc_server.ThreadingOSCUDPServer(
            ("10.30.123.87", 1234), self.dispatcher)
        self.server.serve_forever()  # Blocks forever

        # self.server = osc_server.ThreadingOSCUDPServer(
        #     ("127.0.0.1", 1234), self.dispatcher)
        # print("Serving on {}".format(self.server.server_address))
        # self.server.serve_forever()

    def mostrarEscena(self, escena):
        print("metodo no implementado en clase base")
    
    def convertirComputadorHumano(self, valor):
        return valor + 1
    
    def convertirHumanoComputador(self, valor):
        return valor - 1