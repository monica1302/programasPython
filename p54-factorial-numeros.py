# Imprime el factorial de n números

n = int(input("De cuantos numeros desea el factorial: "))
for i in range(1,n+1):
    print(f"{i}! = ", end="")
    f=1
    for j in range(1,i+1):
        print (f"{j} * ", end ="")
        f =f * j
    print(f" = {f}")

print("\nProceso terminado")