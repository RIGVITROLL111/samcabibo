print("HUCHA")
ahorro = float(input("¿Cuántos euros quiere ahorrar?: "))
meter_dinero = 0
while ahorro > meter_dinero:
    meter_dinero += float(input("¿Cuántos euros quiere meter en la hucha?: "))
print(f"A ahorrado {meter_dinero} euros")