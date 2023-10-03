# Cambiar los elementos de una lista

nums = [10, 9, 8.5, 6.5, 9.8, 7, 5, 6.2, 9.5]
print(f"Todos los números : {nums}")
nums[0]=7
nums[1]=7
print(f"Modificar 0 y 1 : {nums}")
nums[2:5] = [9,9,9]
print(f"Modificar 2:5 - : {nums}")