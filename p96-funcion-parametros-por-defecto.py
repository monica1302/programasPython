# Funcion con parametros con valores por defecto o valores pre esstablecidos

def saluda(nombre="Juan",edad=10):
    print(f"Hola {nombre} tu edad es {edad}")

saluda()
saluda("Rocio")
saluda("Jorge",30)

print ("\nProceso terminado")
