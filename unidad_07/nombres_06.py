# cd  /workspaces/curso_python/unidad_07

# Hay muchos enfoques para solucionar este problema. 
# Sin embargo, aquí hay una forma simple de corregir este error en nuestro código.

with open("nombres.txt", "r") as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    print("hola,", linea.rstrip())

# Observa que rstrip tiene el efecto de eliminar el salto de línea extraño al final de cada línea.

# Aún así, este código podría simplificarse aún más:
with open("nombres.txt", "r") as archivo:
    for linea in archivo:
        print("hola,", linea.rstrip())





