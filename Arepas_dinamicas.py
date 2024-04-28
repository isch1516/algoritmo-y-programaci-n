harina = float(input("Harina (en tazas): "))
agua = float(input("Agua (en tazas): "))
sal = float(input("Sal (en cucharadas): "))

# Calcula la cantidad de masa de arepas
cantidad_masa = (harina*0.5 + agua*0.5 + sal*0.25) * 100  # en gramos

# Imprime la cantidad de masa resultante
print("La cantidad de masa de su arepa es de: " + str(cantidad_masa) + " gramos.")