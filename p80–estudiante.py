# Estudiante

estudiante = {
    "Nombre":"Juan Perez",
    "Edad":45,
    "Email":"jperez@msn.com",
    "Carrera":"Sistemas"
}

print(f"\nEl diccionario: \n\n{estudiante}")
estudiante["Calificacion"]=9.5
estudiante["Email"]="juanp@gmail.com"
print(f"\nEl diccionario actualizado: \n\n{estudiante}")

print("\nLas llaves: \n")
for k in estudiante.keys():
    print(k)

print("\nLos valores: \n")
for v in estudiante.values():
    print(v)

print("\nLlaves y valores:\n")
for k,v in estudiante.items():
    print(f"{k:<12} : {v}")


print("\nProceso terminado")