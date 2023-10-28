#Funcion para decifrar el dia de la semana por medio de un numoer del 1 al 7


def semana(n):
    dia=""
    if n==1:
        dia="Lunes"
    elif n==2:
        dia="Martes"
    elif n==3:
        dia="Miercoles"
    elif n==4:
        dia="Jueves"
    elif n==5:
        dia="Viernes"
    elif n==6:
        dia="Sabado"
    elif n==7:
        dia="Domingo"
    else:
        dia="Error"
    return dia
    
#Programa principal
n=int(input("Dame un numero del 1 al 7: "))
print(f"El dia de la semana es: {semana(n)}")

print ("\nProceso terminado")
