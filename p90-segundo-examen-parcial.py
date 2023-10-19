#Segundo examen parcial 

print("\nBIENVENIDO A PIZZERIA PIZZA")
print("El precio base es de $15.00, en la compra de mas de $30.00 recibe un descuento del 5%")
print("\nIngredientes extras: \nT(Tomate)   - $1.50 \nP(Peperoni) - $3.50\nA(Aguacate) - $0.40\nQ(Queso     - $3.74\nI(Piña)     - $2.10")

i ={
    "T":1.50,
    "P":3.50,
    "A":0.40,
    "Q":3.74,
    "I":2.10
}

lista=[]
cuenta=15
cuentad=0

e=input("\nDesea agregar ingredientes extra a su pizza:").upper()
if e == "S":
    n=int(input("Cuantos extras: "))

    for x in range(n):
        extra = input("Ingrediente extra: ").upper()
        lista.append(extra) 

        if extra=="T":
            cuenta= cuenta + i["T"]
        elif extra=="P":
            cuenta= cuenta + i["P"]
        elif extra=="A":
            cuenta= cuenta + i["A"]
        elif extra=="Q":
            cuenta= cuenta + i["Q"]
        elif extra=="I":
            cuenta= cuenta + i["I"]
        else:
            print("Ingrediente no valido")
        
        cuenta=+ cuenta

    print("\nIngredientes agregados: ",lista)

    
else:
    print("El precio base es de $15.00, en la compra de mas de $30.00 recibe un descuento del 5%")
    for k,v in i.items():
        print(f"{k:<2} : {v}")

print("\nResumen de pedido")
print(f"Subtotal: ${cuenta:.2f}")
if cuenta > 30:
    cuenta= cuenta *0.95
    
print(f"Total: ${cuenta:.2f}")




