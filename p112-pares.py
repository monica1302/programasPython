def pares(lista):
    p = []
    for n in lista:
        if n % 2 == 0:
            p.append(n)
    return p

def leer():
    lista=[]
    while True:
        n=int(input("Numero:"))
        if n==-1:
            break
        lista.append(n)
    return lista

#Programa principal
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = pares(nums)
print("Los pares son ", res)

lista=leer()
print (lista, len(lista))
res = pares(lista)
print("Los pares son ", res)

print ("\nProceso terminado")
