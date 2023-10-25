#Conjuntos

A={50, 60, 70, 80, 90, 100, 200}
B={60, 90, 100, 300, 400, 500}
C={10, 20, 60, 90, 70, 100, 600, 700}

print(f"A : {A}\nB : {B}\nC : {C}\n")

print(f"Union de A - B : {A | B}")
print(f"Union de B - C : {B | C}")
print(f"Diferencia A - C: {A - C}")
print(f"Diferencia simetrica B - C: {B ^ C}")
print(f"Interseccion B - C: {B & C}")
print(f"Subconjunto A de B: {A<=B} ")
print(f"Superconjunto C de A: {C>=A}")
print(f"100 esta en A: {100 in A}")
print(f"60 esta en A: {60 in A}")
print(f"60 esta en B: {60 in B}")
print(f"60 esta en C: {60 in C}")
print(f"900 no esta en C: {900 not in C}")