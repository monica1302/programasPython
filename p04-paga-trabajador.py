#Calcula el salario de un trabajador 

print("Calculando la paga de un trabajador\n")

nombre = input("Cual es tu nombre: ")
horas = int(input("Cuantas horas se trabajo: "))
paga = float(input("Paga por hora: "))
tasa = 0.03
pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

print("Resumen de pagos:\n")
print(f"El trabajador {nombre}, trabajo {horas} horas, con una paga de {paga} pesos por hora, impuesto de {tasa}%")
print(f"Paga bruta {pagabruta}")
print(f"Impuessto {impuesto}")
print(f"Paga neta {paganeta}")