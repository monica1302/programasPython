#Imprime los pares y su suma/ Imprime impares y su suma

while(True):
    n = int(input("Hasta donde deseas los numeros: "))
    s = 0
    print("\nNumeros pares:")
    for i in range(1,n+1,2):
        print(i,end=' ')
        s += i

    print(f"\nSuma pares: {s}")
    s = 0
    print("\nNumeros impares:")
    for i in range(2,n+1,2):
        print(i,end=' ')
        s += i
    print(f'\nSuma impares: {s}')

    res=input("\nDesea continuar:  ").upper()
    if res== "N":
        break

print("\nProceso terminado")

