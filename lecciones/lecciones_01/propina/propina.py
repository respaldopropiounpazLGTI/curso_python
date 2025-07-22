def main():
    dolares = dolar_a_float(input("Cuánto costó la comida? "))
    #  print(dolares)
 
    porcentaje = porcentaje_a_float(input("Qué porcentaje te gustaría dejar de propina? "))
    #  print(porcentaje)

    propina = dolares * porcentaje
 
    print(f"Dejar ${propina:.2f}")

def dolar_a_float(d):
    return float(d.strip("$"))

def porcentaje_a_float(p):
   return float(p.replace('%', "")) / 100 
 

main()