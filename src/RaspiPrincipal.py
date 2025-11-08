# importar biblioteca
from pythonosc.udp_client import SimpleUDPClient
# from Direcciones import chicas, medianas, dev, principal
from Direcciones import chicas, medianas, principal


class RaspiPrincipal:
    def __init__(self, puerto):
        self.puerto = puerto
        # self.numeroDeRaspis = 128
        self.direccionIP = principal
        self.ipsPantallas = []

        for eje in chicas:
            for ip in chicas[eje]:
                if ip != "0.0.0.0":
                    self.ipsPantallas.append(ip)

        for eje in medianas:
            for ip in medianas[eje]:
                if ip != "0.0.0.0":
                    self.ipsPantallas.append(ip)
        self.clientes = []
        self.enviarMensajeATodos("/admin/init", 1)
        self.corriendo = True

        for ip in self.ipsPantallas:
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
        self.enviarMensajeATodos("/paraMedianas/nuevaPregunta/", preguntaActual)
        # self.enviarMensajeATodos("/paraChicas/nuevaRespuesta/", preguntaActual)

    def enviarMensajeNuevaRespuesta(self, preguntaActual, eje, pantalla):
        self.comandoTemp = "/paraChicas/" + str(eje) + "/" + str(pantalla) + "/"
        self.enviarMensajeATodos(self.comandoTemp, preguntaActual)
        print(self.comandoTemp)
