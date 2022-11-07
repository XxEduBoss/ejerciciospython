from ej_1_baraja import mis_cartas
import random

"""

Se desea realizar un método que reciba una lista de diccionarios de cartas y ponga las cartas
en posiciones aleatorias, simulando la acción de barajar. El método también devuelve una
lista de diccionarios con las cartas barajadas.

"""


def barajar():

    baraja = mis_cartas()
    cartas_barajadas = []

    for carta in baraja:

        i = random.randint(0, len(cartas_barajadas))
        cartas_barajadas.insert(i, carta)

    return cartas_barajadas

# print(barajar())
