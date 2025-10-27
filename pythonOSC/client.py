"""Small example OSC client

This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""
import argparse
import random
import time
from pythonosc import udp_client

puertoServidor = 5000

lasOtrasRaspberries = [
    # 01
    "",
    # 02
    "",
    # 03
    "",
    # 04
    "192.168.1.126",
    # 05
    "192.168.1.127",
    # 06
    "",
    # 07
    "",
    # 08
    "",
    # 09
    "",
    # 10
    ""
]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
                        help="The ip of the OSC server")

    parser.add_argument("--port", type=int, default=puertoServidor,
                        help="The port the OSC server is listening on")

    args = parser.parse_args()

    for ip in lasOtrasRaspberries:
        if ip != "":
            print("Enviando a la Raspberry Pi en la IP: {}".format(ip))
            args.ip = ip
            client = udp_client.SimpleUDPClient(args.ip, args.port)

            for x in range(10):
                client.send_message("/filter", random.random())
                time.sleep(0.1)
