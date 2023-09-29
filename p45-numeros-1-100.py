#Imprime los numeros del 1 a x

x=int(input("Hasta donde:"))
y=int(input("De cuanto en cuanto: "))

for n in range(1,x+1,y):
    print(n,end=' ')


print("\nProceso terminado")