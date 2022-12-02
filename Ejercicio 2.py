#Escribir una función que reciba un número entero positivo y devuelva su factorial. Realiza el ejercicio mediante
# bucles interactivos y mediante una función recursiva.

def factorial(numero):
    """Esta función calcula el factorial de un número entero
    positivo
    Parámetros:
    numero: Es un numero entero positivo
    Devuelve el factorial de un numero."""
    p = 1
    for n in range(1, numero + 1):
        p = p * n
    return p

print(factorial(3))

def factorialRec(numero):
    """Esta función calcula el factorial de un número entero
    positivo
    Parámetros:
    numero: Es un numero entero positivo
    Devuelve el factorial de un numero."""
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)
print(factorialRec(3))



