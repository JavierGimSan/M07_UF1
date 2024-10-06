numeros = input("Introdueix 10 números separats per un espai: ").split(' ') # Separo els elements pels espais.
llistaEnters = [int(x) for x in numeros] # Faig una llista on passo els elements a enters
myTupla = tuple(sorted(llistaEnters)) # Ara puc ordenar els elements de la llista per valor numèric
print(myTupla)
