# /workspaces/curso_python/unidad_07
import csv

estudiantes = []

with open("estudiantes.csv") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        estudiantes.append({"nombre": fila[0], "hogar": fila[1]})

for estudiante in estudiantes:
    print(f"{estudiante['nombre']} es de {estudiante['hogar']}")
