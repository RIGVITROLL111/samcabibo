print("COMPARADOR DE TRES NUMEROS")
num1 = float(input("Escriba el primer numero: "))
num2 = float(input("Escriba el segundo numero: "))
num3 = float(input("Escriba el tercer numero: "))
#if num1 == num2:
#   print(f"el primer numero {num1} y el segundo numero {num2} son iguales")
#elif num1 == num3:
#   print(f"el primer numero {num1} y el tercer numero {num3} son iguales")
#elif num2 == num3:
#   print(f"el segundo numero {num2} y el tercer numero {num3} son iguales")
#elif num1 == num2 == num3:
#   print("los tres numeros son iguales")
if num1 == num2 and num1 == num3 or num2 == num3:
    print("Dos numeros son iguales")
elif num1 == num2 and num2 == num3:
    print("los tres numeros son iguales")
else:
    print("Los tres numeros son diferentes")
