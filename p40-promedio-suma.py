# Calcular suma y primedio de una serie de numeros

cuenta = suma = 0

print("Calculo de suma y prmedio de una serie de numeros, parar con 0\n")

while(True):
    while(True):
        num = int(input("Numero: "))
        if num != 0:
            cuenta += 1;
            suma += num
        else:
            break
    prom = suma/cuenta
    
    print(f"Se introdujeron {cuenta} numeros")
    print("La suma de los numeros es: ", suma)
    print("El promedio es: ",prom)
    res=input("Deseas Continuar(S/N):  ").upper()
    if res=='N':
        break

print("\n Proceso terminado")