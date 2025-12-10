print("NUMEROS MAYORES")
num1 = float(input("Escriba un número: "))
num2 = float(input(f"Escriba un número mayor que {num1}: "))
while num2 > num1:
    num2 = float(input(f"Escriba un número mayor que {num1}: "))
print(f"Gracias! El número {num2} NO es mayor que {num2}.")