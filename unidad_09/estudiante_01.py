class Estudiante:
    def __init__(self, nombre, casa):
        self.nombre = nombre
        self.casa = casa

def principal():
    estudiante = obtener_estudiante()
    print(f"{estudiante.nombre} de {estudiante.casa}")

def obtener_estudiante():
    estudiante = Estudiante()
    estudiante.nombre = input("Nombre: ")
    estudiante.casa = input("Casa: ")
    return estudiante 
    # return Estudiante(nombre, casa) # Otra opción

if __name__ == "__main__":
    principal()

# El método __init__:
# - Es el constructor de la clase.
# - Se ejecuta automáticamente cuando creas un nuevo objeto de tipo Estudiante.
# - Los guiones bajos dobles (__init__) indican que es un método especial en Python.

# Los parámetros:
# - self: referencia al objeto que se está creando (siempre va primero).
# - nombre: el nombre del estudiante.
# - casa: la casa a la que pertenece el estudiante.

# Los atributos:
# - self.nombre = nombre: guarda el nombre en el objeto
# - self.casa = casa: guarda la casa en el objeto