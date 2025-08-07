# Ejemplo de NO usar un método de clase.
import random

class Sombrero:
    def __init__(self):
        self.casas = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def clasificar(self, nombre):
        print(nombre, "está en", random.choice(self.casas))

sombrero = Sombrero()
sombrero.clasificar("Harry")

# Observa que sombrero = Sombrero() instancia un sombrero.
# podríamos querer ejecutar la función clasificar 
# sin crear una instancia particular del sombrero clasificador 
# (¡después de todo, solo hay uno!)
