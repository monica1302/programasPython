#Imprime los numeros del x a 1

x=int(input("Desde donde comenzar a descender:"))
y=int(input("De cuanto en cuanto: "))

for n in range(x,0,-y):
    print(n,end=' ')


print("\nProceso terminado")