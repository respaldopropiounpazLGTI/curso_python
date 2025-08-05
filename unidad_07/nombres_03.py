# cd  /workspaces/curso_python/unidad_07
nombre = input("¿Cuál es tu nombre? ")
archivo = open("nombres.txt", "a")

# \n lo soluciona
archivo.write(f"{nombre}\n")
archivo.close()

