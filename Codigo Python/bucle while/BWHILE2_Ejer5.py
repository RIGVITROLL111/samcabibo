print("SUMA DE NUMEROS")
num1 = int(input("Escriba un numero: "))
suma = 0
while num1 >= 0:
    suma += num1
    num1 = int(input("Escriba otro numero: "))
print(f"la suma de los numeros es {suma}")