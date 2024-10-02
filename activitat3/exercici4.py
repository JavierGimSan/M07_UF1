numeros = input("Introdueix 10 números separats per un espai: ").split(' ')
llistaEnters = [int(x) for x in numeros]
myTupla = tuple(sorted(llistaEnters))
print(myTupla)
