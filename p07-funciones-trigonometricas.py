# Uso de las funciones trigonometricas en python

import math

print("Calculo de las funciones trigonometricas basicas")
angulo = float(input("Dame un angulo en grados "))

angrad   = math.radians(angulo)
seno     = math.sin(angulo)
coseno   = math.cos(angulo)
tangente = math.tan(angulo)

salida=("Resumen de funciones\n"
f"El seno es:     {seno:.3f}\n"
f"El coseno es:   {coseno:.3f}\n"
f"La tangente es: {tangente:.3f}\n"
f"El angulo de {angulo} grados equivale a {angrad} radianes")

print(salida)
