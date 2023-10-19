#Conjuntos

A={"Juan", "Maria", "Pedro", "Jose", "Rocio"}
B={"Pedro", "Juan", "Pablo", "Mateo", "Esther"}

print(f"A : {A}\nB : {B}\n")

print(f"Union de A - B : {A | B}")
print(f"Interseccion A - B: {A & B}")
print(f"Diferencia A - B: {A - B}")
print(f"Diferencia simetrica A - B: {A ^ B}")
C={"Pablo", "Mateo"}
print(f"Subconjunto C de B: {C<=B} ")
S={"Reynaldo", "Angelica"}
print(f"Superconjunto A de S: {A>=S}")
print(f"Pedro esta en A: {'Pedro' in A}")
print(f"Lilia no esta en B: {'Lilia' not in B}")
