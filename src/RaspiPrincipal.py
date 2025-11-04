from pythonosc.udp_client import SimpleUDPClient


class RaspiPrincipal:
    def __init__(self, puerto):
        self.puerto = puerto
        self.numeroDeRaspis = 128
        self.ips = []
        self.puertoEnviar = 1234

        for i in range(self.numeroDeRaspis):
            self.ips.append(
                "192.168.0." + str(i))

    def enviarMensaje(self, ip, etiqueta, valor):
        client = SimpleUDPClient(ip, self.puerto)
        client.send_message(etiqueta, valor)

    def enviarMensajeATodos(self, etiqueta, valor):
        for ip in self.ips:
            self.enviarMensaje(ip, etiqueta, valor)
            print("etiqueta:" + etiqueta +
                  " valor: " + str(valor) +
                  " enviado a " + ip)
