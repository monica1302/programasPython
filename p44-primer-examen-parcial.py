#Calcular resumen de ventas para un evento academico 

print("Universidad Patito SA de CV")
print("Sistema de Inscripciones al Congreso de Sistemas")
total=0

while(True):
    usuario = int(input("\nTipo de usuario: [1] Alumno $100.00, [2] Trabajador $200.00, [3] Docente $500.00 ?  "))
    paquete = int(input("Tipo de paquete:[1] Solo conferencias $600.00, [2] Con evento sociales $800.00, [3] Con kit de acceso $900.00 ?  "))

    if usuario==1:
        cuenta=100
        if paquete==1:
            cuenta= cuenta+600

        elif paquete==2:
            cuenta= cuenta+800

        elif paquete==3:
            cuenta= cuenta+900
        
        cantidad= int(input("Cantidad requerida: "))
        cuenta=cuenta* cantidad

        if cuenta >= 5000:
            descuento= cuenta*0.20
            cuenta= cuenta* 0.8 
            print(f"Se aplico un descuento de ${descuento:.2f} (20%), quedando un subtotal de ${cuenta:.2f}")
            total +=cuenta

        else:
            print (f"El subtotal es ${cuenta:.2f}")
            total +=cuenta

    if usuario==2:
        cuenta=200
        if paquete==1:
            cuenta= cuenta+600

        elif paquete==2:
            cuenta= cuenta+800

        elif paquete==3:
            cuenta= cuenta+900
        
        cantidad= int(input("Cantidad requerida: "))
        cuenta=cuenta* cantidad

        if cuenta >= 5000:
            descuento= cuenta*0.10
            cuenta= cuenta* 0.9 
            print(f"Se aplico un descuento de ${descuento:.2f} (10%), quedando un subtotal de ${cuenta:.2f}")
            total +=cuenta

        else:
            print (f"El subtotal es ${cuenta:.2f}")
            total +=cuenta

    if usuario==3:
        cuenta=500
        if paquete==1:
            cuenta= cuenta+600

        elif paquete==2:
            cuenta= cuenta+800

        elif paquete==3:
            cuenta= cuenta+900
        
        cantidad= int(input("Cantidad requerida: "))
        cuenta=cuenta* cantidad

        if cuenta >= 5000:
            descuento= cuenta*0.05
            cuenta= cuenta* 0.95
            print(f"Se aplico un descuento de ${descuento:.2f} (5%), quedando un subtotal de ${cuenta:.2f}")
            total +=cuenta

        else:
            print (f"El subtotal es ${cuenta:.2f}")
            total +=cuenta
   
    res=input("\nDesea continuar:  ").upper()
    if res== "N":
        break

print("\nEl total de la compra es: $", total)
print("\nProceso terminado")
