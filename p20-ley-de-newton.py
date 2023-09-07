#Segunda ley de newton (fuerza = masa * aceleracion)

print("Calculando los valores de la segunda ley de newton")
print("[1] Calcular la fuerza")
print("[2] Calcular la masa")
print("[3] Calcular la aceleracion")

op = int(input("Que deseas calcular:"))

if op==1:
    print("\nCalculando la fuerza")
    m = float(input("Cual es la masa: "))
    a = float(input("Cual es la aceleración: "))
    f = m * a
    print(f"La fuerza es: {f:.2f}")

elif op==2:
    print("\nCalculando la masa")
    f = float(input("Cual es la fuerza: "))
    a = float(input("Cual es la aceleracion: "))
    m = f / a
    print(f"La mase es: {m:.2f}")

elif op==3:
    print("\nCalculando la aceleración")
    f = float(input("Cual es la fuerza: "))
    m = float(input("Cual es la masa: "))
    a = f / m
    print(f"La aceleración es: {a:.2f}")

else :
    print("\nOPCION INVALIDA")

print("\nProceso terminado")