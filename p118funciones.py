#Creamos un modulo con las funciones 
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

def promedio(lista):
    s = 0
    for n in lista:
        s += n
    return s / len(lista)

def suma(lista):
    s = 0
    for n in lista:
        s += n
    return s

def leer():
    lista=[]
    while True:
        n=int(input("Numero:"))
        if n==0:
            break
        lista.append(n)
    return lista
