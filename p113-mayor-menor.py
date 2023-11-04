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

def leerdatos():
    datos=[]
    while True:
        d=int(input("Número: "))
        if d==-1:
            break;
        datos.append(d)
    return datos

# Programa principal
nums = leerdatos()
print(f"Lista de números: {nums}")
may = mayor(nums)
men = menor(nums)
print("Resumen estadistico: \n")
print(f"Total numeros : {len(nums)}")
print(f"El menor : {men}")
print(f"El mayor : {may}")

print ("\nProceso terminado")