import random


def baraja():
    carta = {
        "tipo": "",
        "palo": "",
        "valor": "",
    }

    tipos = [1, 2, 3, 4, 5, 6, 7, "Sota", "Caballo", "Rey"]
    palos = ["Oro", "Basto", "Copa", "Espadas"]
    lista_cartas = []

    for palo in palos:
        for tipo in tipos:
            carta = carta.copy()
            carta["tipo"] = tipo
            carta["palo"] = palo
            if carta["tipo"] == "Sota":
                carta["valor"] = 10
            elif carta["tipo"] == "Caballo":
                carta["valor"] = 11
            elif carta["tipo"] == "Rey":
                carta["valor"] = 12
            else:
                carta["valor"] = carta["tipo"]
            lista_cartas.append(carta)

    return lista_cartas
    print(lista_cartas)
baraja()
def barajar():

    Baraja = baraja()
    cartas_barajadas = []

    for carta in Baraja:

        i = random.randint(0, len(cartas_barajadas))
        cartas_barajadas.insert(i, carta)

    return cartas_barajadas

def el21(num_jugadores):

    if num_jugadores % 40 != 0:
        print("Vuelva a escribir un número de jugadores correcto")

    else:
        print("Perfecto, ¡A jugar!")


    for jug in range(num_jugadores):

        monton1 = []
        monton2 = []
        monton3 = []
        monton4 = []
