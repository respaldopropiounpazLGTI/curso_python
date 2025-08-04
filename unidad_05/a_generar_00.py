# Puedes usar la palabra import en tu programa.
import random

# Dentro del módulo random, hay una función incorporada llamada random.choice(seq). random es el módulo que estás importando. 
# Dentro de ese módulo, está la función choice. 
# Esa función toma un seq o secuencia que es una lista.
moneda = random.choice(["cara", "cruz"])
print(moneda)
