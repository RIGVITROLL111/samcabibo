print("Nueros positivos")
objetivo = int(input("Escriba la cantidad de numeros positivos a escribir"))
while objetivo <= 0:
    objetivo = int(input("La cantidad debe ser mayor que 0. Inténtelo de nuevo: "))

num1 = int(input("Esciba un numero: "))
total = 1

if num1 > 0:
    cantidad = 1
else:
    cantidad = 0

while cantidad < objetivo:
    numero = int(input("Escriba otro número: "))
    if numero > 0:
        cantidad += 1
    total += 1

if total == 1:
    print("Ha escrito 1 número positivo.")
elif objetivo == 1:
    print(f"Ha escrito {total} números, {objetivo} de ellos positivo.")
else:
    print(f"Ha escrito {total} números, {objetivo} de ellos positivos.")