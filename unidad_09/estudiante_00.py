class Estudiante:
    ...

def principal():
    estudiante = obtener_estudiante()
    print(f"{estudiante.nombre} de {estudiante.casa}")

def obtener_estudiante():
    estudiante = Estudiante() # podemos crear una instancia estudiante de la clase Estudiante.
    estudiante.nombre = input("Nombre: ") # observa que utilizamos "notación de punto" para acceder a los atributos de esta variable estudiante de la clase Estudiante.
    estudiante.casa = input("Casa: ")
    return estudiante

if __name__ == "__main__":
    principal()
