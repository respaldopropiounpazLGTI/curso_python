# cd  /workspaces/curso_python/unidad_07
nombre = input("¿Cuál es tu nombre? ")

# open es una funcionalidad incorporada en Python que te permite abrir un archivo y utilizarlo en tu programa.
# Observa que la función open abre un archivo llamado nombres.txt con la escritura habilitada, como lo indica la w.
archivo = open("nombres.txt", "w")

# escribe el nombre en el archivo de texto.
archivo.write(nombre)

# cierra el archivo.
archivo.close()
