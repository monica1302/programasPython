# Cuenta números, los suma, cuenta positivos, negativos y ceros, parar con 999

cuenta = suma = cp = cn = cc= 0

print("Cuenta números, los suma, cuenta positivos, negativos y ceros, parar con 999\n")

while(True):
    num = int(input("Numero: "))
    if num != 999:
        cuenta += 1;
        suma += num
        if num > 0:
            cp += 1
        elif num <0 :
            cn += 1
        else:
            cc += 1

    else:
        break

print(f"Se introdujeron {cuenta} numeros")
print("Positivos: ", cp)
print("Negativos: ", cn )
print("Ceros : ", cc)
print("La suma de los numeros es", suma)

print("\n Proceso terminado")