
def suma(n1,n2,op):
    s=0
    if op=="P":
        if n1%2==0:
            for i in range(n1,n2+1,2):
                s += i
        else:
            for i in range(n1-1,n2+1,2):
                s += i
    elif op=="I":
        if n1%2==0:
            for i in range(n1+1,n2+1,2):
                s += i
        else:
            for i in range(n1,n2+1,2):
                s += i
    else:
        print("OPCION INVALIDA")

    return s


print("Suma de un rango de numeros")

n1=int(input("Numero de inicio: "))
n2=int(input("Numero de fin: "))

print("[P] Sumar numeros pares ")
print("[I] Sumar numeros impares")
op=input("Eliga opcion: ").upper()
print("\nLa suma es:", suma(n1,n2,op))

print ("\nProceso terminado")

