print("CADA VEZ MAS GRANDES")
num1 = int(input("Escriba un numero: "))
num2 = int(input(f"Escriba un numero mayor que {num1}: "))

while num1 < num2:
    num1 = num2
    num2 = int(input(f"Escriba un numero mayor que {num1}: "))
print(f"Ha escrito un numero {num2} mayor el {num1}")

#while num1 < num2:
#    print(f"El numero {num1} es menor que numero {num2}, itroduzca uno de nuevo")
#    num3 = int(input(f"Escriba un numero mayor que {num2}"))
#    while num2 < num3:
#        num2 = int(input(f"Escriba un numero mayor que {num1}: "))
#print(f"Ha escrito un numero {num2} mayor el {num1}")