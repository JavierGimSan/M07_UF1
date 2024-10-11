import exercici2 as ex2
import exercici4_daniel as ex4b

'''
EXERCICI 2
'''
#Funcio per mostrar l'informacio d'una matriu
def mostrarInfoMaatriu(matriu):
    print("Array:\n", matriu)
    print("Numero total d'elements: ", matriu.size)
    print("Dimensio matriu (C, F): ", matriu.shape)
    print("Tipus d'elements interns: ", matriu.dtype)
    print("Tamany de la matriu: ", matriu)
    print("\n")

#Crear arrays
a = ex2.crearArray1D()
b = ex2.crearArray2D()
c = ex2.crearArrayND()

#Mostrar info
print("ARRAY 1")
mostrarInfoMaatriu(a)

print("ARRAY 2")
mostrarInfoMaatriu(b)

print("ARRAY 3")
mostrarInfoMaatriu(c)


'''
EXERCICI 4
'''
ex4b.exercici4()