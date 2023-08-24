#lee datos del usuario y envia un saludo a pantalla

print("Leyendo datos y enviando un mensaje")

nombre= input ("Dame tu nombre: ")
edad = input ("Dame tu edad: ")
peso = float(input("Dame tu peso: "))

print(f"\nTu nombre es {nombre}, de {edad}, con un peso de {peso}")

print(type(nombre))
print(type(edad))
print(type(peso))