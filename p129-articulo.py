class Articulo:
    def __init__(self, ide, descripcion, cantidad, precio,):
        self.ide = ide
        self.descripcion = descripcion 
        self.cantidad =  cantidad
        self.precio = precio
        
    def total(self):
        return self.cantidad*self.precio
   
    def __str__(self):
        return f"Id: {self.ide}, descripcion: {self.descripcion}, cantidad: {self.cantidad}, precio: {self.precio}"
    

# Programa principal
art1 = Articulo('A101', 'Pluma Roja', 888, 0.08)
print(art1)
art1.cantidad = 999
art1.precio = 0.99
print("Id          = ",art1.ide)
print("Descripcion = ",art1.descripcion)
print("Cantidad    = ",art1.cantidad)
print("Precio      = ",art1.precio)
print(f"Total      = {art1.total():.2f}\n")

art2 = Articulo("A102", "Pluma Azul", 934, 1.2)
print(art2)
art3 = Articulo("P103", "Lapiz del 12", 456, 0.5)
print(art3)
total = art1.total() + art2.total() + art3.total()
print(f"\nTotal todos = {total:.2f}")

print ("\nProceso terminado")