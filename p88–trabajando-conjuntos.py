# Operaciones sobre conjuntos

m = {"Zacatecas", "Guadalupe","Jerez","Fresnillo"}

print(f"\nLa colección es del tipo : {type(m)}")
print(f"Longitud del conjunto : {len(m)}")
print(f"El conjunto original : {m}")
print("\nLista de municipios usando un ciclo: ")
for mun in m:
    print(mun,end=' ')

print(f"\nEsta Zacatecas en el conjunto: {'Zacatecas' in m}")

print("\nAgregra elementos a un conjunto:")
m.add("Teul")
print(f"Agregar a Teul :{m}")
otrosm = {"Luis Moya","Ojocaliente","Tepetongo"}
m.update(otrosm)
print(f"Agregrar a Luis Moya, Ojocaliente, Tepetongo: \n{m}\n")

print("\nEliminar elementos del conjunto:")
m.remove("Zacatecas")

print(f"Eliminar a Zacatecas: {m}")
m.discard("Ojocaliente")
print(f"Eliminar a Ojocaliene: {m}")
mun=m.pop()
print(f"Eliminar al primero: {m} - elemento eliminado {mun}")
m.clear()
print(f"Eliminar: {m}")

print ("\nProceso terminado")

