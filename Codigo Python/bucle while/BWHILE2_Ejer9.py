print("DESCOMPOSICION EN NUMEROS PRIMOS")
num = int(input("Escriba un numero mayor que 1: "))
while num <= 1:
    num = int(input(f"{num} no es mayor que 1, introduzca otro numero mayor a 1: "))
copia = num

print("Descomposición en factores primos:", end="")
p = 2
while copia > p:
    while copia % p == 0:
        copia = copia // p
        print(f" {p}",end="")
    p += 1
if copia != 1:
    print(f" {copia}")