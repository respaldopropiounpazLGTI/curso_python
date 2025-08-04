while True:
    try:
        x = int(input("¿Cuál es x? "))
    except ValueError:
        print("x no es un entero")
    else:
        break

print(f"x es {x}")
