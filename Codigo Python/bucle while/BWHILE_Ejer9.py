print("HUCHA MEJORADA")
objetivo_ahorro = float(input("¿Cuántos euros quiere ahorrar?: "))
while objetivo_ahorro < 0:
    print("Por favor, escriba una cantidad positiva.")
    objetivo_ahorro += float(input("¿Cuántos euros quiere meter en la hucha?: "))
hucha_ahorro = 0

while objetivo_ahorro > hucha_ahorro:
    ahorro += float(input("¿Cuántos euros quiere meter en la hucha?: "))
    while ahorro < 0:
        print("Por favor, escriba una cantidad positiva.")
        ahorro += float(input("¿Cuántos euros quiere meter en la hucha?: "))
    ahorro += hucha_ahorro
print(f"A ahorrado {hucha_ahorro} euros")