# Imprime las tablas de 1 a n, hasta m

while(True):
    n = int(input("Hasta que tabla quieres: "))
    m = int(input("Hasta donde la quieres: "))
    t=1

    while t <= n:
        print(f"\nTabla del {t} \n")
        c=1 
        while( c <= m ):
            print(f"{t} x {c} = {t*c}")
            c+=1
        t+=1
    res=input("\nDeseas Continuar(S/N)? ")
    if res.upper()=="N":
        break

print("\nProceso terminado")