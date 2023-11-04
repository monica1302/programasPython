from math import sqrt

def leer():
    lista=[]
    while True:
        n=int(input("Numero:"))
        if n==0:
            break
        lista.append(n)
    return lista

def suma(lista):
    s = 0
    for n in lista:
        s += n
    return s

def mayor(lista):
    m = lista[0]
    for n in range(len(lista)):
        if lista[n] > m :
            m = lista[n]
    return m

def menor(lista):
    m = lista[0]
    for n in range(len(lista)):
        if lista[n] < m :
            m = lista[n]
    return m

def media(lista):
    m = 0
    for n in lista:
        m += n
    m=m / len(lista)
    return m

def var(lista):
    m = 0
    for n in lista:
        m += n
    m=m/len(lista)
    v=0
    for n in lista:
        v += (n-m)**2
    v=v/len(lista)
    return v 

def des(lista):
    m = 0
    for n in lista:
        m += n
    m=m/len(lista)
    v=0
    for n in lista:
        v += (n-m)**2
    v=v/len(lista)
    d=sqrt(v)
    return d


lista=leer()
print ("\nLista original:   ",lista)

ma = mayor(lista)
me = menor(lista)
m = media(lista)
v=var(lista)
d=des(lista)

print(f"El menor: ", me)
print(f"El mayor: ", ma)
print(f"La media: ",m )
print(f"La varianza: {v:.4f}")
print(f"La desviacion estandar: {d:.4f} ")
print ("\nProceso terminado")
