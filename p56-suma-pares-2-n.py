#Imprimir numeors pares a n y su suma

n = int(input("Hasta que numero deseas imprimir: "))
s = 0

for i in range(2,n+1,2):
    print(i,end=' ')
    s =s + i

print(f"\nLa suma de los pares es: {s}")

print("\nProceso terminado")
