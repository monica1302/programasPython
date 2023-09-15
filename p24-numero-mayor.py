#Dados 3 numeros identificar cual es el mayor

print("Dame 3 numeros enteros: ")
n1, n2, n3 = int(input()), int(input()), int(input())

if n1 < n2 > n3:
    print(f"{n2} es mayor")
if n2 < n3 > n1:
    print(f"{n3} es mayor")
if n3 < n1 > n2:
    print(f"{n1} es mayor")

print("\nProceso terminado")
