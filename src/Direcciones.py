
principal = "192.168.1.103"

# computadores de desarrollo
dev = [
    # macMiniLab
    "192.168.1.100",
    # macbook janis
    "192.168.1.200",
    # macbook aaron
    "192.168.1.201",
    # macbook mateo
    "192.168.1.202"
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
        "192.168.1.101",
        "192.168.1.108",
        # "0.0.0.0",
        # "0.0.0.0",
    ],
    "eje-2":
    [
        # la 0 es placeholder
        "0.0.0.0",
        "0.0.0.0",
        "0.0.0.0",
        # "0.0.0.0",
        # "0.0.0.0",
    ],
    "eje-3":
    [
        # la 0 es placeholder
        "0.0.0.0",
        "0.0.0.0",
        "0.0.0.0",
        # "0.0.0.0",
        # "0.0.0.0",
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
        "192.168.1.101",
        "0.0.0.0",
    ],
    "eje-2":
    [
        "0.0.0.0",
        "0.0.0.0",
    ],
    "eje-3":
    [
        "0.0.0.0",
        "0.0.0.0",
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
        "0.0.0.0",
    ],
    "eje-2":
    [
        # la 0 es placeholder
        "0.0.0.0",
        "0.0.0.0",
    ],
    "eje-3":
    [
        # la 0 es placeholder
        "0.0.0.0",
        "0.0.0.0",
    ],
}
