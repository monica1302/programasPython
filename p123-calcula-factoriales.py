def leer():
    lista=[]
    while True:
        n=int(input("Numero:"))
        if n==0:
            break
        lista.append(n)
    return lista

def factorial(n):
    faclist=[]
    for n in lista:
        fac=1
        for d in range(1,n+1):
            fac*=int(d)
        faclist.append(fac)
    return faclist

lista=leer()
print ("\nLista original:   ",lista)

fac=factorial(lista)
print(f"El factorial  es: ", fac)

print ("\nProceso terminado")
