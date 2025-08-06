class Estudiante:
    def __init__(self, nombre, casa):
        if not nombre:
            # podemos crear nuestras propias excepciones que alertan al programador sobre un error 
            # potencial creado por el usuario llamado raise.
            raise ValueError("Falta el nombre") # levantamos ValueError con un mensaje de error específico.
        if casa not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Casa inválida")
        self.nombre = nombre
        self.casa = casa

def principal():
    estudiante = obtener_estudiante()
    print(f"{estudiante.nombre} de {estudiante.casa}")

def obtener_estudiante():
    nombre = input("Nombre: ")
    casa = input("Casa: ")
    return Estudiante(nombre, casa)

if __name__ == "__main__":
    principal()
