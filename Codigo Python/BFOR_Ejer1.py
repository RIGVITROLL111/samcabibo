print("PARES E IMPARES")
num1 = int(input("Escriba un numero entero: "))
num2 = int(input(f"Escriba un numero mayor o igual que {num1}: "))
if num2 < num1:
    print(f"El numero {num2} es menor que {num1}")
else:
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            print(f"El numero {i} es par")
        else:
            print(f"El numero {i} es impar")