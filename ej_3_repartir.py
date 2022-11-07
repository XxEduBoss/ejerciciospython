from ej_2_barajar import barajar

"""

Se desea realizar un método que simule la acción de repartir. Para ello el método recibe tres
parámetros:

● num_jugadores (int)

● num_cartas_por_jugador (int)

● baraja (list[diccionario])

El método debe devolver tantas listas como jugadores, y cada lista con el número de cartas
por jugador, sin repetir ninguna carta entre los jugadores. Además nada más empezar el
método hay que comprobar que el número de jugadores y las cartas que toca a cada jugador,
no supere el tamaño de la baraja. En el caso de no cumplirse la condición el método
devolverá un mensaje diciendo “Número de jugadores y cartas no válido”.

"""


def repartir_cartas(num_jugadores, num_cartas_por_jugador):
    baraja = barajar()
    monton = []

    if num_jugadores * num_cartas_por_jugador > len(baraja):
        print("Número de jugadores y cartas no válido")

    else:
        for jugar in range(num_jugadores):
            montones = baraja[0:num_cartas_por_jugador]
            monton.append(montones)
            baraja = baraja[num_cartas_por_jugador:]
            bucle = "jugador " + str(jugar + 1)
            print(bucle + str(montones))
        return monton

repartir_cartas(4, 10)
