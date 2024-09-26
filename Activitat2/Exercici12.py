nombre = int(input("Introdueix un número: "))
suma = 1
solucio = 0

for suma in range(1, nombre+1, suma):
    solucio +=suma

print("La suma total és: " + str(solucio))