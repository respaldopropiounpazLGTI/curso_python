def main():
    texto = input("Gritaaa!!: ")
    texto_minuscula = convertir_minuscula(texto)
    print(texto_minuscula)

def convertir_minuscula(texto):
    return texto.lower()

main()