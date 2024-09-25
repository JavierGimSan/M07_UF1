paraules = input("Introdueix d'1 a 3 paraules separades per un espai: ").split(' ')

if len(paraules) > 3:
    print("Nombre de paraules fora del marge")
else:
    index = 0
    for index in range(0, len(paraules), 1):
        longitudParaula = len(paraules[index])
        print("Longitud de la paraula " + " \"" + str(paraules[index]) + "\" " + ": " + str(longitudParaula))
        print("Primera lletra: " + (paraules[index])[0])
        print("Última lletra: " + (paraules[index])[len((paraules[index]))-1])