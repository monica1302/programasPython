
datos={
    "Apozol":1863,
    "Calera":1868,
    "Fresnillo":1554,
    "Guadalupe":1824,
    "Jalpa":1824,
    "Jerez":1824,
    "Loreto":1931,
    "Mazapil":1824,
    "Momax":1857,
}

print(f"\nDiccionario: {datos}\n")
datos.pop("Apozol")
datos.pop("Fresnillo")
datos.popitem()
datos.clear()

print("\nDiccionario modificado:")
for k,v in datos.items():
    print(f"{k:<10} : {v}")

print("\nProceso terminado")

