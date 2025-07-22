vida = input("¿Cuál es la respuesta a la gran pregunta sobre la vida, el universo y todo lo demás? ").lower().strip()

#if vida == "42" or vida== "cuarenta y dos" or vida == "cuarentaidos":
  #  print("¡Sí!")
#else:
 #   print("NO")




match vida:
    case "42" :
        print("¡Sí!")
    case "cuarenta y dos":
        print("¡Sí!")
    case "cuarentaidos":
        print("¡Sí!")
    case _:
        print("¡NO!")
