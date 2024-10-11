areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

print(areas_pis[1])

print(areas_pis[-1])

print(areas_pis[areas_pis.index("Terrassa")+1]) #busco la posició del'element "terrassa" i vaig al següent element, qué és l'àrea.

print(areas_pis[0:3])

print(areas_pis[2:])

print(areas_pis[areas_pis.index("Habitació1")+1] + areas_pis[areas_pis.index("Habitació2")+1])

areas_pis[areas_pis.index("Lavabo")+1] = 10
print(areas_pis)

areas_pis.extend(["pati interior", 2.78])
print(areas_pis)

area_total = areas_pis[1::2] #Faig una nova list desde l'element a la posició 1 fins al final, i els afegeixo de 2 en 2.
print(sum(area_total)) #Sumo tots els elements de la nova list, que són les àrees.

