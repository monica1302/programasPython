# Imprimir numeros del 1 a n o de n a 1

while(True):
    print("[1] Imprimir numeros ascendentes ")
    print("[2] Imprimir numeros descendentes ")

    op = int( input("\nElige una opción: ") )
    
    if op==1:
        n=int(input(f"\nImprimiendo los numeros de 1 hasta: "))
        for x in range(1,n+1,1):
            print(x,end=' ')

    elif op==2:
        print(f"\nImprimiendo los numeros de n hasta 1\n")
        n= int(input("Dame el valor de n: "))
        for x in range(n,0,-1):
            print(x,end=' ')

    else:
        print("\nOpcion invalida")
    
    res=input("\nDesea continuar:  ").upper()
    if res== "N":
        break

print("\nProceso terminado")