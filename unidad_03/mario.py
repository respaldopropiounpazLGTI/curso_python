def main():
    # imprimir_columna(3)
    # imprimir_fila(4)
    imprimir_cuadrado(3)

def imprimir_cuadrado(tamanio):
    for i in range(tamanio):
        imprimir_fila(tamanio)

# def imprimir_columna(altura):
#     for _ in range(altura):
#         print("#")

def imprimir_fila(anchura):
    print("#" * anchura)


main()