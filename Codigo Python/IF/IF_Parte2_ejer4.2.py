print("COMPARADOR DE MULTIPLOS 2")
num1 = int(input("Escriba un numero: "))
num2 = int(input("Escriba otro numero: "))
if num1 == 0 or num2 == 0:
    print("No se admite 0")
elif num1 < 0 or num2 < 0:
    print("No se admiten numeros negativos")
elif num1 >= num2 and num1 % num2 != 0:
    print(f"{num1} no es multiplo de {num2}")
elif num1 >= num2 and num1 % num2 == 0:
    print(f"{num1} es pultiplo de {num2}")
elif num1 < num2 and num1 % num2 != 0:
    print(f"{num2} no es multiplo de {num1}")
else:
    print(f"{num2} es multiplo de {num1}")
    print("Hasta pronto ¡¡¡")