# Agregar elementos a la lista

nums = [80.3, 12.5, 60.2, 30.4]
otros = [110,120,130]

print(f"Todos los números : {nums}")
nums.append(90)
nums.append(100)
print(f"Agregar al final : {nums}")
nums.insert(4,80)
print(f"Insertar : {nums}")
nums.extend(otros)
print(f"Extender con : {nums}")

print("\nProceso terminado")