saludo = input("Saludar: ").lower().strip()

print(saludo.startswith("hola") == "hola")

if saludo.startswith("hola") == "hola":
    print(0)
elif saludo.startswith("h") == "h":
    print(20)
else:
    print(100)