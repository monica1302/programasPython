#Funcion de conversion de unidades metricas

def ci(n):
    cm=0
    cm= n * 2.54
    return cm

def mp(n):
    ft=0
    ft= n* 3.281
    return ft

print ("Conversor de unidades")
print ("[1] Convertir de pulgadas a centimetros")
print ("[2] Convertir de metros a pies")

op=int(input("Elige una opción: "))

if op==1:
    n = int (input ("Cantidad a convertir: "))  
    print("Conversion:",ci(n), "cm")
elif op==2:
    n = int (input ("Cantidad a convertir: "))  
    print("Conversion:", mp(n), "ft")
else:
    print("OPCION INVALIDA")


print ("\nProceso terminado")
