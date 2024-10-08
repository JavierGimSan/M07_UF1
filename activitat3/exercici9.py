assignatures = ["M01", "M02", "M03", "M04", "M05", "M06"]
notes = input("Introdueix 6 notes separades per espais: ").split(' ')
notesInt = [int(x) for x in range(0, len(notes))]

for x in range(0, len(assignatures), 1):
    print("A " + assignatures[x] + " ha tret " + str(notesInt[x]))

dictNotes = {}

for x in range (0, len(assignatures), 1):
    dictNotes[assignatures[x]] = notesInt[x]

print(dictNotes)
