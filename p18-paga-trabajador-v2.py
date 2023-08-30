# Calcular la paga de un trabajador considerando las horas extra

print("Calculando la paga de horas extra de un trabajador (la hora extra se pagan al doble)")
nombre = input("Nombre del trabajador:  ")
horas = int(input("Horas trabajadas:  "))
paga = float(input("Paga x hora:  "))

if horas > 40 :
    extra = horas - 40
    total = (40 * paga ) + ( extra * (paga + paga))
else :
    total = horas * paga

print(f"{nombre} trabajo {horas} horas, por lo que le corresponde un total de {total} pesos")


print("\n Proceso terminado")

