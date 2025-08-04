# pip install pytest
# En la ventana de terminal, escribe pytest prueba_calculadora_04.py 
import pytest
from calculadora import cuadrado

def main():
    probar_positivo()
    probar_negativo()
    probar_cero()
    probar_str()

def probar_positivo():
    assert cuadrado(2) == 4
    assert cuadrado(3) == 9

def probar_negativo():
    assert cuadrado(-2) == 4
    assert cuadrado(-3) == 9

def probar_cero():
    assert cuadrado(0) == 0

# Observa que en lugar de usar assert, estamos aprovechando una función dentro de la biblioteca pytest llamada raises que te permite expresar que esperas que se levante un error.
def probar_str():
    with pytest.raises(TypeError):
        cuadrado("gato")

main()

# Más info sobre pytest https://docs.pytest.org/en/7.1.x/getting-started.html