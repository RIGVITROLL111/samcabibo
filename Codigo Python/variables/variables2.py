print("CALCULO DE IMC")
PESO = float(input("Cuanto pesa(en Kg)?: "))
ALTURA = float(input("Cuanto mide(en metros ejemplo 190cm = 1.9)?: "))
IMC = PESO / ALTURA ** 2
print(f"Su IMC es {round(IMC, 1)}")    
