#Imprimir una tabla de conversion de Peso a Dolar y Libra

tcd= 19.13
tcl= 21.22

while(True):
    while(True):
        pi=float(input("Valor inicial:  "))
        pf=float(input("Valor final:  "))
        if (pi < pf):
            break
    
    c= pi
    print("Peso \t Dolar \t Libra")
    print ("-"*25)
    while (c <= pf):
        print(f"{c}\t {c/tcd:.4f}\t {c/tcl:.4f}")
        c= c+ 1
    print ("-"*25)
    res=input("Desea continuar?  ").upper()
    if res== "N":
        break

print("\nProceso terminado")


