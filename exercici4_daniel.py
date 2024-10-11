import numpy as np

def exercici4():
    #Part 1: Crearà una matriu de 3x4 de números aleatoris de 0 a 80
    print("Matriu de 3x4 creada amb numeros al atzar entre 0 i 80")
    matriu1 = np.random.randint(80, size=(3, 4))
    print(matriu1,"\n")

    #Part 2: Modificar l’anterior matriu: La nova matriu ha de ser de 4x3 i la última fila passa a ser la última columna
    ultimaColumnaM1 = matriu1[:, -1]    #Guardem l'ultima coulumna
    matriu2 = matriu1
    matriu2 = np.delete(matriu2, -1, axis=1)    #Eliminem la columna
    matriu2 = np.insert(matriu2, len(matriu2), ultimaColumnaM1, axis=0) #Afegim fila nova
    print("Matriu anterior pero modificada a 4x3 utilitzant l'ultima columna com a ultima fila")
    print(matriu2,"\n")


    #Part 3:
    ultimNumero = matriu2[0,2]
    columnaNova = np.array([ultimNumero, ultimNumero, ultimNumero, ultimNumero])
    #print(columnaNova)
    matriu3 = matriu2
    matriu3 = np.insert(matriu3, len(matriu3)-1, columnaNova, axis=1)
    print("Matriu anterior modificada afegint una ultima columna agafant el primer valor de l'ultima columna")
    print(matriu3,"\n")

exercici4()