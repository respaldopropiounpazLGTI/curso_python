saludo = input("Saludar: ").lower().strip()

if saludo.startswith("hola"):
    print(0)
elif saludo.startswith("h"):
    print(20)
else:
    print(100)