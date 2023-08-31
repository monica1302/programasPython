#Calcular el volumen de un cilindro dado su radio y altura

print("Calcular el volumen de un cilindro dado su radio y altura")
print("Cual es el radio y altura del cilindro: ")
radio,altura =  float(input()), float(input())

import math
volumen = math.pi * (radio* radio) * altura

print(f"El volumen del cilindro es: {volumen:.2f}")

