print("CUENTA PARES 1")
num = int(input("Escriba un numero par: "))
while num % 2 != 0:
    num = int(input(f"{num} no es un numero par, Intentelo de nuevo: "))
cont = 1
seguir = input("Quiere seguir escribiendo pares?: ")
while seguir == "S" or "s":
    num = int(input("Escriba un numero par: "))
    while numero % 2 != 0:
        numero = int(input(f"{numero} no es un número par. Inténtelo de nuevo: "))
    cont += 1
    seguir = input("Quiere seguir escribiendo pares?: ")
if cont == 1:
    print("Ha escrito un numero")
else:
    print(f"Ha escrito {cont} numeros")