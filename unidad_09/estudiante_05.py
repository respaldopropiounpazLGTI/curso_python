# Decoradores
class Estudiante:
    def __init__(self, nombre, casa):
        if not nombre:
            raise ValueError("Nombre inválido")
        self.nombre = nombre
        self.casa = casa

    def __str__(self):
        return f"{self.nombre} de {self.casa}"

    # Definimos casa como una propiedad de nuestra clase.
    # Getter para casa
    @property
    def casa(self):
        return self._casa

    # Setter para casa
    @casa.setter
    def casa(self, casa):
        if casa not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Casa inválida")
        self._casa = casa

def principal():
    estudiante = obtener_estudiante()
    print(estudiante)

def obtener_estudiante():
    nombre = input("Nombre: ")
    casa = input("Casa: ")
    return Estudiante(nombre, casa)

if __name__ == "__main__":
    principal()

# ¿Por qué _casa y no casa?

# casa es una propiedad de nuestra clase, 
# con funciones a través de las cuales un usuario 
# intenta establecer nuestro atributo de clase.

# _casa es ese atributo de clase en sí mismo. 
# El guión bajo inicial, _, indica a los usuarios 
# que no necesitan (¡y de hecho, no deberían!) modificar este valor directamente. 
# _casa solo debe establecerse a través del setter casa.
 
# Cuando un usuario llama estudiante.casa, 
# están obteniendo el valor de _casa a través de nuestro "getter" casa.