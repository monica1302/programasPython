def leer():
    lista=[]
    while True:
        n=int(input("Numero:"))
        if n==0:
            break
        lista.append(n)
    return lista

def sumadigitos(n):
    sumlist=[]
    for n in lista:
        suma = 0
        for d in str(n):
            suma += int(d)
        sumlist.append(suma)
    return sumlist

lista=leer()
print ("Lista original: ",lista)

suma=sumadigitos(lista)
print("Suma de digitos de la lista: ",suma)

print ("\nProceso terminado")