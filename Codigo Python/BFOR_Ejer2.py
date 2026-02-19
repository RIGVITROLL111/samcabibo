print("DIVISORES")
num = int(input("Escriba un numero mayor que cero: "))
while num <= 0:
    print(f"El numero {num} tiene que ser mayor a 0")
    num = int(input("Escriba un numero mayor que cero: "))
else:
    print(f"Los divisores de {num} son: ", end="")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i," ", end="")