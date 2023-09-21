# Imprime la tabla de multiplicar deseada del 1 al n

while(True):
    t = int(input("Que tabla quieres: "))
    n = int(input("Hasta donde la quieres: "))
    c = 1

    while( c <= n):
        print(f"{t} x {c} = {t*c}")
        c= c+1
    res=input("Deseas Continuar(S/N):  ").upper()
    if res=='N':
        break

print("\nProceso terminado")