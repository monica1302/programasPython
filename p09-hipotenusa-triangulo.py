#Calcular la hipotenusa de un triangulo rectangulo 

print("Dame los 3 la longitud de los lados del triangulo")
lado1,lado2,lado3 =  int(input()), int(input()), int(input())

import math
hipo=math.sqrt(lado1+lado2+lado3)

print(f"\n La hipotenusa del triangulo es: {hipo:.2f} ")