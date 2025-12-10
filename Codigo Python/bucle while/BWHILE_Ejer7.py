print("CONFIRME SU CONTRASEÑA")
contraseña1 = input("Escriba su contraseña: ")
contraseña2 = input("Confirme su contraseña: ")
while contraseña1 != contraseña2:
    print("Las contraseñas no son igules")
    contraseña1 = input("Escriba su contraseña: ")
    contraseña2 = input("Confirme su contraseña: ")
print("Contraseña confirmada, hasta pronto!")