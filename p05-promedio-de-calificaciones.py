# Calcular el promedio de 3 calificaciones

print("Calculando el promedio de 3 calificaciones")
print("Dame 3 calificaciones separadas por espacios:")
c1,c2,c3 = input().split()
c1,c2,c3 = [int(c1), int(c2),int(c3)]

suma = (c1+c2+c3)
prom = suma/3
print(f"Las calificaciones son : {c1},{c2},{c3} su suma: {suma:.2f} y el promedio es:  {prom:.2f}")

