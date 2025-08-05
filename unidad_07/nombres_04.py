# cd  /workspaces/curso_python/unidad_07

# La palabra clave with te permite automatizar el cierre de un archivo.
nombre = input("¿Cuál es tu nombre? ")

with open("nombres.txt", "a") as archivo:
    archivo.write(f"{nombre}\n")


