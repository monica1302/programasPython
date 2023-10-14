#Diccionario de llaves de cadena paises

mundo= {
    "Argentina":300,
    "Brasil": 200,
    "Colombia":300,
    "Chile":400,
    "Ecuador":500,
    "Bolivia":600,
    "Jammaica":700
}

print("\nDiccionario:", mundo)
mundo["Brasil"]=250
mundo["Chile"]=450
mundo.update({"Bolivia":650})
mundo.update({"Jamaica":750})

print("\nDiccionario modificado:")
for k,v in mundo.items():
    print(f"{k:<10} : {v}")


print("\nProceso terminado")
