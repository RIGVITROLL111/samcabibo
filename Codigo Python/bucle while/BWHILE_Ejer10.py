print("CONFIRME SU CONTRASEÑA 2")
contraseña1 = input("Escriba su contraseña: ")
limite = 3
print(f"Tiene {limite} intentos")
contraseña2 = input("Confirme su contraseña: ")
cont = 1

while contraseña1 != contraseña2 and cont < limite:
    print("Las contraseñas no son iguales")
    contraseña2 = input("Confirme su contraseña: ")
    cont += 1

if contraseña1 == contraseña2:
    print("Contraseña confirmada, hasta pronto!")
elif cont == limite: ### pequeña mejora, para que muestre un mensaje al superar el límite de intentos ###
    print("Ha superado el número de intentos")
else:
    print("Contraseña no confimada. Hasta pronto!")