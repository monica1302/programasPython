#Acceder a una lista y modificarla

num= [100, 123, 456, 222, 999, 895, 325, 234, 322, 988 ]
print("Numeros: ", num)
print("El primer elemento: ", num[0])
print("El ultimo elemento: ", num[-1])
print("Elemento 999: ", num[4])
print("Elementos entre 123 a 999: ", num[2:4])
print("Elementos desde inicio hasta 222:", num[:4])
print("Elementos desde 222 hasta el final: ", num[3:])
nnum = list(map(lambda n: -n, num))

print("Los ultimos tres elementos usando inidice negativo: ", nnum[6:])

print("\nProceso terminado")