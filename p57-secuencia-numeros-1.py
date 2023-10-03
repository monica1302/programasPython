#Imprimir secuencia de numeros mostrados en cada renglon

n = int(input("Dame un numero: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end="  ")
    print()

print("\nProceso terminado")