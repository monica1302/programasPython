#Remover una lista

num=[100, 123, 456, 222, 999, 895, 325, 234, 322, 988]
print("Numeros: ", num)
num.remove(100)
num.remove(123)
num.remove(456)
num.remove(322)
num.remove(988)
nums=num.pop(0)
print(f"Remover y regresar elemento 222: {num} - {nums}")
nums=num.pop()
print(f"Remover el ultimo y mostrarlo : {num} - {nums}")
print("Numero restantes: ", num)

num.clear()
print(f"\nRemover todos : {num}")

print("\nProceso terminado")

