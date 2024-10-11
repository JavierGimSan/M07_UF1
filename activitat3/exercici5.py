frase = input("Introdueix una frase: ")
myTupla = tuple(frase.replace(' ', ''))
print("Tupla sense espais: " + str(myTupla))
fraseSenseRepetits = ""
for x in range(0, len(myTupla)-1, 1):
    if str(myTupla[x]) in fraseSenseRepetits:
        x = x+1
    else:
        fraseSenseRepetits = fraseSenseRepetits + myTupla[x]
tuplaSenseRepetits = tuple(fraseSenseRepetits)
        
print("Tupla sense repetits: " + str(tuplaSenseRepetits))