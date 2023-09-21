# Calcula la conjetura de Collatz

while(True):
    print("Imprime la conjetura de collatz")
    num = int(input('Dame un número = '))

    while num != 1:
        print(num,end=" ")
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1

    print(num,end=" ")
    res=input("\nDeseas Continuar(S/N)? ").upper()
    if res=="N":
        break

print("\nProceso terminado")