# importar biblioteca
from pythonosc.udp_client import SimpleUDPClient


class RaspiPrincipal:
    def __init__(self, puerto):
        self.puerto = puerto
        self.numeroDeRaspis = 128
        self.ipsPantallas = ["10.30.123.87"]
        self.clientes = []
        self.enviarMensajeATodos("/admin/init", 1)
        self.corriendo = True

        for ip in self.ipsPantallas:
            # cliente = SimpleUDPClient(ip, self.puerto)
            self.clientes.append(SimpleUDPClient(ip, self.puerto))

    def enviarMensaje(self, cliente, etiqueta, valor):
        cliente.send_message(etiqueta, valor)

    def enviarMensajeATodos(self, etiqueta, valor):
        for cliente in self.clientes:
            try:
                # print(cliente)
                self.enviarMensaje(cliente, etiqueta, valor)
                # print("etiqueta:" + etiqueta +
                #       " valor: " + str(valor) +
                #       " enviado a " + "bla")
            except Exception as e:
                print(e)
                # print("pucha")

    def mostrar(self):
        print("mostrar en raspiPrincipal")

    def enviarMensajeNuevaPregunta(self, preguntaActual):
        self.enviarMensajeATodos("/paraMedianas/nuevaPregunta", preguntaActual)
