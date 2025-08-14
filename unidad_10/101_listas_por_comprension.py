# Forma tradicional

# cuadrados = []

# for x in range(10):
#     cuadrados.append(x**2)

# print(cuadrados)

# [expresión for elemento in iterable]
# cuadrados = [x**2 for x in range(10)]

# print(cuadrados)

# Forma tradicional

# pares = []
# for x in range(10):
#     if x % 2 == 0:
#         pares.append(x)

# [expresión for elemento in iterable if condición]
pares = [x for x in range(10) if x % 2 == 0]

print(pares)
