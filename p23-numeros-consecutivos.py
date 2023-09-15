#Imprimir si tres numeros son consecutivos o no
#9 10 11 consecutivos
#4 6 8 no consecutivos 

print("Dame 3 numeros enteros: ")
n1, n2, n3 = int(input()), int(input()), int(input())

if  n1 +2 == n2 +1 == n3:
    print("Los numeros son consecutivos")
else:
    print("Los numeros no son consecutivos")

print("Proceso terminado")