print("PAR E IMPAR con elif")
PAR = int(input("introduzca un numero par: "))
IMPAR = int(input("introduzca un numero impar: "))

if PAR % 2 == 1:
    print("uno o mas numero son incorrectos")
    print("ejecute de nuevo e introduzca otro numero")
elif IMPAR % 2 == 0:
    print("uno o mas numero son incorrectos")
    print("ejecute de nuevo e introduzca otro numero")
else:
    print("Hasta pronto")