import random
longitud_contra = int(input("introduce la longitud de la contraseña =>"))

contraseña = ""
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

for _ in range(longitud_contra):
    caracter_aleatorio = random.choice(caracteres)
    contraseña += caracter_aleatorio

print("Contraseña generada:", contraseña)