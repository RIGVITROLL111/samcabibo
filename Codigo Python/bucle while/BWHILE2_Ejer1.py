print("NUMERO MAYOR")
num1 = int(input("Escriba un número: "))
num2 = int(input(f"Escriba un número mayor que {num1}: "))
while num1 <= num2:
    print(f"El número {num2} no es mayor que {num1}. Por favor, inténtelo de nuevo.")
    num2 = int(input(f"Escriba un número mayor que {num1}: "))
print(f"Ha escrito los numero {num1} y {num2}, Hasta pronto!")