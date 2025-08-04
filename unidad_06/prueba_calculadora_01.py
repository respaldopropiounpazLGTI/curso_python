from calculadora import cuadrado

def main():
    probar_cuadrado()

def probar_cuadrado():
    # El comando assert de Python nos permite decirle al intérprete que algo, 
    # alguna afirmación, es verdadera.
    assert cuadrado(2) == 4
    assert cuadrado(3) == 9

if __name__ == "__main__":
    main()

