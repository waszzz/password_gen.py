import random
character = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

tell = int(input("Introduce la longitud de tu contraseña: "))

password = ""

for i in range(tell):
    password += random.choice(character)

print(password)
