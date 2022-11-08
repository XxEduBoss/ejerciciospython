import random
import time
from random import choice
import os

def carta1():
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
                carta["valor"] = 0.5
            elif carta["tipo"] == "Caballo":
                carta["valor"] = 0.5
            elif carta["tipo"] == "Rey":
                carta["valor"] = 0.5
            else:
                carta["valor"] = carta["tipo"]
            lista_cartas.append(carta)

    return lista_cartas
#
def barajar():

    baraja = carta1()
    cartas_barajadas = []

    for carta in baraja:

        i = random.randint(0, len(cartas_barajadas))
        cartas_barajadas.insert(i, carta)

    return cartas_barajadas



def sieteymedio(num_jugadores):
    limite = 7.5
    lista_puntuaje = []
    lista = []

    for jug in range(num_jugadores):

        carta_aleatoria = choice(barajar())

        suma_total = carta_aleatoria["valor"]

        print("Te ha tocado la carta " + str(carta_aleatoria["tipo"]) + " de " + str(carta_aleatoria["palo"]))

        print("Tienes " + str(carta_aleatoria["valor"]) + " puntos")

        respuesta = input("¿Quieres otra carta?: ")


        while respuesta == "SI".lower():

            carta_aleatoria = choice(barajar())

            print("Te ha tocado la carta " + str(carta_aleatoria["tipo"]) + " de " + str(carta_aleatoria["palo"]))

            suma_total += carta_aleatoria["valor"]

            if suma_total == 1:
                print("Tienes " + str(suma_total) + " punto")

            else:
                print("Tienes " + str(suma_total) + " puntos")

            if suma_total == 7.5:
                print("Has terminado")

                lista_puntuaje.append(suma_total)
                suma_total = 0
                lista.append(suma_total)

                time.sleep(1.2)
                os.system('cls')
                break

            else:
                respuesta = input("¿Quieres otra carta?: ")

        else:
            print("Te has plantado con " + str(suma_total) + " puntos")

            lista_puntuaje.append(suma_total)

            if suma_total > limite:
                suma_total -= limite
                lista.append(suma_total)

            elif suma_total < limite:
                suma_total = limite - suma_total
                lista.append(suma_total)

            elif suma_total == limite:
                suma_total = 0
                lista.append(suma_total)

            time.sleep(1.2)
            os.system('cls')

    minimo = min(lista)
    punt = minimo
    diferencias = lista
    lista_ganadores = []

    for i in range(0, len(diferencias)):
        if diferencias[i] == punt:
            lista_ganadores.append(i)

    for indice in lista_ganadores:
        if len(lista_ganadores) == 1:
            print("Ha ganado el jugador " + str(lista_ganadores[0] + 1))

        else:
            print("Han quedado empate")

    jugador = 0
    for jug in range(num_jugadores):

        print("El jugador " + str(jugador + 1) + " se ha quedado a " + str(lista[0]) + " puntos")
        jugador += 1
        lista.remove(lista[0])

(sieteymedio(2))