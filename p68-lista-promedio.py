#Calcular el promedio de una lista


print("Introduce numeros enteros, 99 para terminar:\n")
nums=[]
n=suma=prom=0
while n!=99:
    n = int(input("Numero: "))
    nums.append(n)
    suma+=n
    
prom=suma/len(nums)
mp=[]
for n in nums:
    if n>prom:
        mp.append(n)

print(f"Lista : {nums}")
print(f"Suma : {suma}")
print(f"Promedio : {prom:.2f}")


print("\nProceso terminado")
