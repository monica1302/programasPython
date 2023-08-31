#Dados los angulos de un triangulo, calcular el 3er angulo

print("Cuales son los angulos que se tienen: ")
ang1,ang2 =  float(input()), float(input())

ang3 = 180 -(ang1+ ang2)

print(f"El angulo faltante del triangulo es: {ang3:.2f}")