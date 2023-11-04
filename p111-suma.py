def suma(lista):
    s = 0
    for n in lista:
        s += n
    return s

#Programa principal
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
res = suma(nums)
print("La suma es: ", res)

lista=[]
while True:
    n=int(input("Numero:"))
    if n==-1:
        break
    lista.append(n)

print (lista, len(lista))
res = suma(lista)
print("La suma es: ", res)

print ("\nProceso terminado")

