#Convertir numero decimal a numero romano

n=int(input("Teclea un numero del 1 al 10 para saber el equivalente en numero romano: "))

if n >=1 and n <= 10:
    if n == 1:
        print("I")
    if n == 2:
        print("II")
    if n == 3:
        print("III")
    if n == 4:
        print("IV")
    if n == 5:
        print("V")
    if n == 6:
        print("VI")
    if n == 7:
        print("VII")
    if n == 8:
        print("VIII")
    if n == 9:
        print("IX")
    if n == 10:
        print("X")

else:
    print("ERROR")

print("\nProceso terminado")