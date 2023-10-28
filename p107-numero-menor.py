#Funcion para devolver el menor de 3 numeros 

def Nmenor(n1,n2,n3):
    menor=0
    if n1<n2 and n1<n3:
        menor=n1
    elif n2<n1 and n2<n3:
        menor=n2
    else:
        menor=n3
    return menor

#Programa principal
print("Dame 3 numeros: ")
n1,n2,n3=int(input()),int(input()),int(input())
print("El menor de los 3 numero es: ",Nmenor(n1,n2,n3))


print ("\nProceso terminado")
