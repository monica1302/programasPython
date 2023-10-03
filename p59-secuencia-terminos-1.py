#Imprimir la secuencia de términos armónicos el numero de renglones que el usuario desee y su suma

n = int(input("\nDame el numoeri el cual deseas el factorial: "))
f = 1
s=0

for i in range(1,n+1):
    print(f"1/{i}! + ", end="")
    f=1
    
    for j in range(1,i+1):
        f =f * j
    f=1/f
    s+=f

    if i==n:
        print (f"= {s:.3f}")
print("\nProceso terminado")