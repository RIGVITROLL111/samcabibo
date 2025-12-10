print("PAR E IMPAR 2")
par = int(input("Introduzca un numero par: "))
if par % 2 == 1:
    print("El numero introduciod no es par")
    print("Ejecute de nuevo")
else:
    impar = int(input("introduzca un numero impar: "))
    if impar % 2 == 0:
        print("El numero introducido no es impar: ")
        print("Ejecute de nuevo")
    else:
        print("Hasta pronto")