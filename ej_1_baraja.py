"""

Se desea realizar un método que a partir de las tres listas que se van a mostrar a continuación,
devuelva una lista de diccionario de cartas. Las listas que toma como partida son:

tipo = [1,2,3,4,5,6,7, Sota, Caballo, Rey] (Cadenas)

palos= [“Oro”, “Basto”, “Copa”, “Espadas”]

El diccionario que compondría la carta sería el siguiente:

carta = {
tipo: “1”,
palo: “Oro”,
valor: 0.0
}

Se tiene que devolver una lista de diccionarios, con todas las cartas de los 4 palos de la
baraja.

"""

def mis_cartas():

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
            carta["valor"] = 0.0
            lista_cartas.append(carta)

    return lista_cartas

print(mis_cartas())