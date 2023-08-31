#Dada una cantidad en horas, calcular su equivalente en días, minutos y segundos

print("Dada una cantidad en horas, calcular su equivalente en días, minutos y segundos")
print("Dime las horas: ")

horas = int(input())

minutos = horas * 60
segundos = minutos * 60
dias = horas / 24

print(f"\n{horas} hrs equivale a {minutos} minutos, {segundos} segundos y {dias:.2f} dias. ")
