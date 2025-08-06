# DIFERENCIAS ENTRE TUPLAS Y LISTAS EN PYTHON
# Crear una lista (usa corchetes [])
mi_lista = [1, 2, 3, 4, 5]
print(f"Lista: {mi_lista}")
print(f"Tipo: {type(mi_lista)}")

# Crear una tupla (usa paréntesis ())
mi_tupla = (1, 2, 3, 4, 5)
print(f"Tupla: {mi_tupla}")
print(f"Tipo: {type(mi_tupla)}")

##############################

# Las LISTAS son MUTABLES (se pueden modificar)
print("LISTAS - MUTABLES:")
print(f"Lista original: {mi_lista}")

# Cambiar un elemento
mi_lista[0] = 999
print(f"Después de cambiar índice 0: {mi_lista}")

# Agregar elementos
mi_lista.append(6)
print(f"Después de append(6): {mi_lista}")

# Eliminar elementos
mi_lista.remove(999)
print(f"Después de remove(999): {mi_lista}")

# Las TUPAS son INMUTABLES (no se pueden modificar)
print(f"Tupla original: {mi_tupla}")

# Intentar modificar una tupla genera ERROR
try:
    mi_tupla[0] = 999  # Esto causará un error
except TypeError as e:
    print(f"Error al intentar modificar tupla: {e}")

try:
    mi_tupla.append(6)  # Esto también causará un error
except AttributeError as e:
    print(f"Error al intentar append en tupla: {e}")

##############################

# Ambas permiten acceso por índice
print(f"Primer elemento de la lista: {mi_lista[0]}")
print(f"Primer elemento de la tupla: {mi_tupla[0]}")

# Ambas permiten slicing
print(f"Slice de lista [1:3]: {mi_lista[1:3]}")
print(f"Slice de tupla [1:3]: {mi_tupla[1:3]}")

##############################

# USA LISTAS cuando:
# - Necesites modificar los datos.
# - El tamaño puede cambiar.
# - Requieras métodos como append, remove, etc.
# - Los datos representen una colección que puede crecer.
# USA TUPLAS cuando:
# - Los datos no deben cambiar (coordenadas, RGB, etc.).
# - Necesites una clave para diccionario.
# - Quieras mejor rendimiento en acceso.
# - Representes datos estructurados fijos.

##############################

# Ejemplo con coordenadas (mejor como tupla)
coordenada = (10, 20)  # x, y - no debería cambiar
print(f"Coordenada: {coordenada}")

# Tuplas como claves de diccionario
puntos = {
    (0, 0): "origen",
    (1, 1): "diagonal",
    (0, 1): "arriba"
}
print(f"Diccionario con tuplas como claves: {puntos}")