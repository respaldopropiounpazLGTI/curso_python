# cd  /workspaces/curso_python/unidad_07

# ¿Qué pasa si queremos leer de un archivo?
# Observa que readlines tiene una capacidad especial para leer todas las líneas de un archivo y almacenarlas en una lista llamada lineas.
with open("nombres.txt", "r") as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    print("hola,", linea)



