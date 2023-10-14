#Diccionario con los dias de la semana

semana={
    1:"Lunes",
    2:"Martes", 
    3:"Miercoles", 
    4:"Jueves", 
    5:"Viernes", 
    6:"Sabado", 
    7:"Domingo"
}

print(f"\nDiccionario: {semana}\n")

print("Primer elemento: " , semana[1])
print("Ultimo elemento: " , semana[7])
print("Quinto elemento: ", semana.get(5))
print("Septimo elemento: ", semana.get(7))

print("\nDiccionario:")
for k,v in semana.items():
    print(f"{k:<2} : {v}")


print("\nProceso terminado")
