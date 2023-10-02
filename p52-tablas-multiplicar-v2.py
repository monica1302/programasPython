# Imprime las tablas de la tabla 1 a la tabla n

n = int(input("Hasta que tabla quieres: "))
m = int(input("Hasta donde la deseas: "))

for i in range(1,n+1):
    print (f"\nTable del {i} \n")
    for j in range(1,m+1):
        print(f'{i} x {j} = {i*i}')
print('\n')

print("\nProceso terminado")