#Sumar numeros introducidos hasta la la suma sea >= 200

while(True):
    cuenta = suma = 0
    while(True):
        num = int(input("Numero: "))
        cuenta += 1;
        suma += num
        if suma >= 200:
            print("\n")
            break
       
    
    print(f"Se introdujeron {cuenta} numeros")
    print("La suma de los numeros es: ", suma)
    res=input("Deseas Continuar(S/N):  ").upper()
    if res=='N':
        break

print("\n Proceso terminado")