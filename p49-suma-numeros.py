# Imprimir la suma y el promedio de n numeros introduccidos 

while(True):
    n = int(input("\nCuantos numeros deseas ingresar: "))
    suma = 0

    for i in range(1,n+1):
        num = int(input(f"Número {i}: "))
        suma += num

    prom=suma/n
    print(f"La suma es: {suma}")
    print(f"El promedio es: {prom}")

    res=input("\nDesea continuar:  ").upper()
    if res== "N":
        break

print("\nProceso terminado")


