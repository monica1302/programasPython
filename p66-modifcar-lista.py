#Modificar una lista

num=[100, 123, 456, 222, 999, 895, 325, 234, 322, 988]
print("Numeros: ", num)
num[0]=200
num[4]=1000
num[-1]=999
num[1:3]=[555,666,777]
print("\nNumeros modificados: ",num)

print("\nProceso terminado")