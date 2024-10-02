factors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numero = int(input("Introdueix un número de l'1 al 10: "))

for x in range (0, factors[len(factors)-1], 1):
    print(numero * factors[x])
