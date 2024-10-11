mesos = ('gener', 'febrer', 'març', 'abril', 'maig', 'juny', 'juliol', 'agost', 'setembre', 'octubre', 'novembre', 'desembre')

numMes = 1
while(numMes != 0): 
    numMes = int(input("Introdueix un número de l'1 al 12: "))
    if(numMes == 0):
        print("Número invàlid")
    else:
        print(mesos[numMes-1])
    

