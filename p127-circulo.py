import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return math.pi*math.pow(self.radio,2)
    def circu(self):
        return 2*math.pi * self.radio
    def __str__(self):
        return f"Radio= {self.radio:.2f}, area= {self.area():.2f}, circunferencia= {self.circu():.2f}"

#Programa principal
c1= Circulo(10.40)
print(c1)
print(f"El radio: {c1.radio:.2f}")
print(f"El area: {c1.area():.2f}")
print(f"Circunferencia: {c1.circu():.2f}\n")

c2= Circulo(12.45)
print(c2)
print(f"El radio: {c2.radio:.2f}")
print(f"El area: {c2.area():.2f}")
print(f"Circunferencia: {c2.circu():.2f}\n")

c3= Circulo(100)
print(c3)
print(f"El radio: {c3.radio:.2f}")
print(f"El area: {c3.area():.2f}")
print(f"Circunferencia: {c3.circu():.2f}\n")

areatotal=c1.area()+c2.area()+c3.area()
print(f"El area total de los circulos es: {areatotal:.2f}" )

print ("\nProceso terminado")

