myDict = {}
nom = ""
while(nom != "sortir"): #Si l'usuari fica 'sortir' es talla el bucle.
    nom = input("Insereix un nom: ")
    if(nom != "sortir"): #Si l'usuari fica 'sortir', no es fica al bucle IF. Al tornar al while, es tallarà completament
        if(nom in myDict): #Si el nom ja hi és al diccionari, no s'afegirà de nou.
            print("El nom está repetit, no s'afegirà al diccionari")
        else:
            edat = input("Insereix una edat: ") #Si el nom no és 'sortir' ni està repetit, pregunta l'edat i grava ambdòs al diccionari.
            myDict[nom] = edat # key:value, nom:edat
print(myDict) #Un cop hem sortit del bucle, es mostra el diccionari amb les seves claus i valors.