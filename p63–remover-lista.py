# Remover elementos de la lista

nums = [1, 3, 5, 7, 9, 11, 99, 15, 88, 19, 100]
print(f"Todos los números : {nums}")
nums.remove(99)
print(f"Remover primera ocurrencia : {nums}")
num=nums.pop(8)
print(f"Remover y regresar elemento : {nums} - {num}")
num=nums.pop()
print(f"Remover el ultimo: : {nums} - {num}")
nums.clear()
print(f"Remover todos : {nums}")

print("\nProceso terminado")