print("CONVERTIDOR DE CENTIMETROS A METROS Y KILOMETROS")
cm = int(input("Escriba una distancia en centimetros: "))
if cm <= 0:
    print("Error: La distancia no puede ser negativa")
else:
    kilometros = cm / 100000
    metros = cm / 100
    resto = cm % 100
    print(f"{cm} centimetros son {kilometros} kilometros, y {cm} centimetros son {metros} metros con {resto} centimetros restantes")