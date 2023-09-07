#Aceptar a un estudiante en base a la edad y sus calificaciones

nombre = input("Cual es tu nombre: ")
edad = int(input("Cual es tu edad: "))

if edad<18 :
    print("Lo sentimos. Solo se aceptan mayores de edad")

else :
    print("Dame 2 calificaciones: ")
    c1, c2 = int(input()), int(input())

    if c1<8 or c2<8 :
        print("Lo sentimos, solo aceptamos claificaciones mayores a 8")

    else :
        print(f"{nombre} bienvenid@, tu edad {edad} y calificaciones {c1} y {c2} lo permiten")

print("\nProceso terminado")