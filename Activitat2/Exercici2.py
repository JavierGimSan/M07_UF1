euros = int(input("Introdueix una quantitat en €: "))
iva = int(input("Introdueix l'IVA corresponent (4%, 10%, 21%): "))
iva4 = euros * 0.04
iva10 = euros * 0.1
iva21 = euros * 0.21

while iva not in[4, 10, 21]:
    iva = int(input("IVA incorrecte, introdueix un dins les opcions (4%, 10%, 21%): "))
    
if iva == 4:
    preuFinal = euros + iva4
    print("Preu sense iva: " + str(euros))
    print("IVA 4%: " + str(iva4))
    print("Preu amb IVA: " + str(preuFinal))
elif iva == 10:
    preuFinal = euros + iva10
    print("Preu sense iva: " + str(euros))
    print("IVA 10%: " + str(iva10))
    print("Preu amb IVA: " + str(preuFinal))
elif iva == 21:
    preuFinal = euros + iva21
    print("Preu sense iva: " + str(euros))
    print("IVA 21%: " + str(iva21))
    print("Preu amb IVA: " + str(preuFinal))
else:
    print("IVA incorrecte")