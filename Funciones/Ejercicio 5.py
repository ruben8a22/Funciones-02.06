#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

def cuadrado(muestra):
    """Esta función calcula los cuadrados de una lista de
    números.
    Parámetros:
    muestra: Es una lista de números
    Devuelve una lista con los cuadrados de los números
    """
    lista = []
    for i in muestra:
        lista.append(i**2)
    return lista
print(cuadrado([2, 4, 6, 8, 10]))
print(cuadrado([2.2, 4.2, 3.4, 4.5, 7.7, 8.6]))