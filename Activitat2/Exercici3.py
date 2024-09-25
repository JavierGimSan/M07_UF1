valor1 = int(input("Introdueix valor 1: "))
valor2 = int(input("Introdueix valor 2: "))

if valor1 < valor2:
    print(f"El valor 2 és més gran ({valor2})")
elif valor2 < valor1:
    print(f"El valor 1 és més gran ({valor1})")
else:
    print("Els dos valors són iguals")