# Conversión de grados celious a grados fahrenheit y viceversa

print("Conversión de temperaturas de grados centigrados a grados Fahrenheit")
opcion = str.upper( input("Convertir a grados [C]entigrados o [F]ahrenheit") )

if opcion == 'C':
    print("\nConvirtiendo de Fahrenheit a centigrados\n")
    temp = float(input("Grados Fahrenheit: "))
    fc = (temp - 32) * 5 / 9
    print(f"{temp} grados Fahrenheit equivalen a {fc:.2f} grados Centigrados")
else :
    print("\nConviritiendo de Centigrados a Fahrenheit ")
    temp = float(input("Dame los Centgrados "))
    cf = ( temp * 9 / 5 ) + 32
    print(f"{temp} grados Fahrenheit, equivalen a {cf:.2f} grados Centigrados")

print("\n Proceso terminado")

