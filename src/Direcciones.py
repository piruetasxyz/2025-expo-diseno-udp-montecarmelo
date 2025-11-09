# direcciones ip de los computadores en la red local
principal = "192.168.1.40"

# computadores de desarrollo
dev = [
    # macbook aaron
    "192.168.1.50",
    # ipad aaron
    "192.168.1.51",
    # macbook mateo
    "192.168.1.52",
    # macbook janis,
    "192.168.1.53"
    ]

# computadores con pantallas chicas
# hay 3 ejes
# hay 4 pantallas por eje
chicas = {
    "eje-1":
    [
        # la 0 es placeholder
        "0.0.0.0",
        # esta es 1
        "192.168.1.11",
        # esta es 2
        "192.168.1.12",
    ],
    "eje-2":
    [
        # la 0 es placeholder
        "0.0.0.0",
        # esta es 1
        "192.168.1.21",
        # esta es 2
        "192.168.1.22",
    ],
    "eje-3":
    [
        # la 0 es placeholder
        "0.0.0.0",
        # esta es 1
        "192.168.1.31",
        # esta es 2
        "192.168.1.32",
    ],
}


# computadores con pantallas medianas
# hay 3 ejes
# hay 2 pantallas por eje
# TODO: quizas 1 raspi con dos salidas iguales
medianas = {
    "eje-1":
    [
        # la 0 es placeholder
        "0.0.0.0",
        # eje1 mediana 1 - horizontal preguntas
        "192.168.1.13",
        # eje1 mediana 2 - vertical ejes
        "192.168.1.14",
    ],
    "eje-2":
    [
        # la 0 es placeholder
        "0.0.0.0",
        # eje1 mediana 1 - horizontal preguntas
        "192.168.1.23",
        # eje1 mediana 2 - vertical ejes
        "192.168.1.24",
    ],
    "eje-3":
    [
        # la 0 es placeholder
        "0.0.0.0",
        # eje1 mediana 1 - horizontal preguntas
        "192.168.1.33",
        # eje1 mediana 2 - vertical ejes
        "192.168.1.34",
    ],
}

# computadores con pantallas grandes
# hay 3 ejes
# hay 1 pantalla por eje
grandes = {
    "eje-1":
    [
        # la 0 es placeholder
        "0.0.0.0",
        # eje1 grande 1
        "192.168.1.15",
    ],
    "eje-2":
    [
        # la 0 es placeholder
        "0.0.0.0",
        # eje1 grande 1
        "192.168.1.25",
    ],
    "eje-3":
    [
        # la 0 es placeholder
        "0.0.0.0",
        # eje1 grande 1
        "192.168.1.35",
    ],
}
