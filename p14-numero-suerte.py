#Dado el año de nacimiento, la suma de sus dígitos individuales es el número de la suerte. 

print("Numero de la suerte")
print("En que año naciste: ")

año = int(input())

dig1 = año // 1000 
dig2 = (año - dig1 * 1000) // 100 
dig3 = (año -dig1 *1000 - dig2 *100)//10
dig4 = (año -dig1 *1000 - dig2 *100 - dig3 *10)

suerte= dig1+dig2+dig3+dig4

print(f"Tus digitos individuales son: {dig1,dig2,dig3,dig4}, y tu numero de la suerte es: {suerte}")