print("PAR E IMPAR")
PAR = int(input("escriba un numero par: "))
IMPAR = int(input("escriba un numero impar: "))

if PAR % 2 == 1 or IMPAR % 2 == 0:
    print("los valores introducidos son incorrectos")
    print("ejecute de nuevo e introduzca otro numero")
else:
    print("Hasta pronto")