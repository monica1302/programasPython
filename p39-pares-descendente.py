#Imprimir numeros pares de forma descendente y sumarlos

print("Imprimir y sumar numeros descendentes pares\n")

suma=0
c=100
n= int(input("Hasta que numero quieres imprimir: "))


while(True):
    while c >= n:
        c=c-1
        if c%2 ==0:
            print(c, end=" ")
            suma += c      
    print(f"\nSuma: {suma}")
    res=input("Deseas Continuar(S/N):  ").upper()
    if res=='N':
        break
print("\n Proceso terminado")