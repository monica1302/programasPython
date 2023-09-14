#Imprimir los numeros de 1 a 200 hasta alcanzar la suma de 100

c = 0
s = 0

while c < 200 :
    c = c + 1
    s = s + c
    print(c,end=" ")
    if s >= 1500:
        print("\n")
        break

print(f"Hemos alcanzado el limite {s}, sumando {c} números")

print("\n Proceso terminado")