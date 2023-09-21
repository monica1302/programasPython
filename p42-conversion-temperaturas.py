#Imprimir tabla de conversion de grados centigrados a grados farenheit

while(True):
    while(True):
        pi=float(input("Valor inicial:  "))
        pf=float(input("Valor final:  "))
        if (pi < pf):
            break
    
    c= pi
    print("Centigrados \t Farenheit")
    print ("-"*20)
    while (c <= pf):
        print(f"{c}\t {( c * 9 / 5 ) + 32:.2f}")
        c= c+ 1
    print ("-"*20)
    res=input("Desea continuar:  ").upper()
    if res== "N":
        break

print("\nProceso terminado")

