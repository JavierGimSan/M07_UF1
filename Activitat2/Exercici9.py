paraula1 = input("Introdueix una paraula: ")
paraula2 = input("Introdueix una altra: ")
paraula1canvi = paraula2[0] + paraula2[1]
paraula2canvi = paraula1[0] + paraula1[1]


for index in range (2, len(paraula1)):
    paraula1canvi = paraula1canvi + paraula1[index]

print(paraula1canvi)

for index in range (2, len(paraula2)):
    paraula2canvi = paraula2canvi + paraula2[index]

print(paraula2canvi)