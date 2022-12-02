#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando
# la primera función.

def area_circulo(radio):
    """Esta función calcula el area de un círculo
    Parámetros:
    radio: Es el radio del círculo.
    Devuelve el área del círculo
    """
    pi = 3.1415
    return pi*radio**2

def volumenCilindro(radio, altura):
    """Esta función calcula el volumen de un cilindro.
    Parámetros:
    radio: Es el radio de la base del cilindro.
    altura: Es la altura del cilindro.
    Devuelve el volumen del clindro
    """
    return area_circulo(radio)*altura
print("El volumen del cilindro es " + "\n" +
str(volumenCilindro(16,10)))