print("MAYORES QUE EL PRIMERO")
valor = int(input("Escriba un valor mayor a 0: "))
while valor <= 0:
    print("No se puede introducir un valor menor a 0")
    valor = int(input("Escriba un valor mayor a 0: "))
else:
    num1 = int(input("Escriba un mumero: "))
    for i in range(valor - 1):
        num2 = int(input(f"escriba un numero mas grande {num1}"))
        if num2 <= num1:
            print(f"{num2} no es mayor que {num1}")
        else:
            print("Hasta pronto!!!")