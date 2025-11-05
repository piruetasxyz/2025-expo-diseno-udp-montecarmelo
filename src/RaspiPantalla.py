import math

from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server


class RaspiPantalla:
    def __init__(self, eje, numero):
        self.eje = eje
        self.numero = numero
        self.tamano = None
        self.parser = None
        self.server = None
        self.dispatcher = None

    def print_volume_handler(self, unused_addr, args, volume):
        print("[{0}] ~ {1}".format(args[0], volume))

    def print_compute_handler(self, unused_addr, args, volume):
        try:
            print("[{0}] ~ {1}".format(args[0], args[1](volume)))
        except ValueError:
            pass

    def handler(self):
        # self.parser = argparse.ArgumentParser()
        # self.parser.add_argument("--ip",
        #                          default="127.0.0.1",
        #                          help="The ip to listen on")
        # self.parser.add_argument("--port",
        #                          type=int, default=5005,
        #                          help="The port to listen on")
        # self.args = self.parser.parse_args()

        self.dispatcher = Dispatcher()
        self.dispatcher.map("/filter", print)
        self.dispatcher.map("/volume",
                            self.print_volume_handler,
                            "Volume")
        self.dispatcher.map("/logvolume",
                            self.print_compute_handler,
                            "Log volume",
                            math.log)

        self.server = osc_server.ThreadingOSCUDPServer(
            ("127.0.0.1", 5005), self.dispatcher)
        print("Serving on {}".format(self.server.server_address))
        self.server.serve_forever()
