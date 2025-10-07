# Ejemplo con método de clase
class Estudiante:
    def __init__(self, nombre, casa):
        self.nombre = nombre
        self.casa = casa

    def __str__(self):
        return f"{self.nombre} de {self.casa}"

    @classmethod
    def obtener(cls):
        nombre = input("Nombre: ")
        casa = input("Casa: ")
        return cls(nombre, casa)

def principal():
    estudiante = Estudiante.obtener()
    print(estudiante)

if __name__ == "__main__":
    principal()
