numeros = input("Insereix 10 números separats per espais: ")
llista = (numeros.split(' '))
llistaNumeros = [int(x) for x in llista]
print("Números de l'usuari" + str(llistaNumeros))

sumaTotal = sum(llistaNumeros)
print("Suma total: " + str(sumaTotal))
llistaNumeros.append(sumaTotal)

mitjana = sum(llistaNumeros) / 10
print("Mitjana: " + str(mitjana))
llistaNumeros.append(mitjana)


print("Llista afegint la suma total i la mitjana: " + str(llistaNumeros))