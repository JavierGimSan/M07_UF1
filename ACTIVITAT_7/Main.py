import psycopg2
import create
import read
import update
import delete

try:
    conn = psycopg2.connect(
    database="postgres",
    user='javier_gimenez',
    password='javi123',
    host='localhost',
    port='5432'
    )

    connection = conn.cursor()
    opcio = 0

    print("Crear usuari = 1")
    print("Llegir usuaris = 2")
    print("Actualitzar usuari(tot) = 3")
    print("Actualitzar usuari(nom) = 4")
    print("Actualitzar usuari(cognom) = 5")
    print("Actualitzar usuari(edat) = 6")
    print("Actualitzar usuari(email) = 7")
    print("Esborrar usuari = 8")
    print("Sortir = 9")

    while(opcio != 9):
        opcio = int(input("Selecciona una opcio: "))

        if(opcio == 1):
            name = input("Introdueix el nom: ")
            surname = input("Introdueix el cognom: ")
            age = int(input("Introdueix l'edat: "))
            email = input("Introdueix el correu electrònic: ")
            user_id = create.crear_usuari(name, surname, age, email)
        elif(opcio == 2):
            users = read.llegir_usuari()
            for user in users:
                print(user)
        elif(opcio == 3):
            user_id = int(input("Introdueix l'id de l'usuari: "))
            user_name = input("Nou nom: ")
            user_surname = input("Nou cognom: ")
            user_age = int(input("Nova edat: "))
            user_email = input("Nou email: ")
            update.actualitza_usuari(user_id, user_name, user_surname, user_age, user_email)
        elif(opcio == 4):
            user_id = int(input("Introdueix l'id de l'usuari: "))
            user_name = input("Nou nom: ")  
            update.actualitza_nom(user_id, user_name)
        elif(opcio == 5):
            user_id = int(input("Introdueix l'id de l'usuari: "))
            user_surname = input("Nou cognom: ")
            update.actualitza_cognom(user_id, user_surname)
        elif(opcio == 6):
            user_id = int(input("Introdueix l'id de l'usuari: "))
            user_age = input("Nova edat: ")
            update.actualitza_edat(user_id, user_age)
        elif(opcio == 7):
            user_id = int(input("Introdueix l'id de l'usuari: "))
            user_email = input("Nou email: ")
            update.actualitza_email(user_id, user_email)
        elif(opcio == 8):
            user_id = int(input("Introdueix l'id de l'usuari: "))
            delete.elimina_usuari(user_id)
        elif(opcio == 9):
            print("Sortint del menú...")
        else:
            print("Introdueix un nombre de la llista d'opcions")
except (Exception, psycopg2.Error) as error:
    print("Error", error)
finally:
    conn.close()