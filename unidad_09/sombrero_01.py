# Ejemplo con método de clase
import random

class Sombrero:
    casas = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def clasificar(cls, nombre):
        print(nombre, "está en", random.choice(cls.casas))

Sombrero.clasificar("Harry")

# El método __init__ se elimina porque no necesitamos instanciar un sombrero en ninguna parte de nuestro código.
# self, por lo tanto, ya no es relevante y se elimina. 
# Especificamos este clasificar como un @classmethod, reemplazando self con cls.
