class rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    def area(self):
        return self.ancho* self.largo
    def perimetro(self):
        return 2*self.largo +2*self.ancho
    def __str__(self):
        return f"Largo ={self.largo}, ancho={self.ancho}, area= {self.area():.2f}, perimetro={self.perimetro():.2f}"




#Programa principal
r1=rectangulo(12, 3.4)
print(r1)
print(f"Largo: {r1.largo}, ancho: {r1.ancho}")
print(f"El area: {r1.area():.2f}")
print(f"El perimetro: {r1.perimetro():.2f}\n")

r2=rectangulo(5.6, 7.8)
print(r2)
print(f"Largo: {r2.largo}, ancho: {r2.ancho}")
print(f"El area: {r2.area():.2f}")
print(f"El perimetro: {r2.perimetro():.2f}")

print ("\nProceso terminado")