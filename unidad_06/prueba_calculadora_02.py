from calculadora import cuadrado

def main():
    probar_cuadrado()

def probar_cuadrado():
    try:
        assert cuadrado(2) == 4
    except AssertionError:
        print("2 al cuadrado no es 4")
    try:
        assert cuadrado(3) == 9
    except AssertionError:
        print("3 al cuadrado no es 9")
    try:
        assert cuadrado(-2) == 4
    except AssertionError:
        print("-2 al cuadrado no es 4")
    try:
        assert cuadrado(-3) == 9
    except AssertionError:
        print("-3 al cuadrado no es 9")
    try:
        assert cuadrado(0) == 0
    except AssertionError:
        print("0 al cuadrado no es 0")

if __name__ == "__main__":
    main()

# Más sobre assert https://docs.python.org/3/reference/simple_stmts.html#assert