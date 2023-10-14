#Diccionario

venta={
    "Juan":1550,
    "Jose":2600,
    "Maria":2220
}

print(f"\nDiccionario: {venta}\n")

venta["Rocio"]= 2500
venta["Mateo"]= 1567
venta.update({"Andrea":9567})
venta.update({"Miguel":1234})

print("\nDiccionario modificado:")
for k,v in venta.items():
    print(f"{k:<10} : {v}")


print("\nProceso terminado")
