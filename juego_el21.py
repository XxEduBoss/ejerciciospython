import random
import sys
import time
import os

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

def barajar():

    baraja1 = baraja()
    cartas_barajadas = []

    for carta in baraja1:

        i = random.randint(0, len(cartas_barajadas))
        cartas_barajadas.insert(i, carta)

    return cartas_barajadas



def el21(num_jugadores):

    monton1 = []
    monton2 = []
    monton3 = []
    monton4 = []
    p_monton1 = 0
    p_monton2 = 0
    p_monton3 = 0
    p_monton4 = 0

    if 40 % num_jugadores != 0:
        sys.exit("Vuelva a escribir un número de jugadores correcto")

    else:
        print("---------- EMPIEZA EL 21 ----------")
        print("Monton número 1: " + str(monton1) + " 0 puntos")
        print("Monton número 2: " + str(monton2) + " 0 puntos")
        print("Monton número 3: " + str(monton3) + " 0 puntos")
        print("Monton número 4: " + str(monton4) + " 0 puntos")



    baraja = barajar()
    monton = []
    cartas_por_jugador = 40 / num_jugadores

    for jugar in range(num_jugadores):
        montones = baraja[0:int(cartas_por_jugador)]
        monton.append(montones)
        baraja = baraja[int(cartas_por_jugador):]

    return monton


    for jug in range(num_jugadores):

        montonjugador = monton[0]
        monton.remove[0]

    print(montonjugador)







el21(8)