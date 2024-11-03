import create
import read
import update
import delete

opcio = 0

print("Crear usuari = 1")
print("Llegir usuaris = 2")
print("Actualitzar usuari(tot) = 3")
print("Actualitzar usuari(nom) = 4")
print("Actualitzar usuari(cognom) = 5")
print("Actualitzar usuari(edat) = 6")
print("Actualitzar usuari(email) = 7")
print("Esborrar usuari = 8")

opcio = int(input("Selecciona una opcio: "))

if(opcio == 1):
    name = input("Introdueix el nom: ")
    surname = input("Introdueix el cognom: ")
    age = int(input("Introdueix l'edat: "))
    email = input("Introdueix el correu electrònic: ")
    user_id = create.crear_usuari(name, surname, age, email)
