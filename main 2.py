import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

pass_length = int(input("Introduce la longitud de la contraseña: "))


password = ""
6

for i in range(pass_length):
    password += random.choice(characters)


print("Tu contraseña generada es:", password)