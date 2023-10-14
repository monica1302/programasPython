s=p=0
Nombres=["Juan", "Pedro", "Manuel", "Elias", "Maria", "Felipe", "Julia", "Roberto"]
Sueldo=[4550.22,8456.88,1234.12,9998.00,12345.50,29456.55,12234.00,2000.00]

datos = dict(zip(Nombres, Sueldo))
print(f"\nDiccionario: {datos}\n")

print("\nLas llaves: \n")
for k in datos.keys():
    print(k)

print("\nLos valores: \n")
for v in datos.values():
    print(v)

print("\nLlaves y valores:\n")
for k,v in datos.items():
    print(f"{k:<12} : {v}")
    s+=v

p=s/len(datos)

print(f"\nSuma: {s}")
print(f"Promedio: {p}")

print("\nProceso terminado")
