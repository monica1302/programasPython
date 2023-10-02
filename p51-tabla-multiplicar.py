#Imprimir la tabla de multiplicar que el usuario pida con ciclo for

while(True):

    t = int(input("Que tabla deseas: "))
    n = int(input("Hasta donde la deseas: "))
    for i in range(1, n+1):
        print(f'{t} x {i} = {t*i}')

    res=input("\nDesea continuar:  ").upper()
    if res== "N":
        break

print("\nProceso terminado")
