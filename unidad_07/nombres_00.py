nombres = []
for _ in range(3):
    nombre = input("¿Cuál es tu nombre? ")
    nombres.append(nombre)

# Otra forma de escribirlo
# nombres = []
# for _ in range(3):
#     nombres.append(input("¿Cuál es tu nombre? "))

# lista de nombres como una lista ordenada.
for nombre in sorted(nombres):
    print(f"hola, {nombre}")

