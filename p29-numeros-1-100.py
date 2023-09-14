# Imprimir los numeros del 1 al 100

n=int(input("Hasta donde deseas llegar: "))
p=int(input("Que intervalos deseas: : "))

c = 1
while c <= n :
    print(c, end=" ")
    c=c+p

print("\n Proceso terminado")