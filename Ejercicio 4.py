#Escribir una función que reciba una muestra de números en una lista y devuelva su media.

def muestra(muestra):
    """Esta función calcula la media de una muestra de
    números.
    Parámetros:
    muestra: Es una lista de números
    Devuelve la media de los números.
    """

    return sum(muestra) / len(muestra)
print(muestra([1, 3, 7, 8, 9]))
print(muestra([1.9, 2.5, 3.8, 7.7, 9.1, 10.6]))
