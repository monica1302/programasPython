# Imprime el factorial de un número

n = int(input("Dame el numoeri el cual deseas el factorial: "))
f = 1
for h in range(1,n+1):
    print(h, end = " * ")
    f = f * h

print(f"\nEl factorial es: {f}")

print("\nProceso terminado")