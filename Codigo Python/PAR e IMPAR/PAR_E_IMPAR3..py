print("PAR E IMPAR 3")
par = int(input("Introduzca un numero par: "))
impar = int(input("introduzca un numero impar: "))
error = False
if par % 2 == 1:
    print("El numero introducido no es par")
    error = True
if impar % 2 == 0:
    print("El numero introducido no es impar")
    error = True
if error:
    print("Ejecute de nuevo")
else:
    print("Hasta pronto")