try:
    x = int(input("¿Cuál es x? "))
    print(f"x es {x}")
except ValueError:
    print("x no es un entero")