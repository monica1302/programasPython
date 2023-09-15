#Calcular el promedio de 5 notas y arrojar mensaje correspondiente

print("Dame tus 5 calificaciones: ")
n1, n2, n3, n4, n5 = int(input()), int(input()), int(input()), int(input()), int(input())

suma = n1+n2+n3+n4+n5
prom= suma/5
print("Promedio: ", prom)

if 0 < prom <= 6:
    print("Quedas reprobado")
elif 6 < prom <= 7:
    print("Pasas de panzazo")
elif 7 < prom <= 8:
    print ("Muy bien, puedes mejorar")
elif 8 < prom <= 9:
    print ("Excelente, sigue así")
elif 9 < prom <= 10:
    print ("Perfecto, tu esfuerzo valio la pena")

print("\nProceso terminado")
