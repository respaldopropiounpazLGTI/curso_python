def main():
    nombre = input("Cuál es tu nombre?").strip().title()

    hola(nombre)

    hola()

def hola(para="Mundo"):
    print("Hola", para)

main()


