print("Entre valores")
min = int(input("Escriba un numero para el minimo: "))
max = int(input(f"Escriba otro numero mayor a {min} para el maximo: "))
while min >= max:
    print(f"{min} es mayor que {max}")
    min = int(input(f"Escriba otro numero mayor a {max}: "))
num = int(input(f"Escriba un numero en el rango de, maximo {max} y minimo {min}: "))
cont = 0
print()
while num >= min and num <= max:
    cont += 1
    num = int(input(f"Escriba otro numero en el rango de, maximo {max} y minimo {min}: "))
print()
if cont == 0:
    print(f"No ha escrito ningun numero en el rengo de {max} y {min}")
elif cont == 1:
    print(f"Ha escrito un numero en el rango de {max} y {min}")
else:
    print(f"Ha escrito {cont} numeros en el rango de {max} y {min}")