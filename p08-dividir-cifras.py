# Dividir un numero entero de 3 cifras en centenas, decenas y unidades
#491

print("Dividir en unidades, decenas y centenas un numero entero")
numero = int(input("Dame un número de 3 cifras: "))

centenas = numero // 100 
decenas = (numero - centenas * 100) // 10 
unidades = numero - (centenas * 100 + decenas * 10)

print(f"centenas: {centenas}, decenas: {decenas}, unidades: {unidades}")
print(f"Suma digitos : {centenas+decenas+unidades}")