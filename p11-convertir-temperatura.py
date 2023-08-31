#Dada una temperatura en grados celcius, otener su equivalente en grados fahrenheit

print("Que temperatura quiere convertir a grados fahrenheit: ")
celcius= float(input())

fahrenheit=(celcius * 9/5) + 32

print(f"\n{celcius} grados celcius equivale a {fahrenheit} grados fahrenheit")