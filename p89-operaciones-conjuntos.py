#Permite ejemplificar las operaciones logicas de conjuntos

c1 = {1,2,3,4,5}
c2 = {5,6,7,8,9,10}
c3 = {9,10,11,12,13}
c4 = {3,4,5}

print(f"c1 : {c1}\nc2 : {c2}\nc3 : {c3}\nc4 : {c4}")

print("\nUnion: ")
print(f"Union de c1 - c2 : {c1.union(c2)}")
print(f"Union de c1 - c3 : {c1 | c3}")

print("\nIntersección: ")
print(f"Interseccion c1 - c2: {c1.intersection(c2)}")
print(f"Interseccion c2 - c3: {c2 & c3}")

print("\nDiferencia:")
print(f"Diferencia c1 - c4: {c1.difference(c4)}")
print(f"Diferencia c2 - c3: {c2 - c3}")

print("\nDiferencia simetrica:")
print(f"Diferencia simetrica c1 - c2: {c1.symmetric_difference(c2)}")
print(f"Diferencia simetrica c2 - c3: {c2 ^ c3}")

print("\nProbar por subconjuntos:")
print(f"Subconjunto c4 de c1: {c4.issubset(c1)} ")
print(f"Subconjunto c3 de c2: {c3<=c2} ")

print("\nProbar por supersubconjuntos:")
print(f"Superconjunto c1 de c4: {c1.issuperset(c4)}")
print(f"Superconjunto c2 de c3: {c2>=c3}")

print("\nVerficar la presencia de un elemento en el conjunto:")
print(f" 2 esta en c1: {2 in c1}")
print(f" 6 no esta en c2: {6 not in c1}")

print("\nProceso terminado")