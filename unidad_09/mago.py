# Ejemplo Herencia

class Mago:
    def __init__(self, nombre):
        if not nombre:
            raise ValueError("Falta el nombre")
        self.nombre = nombre

class Estudiante(Mago):
    def __init__(self, nombre, casa):
        super().__init__(nombre)
        self.casa = casa

    ...

class Profesor(Mago):
    def __init__(self, nombre, materia):
        super().__init__(nombre)
        self.materia = materia

    ...

mago = Mago("Albus")
estudiante = Estudiante("Harry", "Gryffindor")
profesor = Profesor("Severus", "Defensa Contra las Artes Oscuras")
...

print(estudiante.nombre)
print(profesor.nombre)

# Observa que hay una clase arriba llamada Mago 
# y una clase llamada Estudiante. 
# Además, observa que hay una clase llamada Profesor. 
# Tanto estudiantes como profesores tienen nombres. 
# También, tanto estudiantes como profesores son magos. 
# Por lo tanto, tanto Estudiante como Profesor heredan las características de Mago. 
# Dentro de la clase "hija" Estudiante, 
# Estudiante puede heredar de la clase "padre" o "súper" Mago 
# ya que la línea super().__init__(nombre) ejecuta el método init de Mago. 
# Finalmente, observa que las últimas líneas de este código crean un mago llamado Albus, 
# un estudiante llamado Harry, y así sucesivamente.
