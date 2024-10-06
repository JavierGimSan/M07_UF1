factors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numero = int(input("Introdueix un número de l'1 al 10: "))

for x in range (0, factors[len(factors)-1], 1): # Faig un bucle for on vaig iterant per la llista factors i multiplicant 
                                                # cada element de la llista pel número introduit per l'usuari.
    print(numero * factors[x])
