import random

nombreAleatori = random.randint(1, 100)

nombreUsuari = int(input("Escull un nombre entre 1 i 100: "))

intents = 1

while nombreUsuari > 100:
    nombreUsuari = int(input("El nombre és massa gran, tria un altre"))

while nombreUsuari != nombreAleatori:
    if nombreUsuari > nombreAleatori:
        print("Intents: " + str(intents))
        nombreUsuari = int(input("Massa gran! Tria un de més petit: "))
        intents += 1
    elif nombreUsuari < nombreAleatori:
        print("Intents: " + str(intents))
        nombreUsuari = int(input("Massa petit! Tria un de més gran: "))
        intents += 1

print("Correcte! Has endevinat el número secret")
print("Intents totals: " + str(intents))

