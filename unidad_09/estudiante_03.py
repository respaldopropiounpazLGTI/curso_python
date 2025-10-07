class Estudiante:
    def __init__(self, nombre, casa, patronus):
        if not nombre:
            raise ValueError("Falta el nombre")
        if casa not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Casa inválida")
        self.nombre = nombre
        self.casa = casa
        self.patronus = patronus

    # Python te permite crear una función específica 
    # mediante la cual puedes imprimir los atributos de un objeto. 
    # __str__ es un método incorporado que viene con las clases de Python.
    def __str__(self):
        return f"{self.nombre} de {self.casa}"

def principal():
    estudiante = obtener_estudiante()
    print(estudiante)  # <----

def obtener_estudiante():
    nombre = input("Nombre: ")
    casa = input("Casa: ")
    patronus = input("Patronus: ")
    return Estudiante(nombre, casa, patronus)

if __name__ == "__main__":
    principal()
