# cd  /workspaces/curso_python/unidad_07
nombre = input("¿Cuál es tu nombre? ")

# se ha cambiado a a para "append" (agregar). 
archivo = open("nombres.txt", "a")

# Sin embargo, ¡notarás un nuevo problema!
archivo.write(nombre)
archivo.close()
