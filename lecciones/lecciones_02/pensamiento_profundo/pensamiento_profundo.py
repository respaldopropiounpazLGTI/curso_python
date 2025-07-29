pregunta = input("¿Cuál es la respuesta a la gran pregunta sobre la vida, el universo y todo lo demás? ")

pregunta = pregunta.strip().lower()

match pregunta:
    case "42" | "cuarenta y dos" | "cuarentaidos":
        print("Si")
    case _ :
        print("No")

# Opción 1

# if pregunta == "42" or pregunta == "cuarenta y dos" or pregunta == "cuarentaidos":
#     print("Si")
# else:
#     print("No")