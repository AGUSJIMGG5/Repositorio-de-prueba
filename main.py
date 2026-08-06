import random

# Variable con todos los caracteres posibles
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# Pedir al usuario la longitud de la contraseña
pass_length = int(input("Introduce la longitud de la contraseña: "))

# Variable donde se guardará la contraseña generada
password = ""

# Bucle para generar la contraseña
for i in range(pass_length):
    password += random.choice(characters)

# Mostrar la contraseña generada
print("Tu contraseña generada es:", password)