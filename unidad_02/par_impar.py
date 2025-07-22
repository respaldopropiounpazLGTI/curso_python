def main():
    x = int(input("Cuál es x? "))
    print(es_par(x))
    if es_par(x):
        print("Par")
    else:
        print("Impar")
    

def es_par(x):
    return x % 2 == 0
    
main()