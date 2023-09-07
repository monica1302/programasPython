# Muestra al tipo de angulo
# <90 agudo, =90 recto, >90 y <180 obtuso, =180 llano, >180 y <360 concavo

angulo = int(input("Dame un angulo: "))

if angulo >= 0 and angulo <=360:
   
    if angulo < 90 :
        print("Agudo")
    elif angulo == 90 :
        print("Recto")
    elif angulo > 90 and angulo < 180 :
        print("Obtuso")
    elif angulo == 180 :
        print("Llano")
    elif angulo > 180 and angulo < 360 :
        print("Concavo")
else :
    print("angulo fuera de rango")


print("\nProceso terminado")
