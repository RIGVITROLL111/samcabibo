print("Divisor de numeros")
dividendo = int(input("Escriba un dividendo: "))
divisor = int(input("Escribe un divisor: "))
#if dividendo % divisor == 0:
#    print(f"La division es exacta: {dividendo // divisor}")
#else:
#    print(f"La division no es exacta: {dividendo // divisor}")
#    print(f"Resto: {dividendo // divisor}")

### no se puede dividir por cero ###
if divisor == 0:
    print("No se puede dividir por cero")
else:
    if dividendo % divisor == 0:
        print(f"La division es exacta: {dividendo // divisor}")
    else:
        print(f"La division no es exacta: {dividendo // divisor}")
        print(f"Resto: {dividendo // divisor}")