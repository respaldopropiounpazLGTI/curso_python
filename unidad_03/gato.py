def main():
    maullar(obtener_numero())

def obtener_numero():
    while True:
        n = int(input("Cuál es n? "))
        if n > 0:
            return n

def maullar(n):
    for _ in range(n):
        print("miau")

main()