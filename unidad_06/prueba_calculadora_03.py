# pip install pytest
# En la ventana de terminal, escribe pytest prueba_calculadora_03.py 

from calculadora import cuadrado

def main():
    probar_cuadrado()

def probar_cuadrado():
    assert cuadrado(2) == 4
    assert cuadrado(3) == 9
    assert cuadrado(-2) == 4
    assert cuadrado(-3) == 9
    assert cuadrado(0) == 0


main()