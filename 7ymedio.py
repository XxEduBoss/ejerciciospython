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

    print(lista_puntuaje)
    print(lista)

    if min(lista):
        print("Ha ganado el jugador " + str(min(lista)) + 1)

    else:
        print("Han quedado empate varios jugadores")




    # Ahora hay que comparar las puntuaciones y decir quien es o quienes son los ganadores.
    # Crear lista con puntuaciones punt_total_jugadores = []
    # Restarle 7.5 a esas puntuaciones
    # Ponerlas en positivo (obtener valor absoluto)
    # El valor minimo min() es el ganador al quedar más cerca del 7.5

    for p in punt_total_jugadores:  #creo diferencia como variable, que va a ser la caja donde me meta las operaciones
        diferencia = p - 7.5
        if diferencia < 0:
            diferencia = diferencia*(-1)  #no pasa nada por pisarme la caja. De esta manera se guardan las operaciones
        elif diferencia > 0:
            diferencia = diferencia * 1
        puntuacion_final.append(diferencia)

#ahora tengo que obtener el minimo, localizar el índice del mínimo y llamar al índice del numero y del nombre de jugador para que sea ganador
#en caso de empate, tiene que llamar a ambos jugadores.
    minimo = min(puntuacion_final)

#veo si hay empate en las puntuaciones, para ello comprobamos las diferencias y creamos una lista de ganadores.
    punt = minimo
    diferencias = puntuacion_final
    lista_ganadores = []

    for i in range(0, len(diferencias)):
        if diferencias[i] == punt:
            lista_ganadores.append(i)

    for indice in lista_ganadores:
        print("ganador/es: " + str(lista_nombres[indice]))

(sieteymedio(2))