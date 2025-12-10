print("PAR E IMPAR 4")
par = int(input("Escriba un numero par: "))
error = False
if par % 2 == 1:
    print("El numero introducido no es par")
    error = True
impar = int(input("Escriba un muero impar: "))
if impar % 2 == 0:
    print("El numero introducido no es impar: ")
    error = True
if error:
    print("Ejecuta de nuevo")
else:
    print("Hasta pronto")
