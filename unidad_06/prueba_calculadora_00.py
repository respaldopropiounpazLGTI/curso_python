from calculadora import cuadrado

def main():
    probar_cuadrado()

def probar_cuadrado():
    if cuadrado(2) != 4:
        print("2 al cuadrado no fue 4")
    if cuadrado(3) != 9:
        print("3 al cuadrado no fue 9")

# Python establece __name__ como el nombre del archivo/módulo
if __name__ == "__main__":
    main()
