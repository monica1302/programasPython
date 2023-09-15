#Dado un numero imprimir el dia de la semana con letra

n=int(input("Teclea con numero que dia de la semana quiere saber: "))

if n >=1 and n <= 7:
    if n == 1:
        print("Domingo")
    if n == 2:
        print("Lunes")
    if n == 3:
        print("Martes")
    if n == 4:
        print("Miercoles")
    if n == 5:
        print("Jueves")
    if n == 6:
        print("Viernes")
    if n == 7:
        print("Sabado")
else:
    print("ERROR")

print("\nProceso terminado")