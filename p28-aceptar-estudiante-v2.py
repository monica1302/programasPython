#Aceptar a un estudiante segun sus datos

nombre = input("Cual es tu nombre: ")

print("[0] Hombre")
print("[1] Mujer")

op = int(input("Sexo:"))


if op==0:
    print("Lo sentimos, solo aceptamos mujeres")

elif op==1:
    edad = int(input("Cual es tu edad: "))
    if edad >= 21:
        print("Dame 3 calificaciones: ")
        n1, n2, n3 = int(input()), int(input()), int(input()) 
        suma = n1+n2+n3
        prom= suma/3

        if 8 < prom <= 9.5:
            print(f"Felicidades {nombre}, has sido aceptado en Universidad Kitty Kat SA")
        else:
            print("Lo sentimos, tu promedio no es aaceptado")

    else:
        print("Lo sentimos, solo aceptamos mujeres mayores de 21 años")
else :
    print("\nOPCION INVALIDA")

print("\nProceso terminado")