#Calcular el numero mayor de una serie introducidos

mayor=0

while(True):
    while(True):
        num = int(input("Numero: "))
        if num>mayor:
            mayor=num
            
        if num != 0:
            continue
        else:
            break

    print("El numero mayor es:", mayor) 
    res=input("\nDesea continuar:  ").upper()
    if res== "N":
        break

print("\n Proceso terminado")
