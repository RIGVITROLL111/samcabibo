print("CALCULO DE AREAS")
print("Elija una figura geometrica:")
print("a) Triangulo")
print("b) Cuadrado")
figura = input("Escriba C para Cuadrado y escriba T para Triangulo: ")
if figura == "C" or figura == "c":
    base = float(input("Escriba la base del cuadrado: "))
    altura = float(input("Escriba la altura del cuadrado: "))
    print(f"El area del cuadrado es: {base * altura}")
elif figura == "T" or figura == "t":
    base = float(input("Escriba la base del triangulo: "))
    altura = float(input("Escriba la altura del triangulo: "))
    print(f"El area del triangulo es: {(base * altura) / 2}")