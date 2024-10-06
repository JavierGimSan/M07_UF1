frase = input("Introdueix una frase: ")
myTupla = tuple(frase.replace(' ', ''))
print("Tupla sense espais: " + str(myTupla))
fraseSenseRepetits = ""
for x in range(0, len(myTupla)-1, 1):
    if str(myTupla[x]) in fraseSenseRepetits:
        x = x+1
    else:
        fraseSenseRepetits = fraseSenseRepetits + myTupla[x]
        

print("Tupla sense repetits: " + fraseSenseRepetits)




# fraseLlistaSenseEspais = fraseLlista[0].replace(' ', '')
# fraseLlistaSenseRepetits = []
# for x in range(1, len(fraseLlistaSenseEspais[0])-1, 1):
#     if(fraseLlistaSenseEspais[0][x] not in fraseLlistaSenseRepetits):
#         fraseLlistaSenseRepetits.append(fraseLlistaSenseEspais[0][x])

# print(fraseLlistaSenseRepetits)
