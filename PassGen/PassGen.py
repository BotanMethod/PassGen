
import string
import random
import art
import os

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = int(input("Enter password length... "))
generated_password = generate_password(password_length)
print("Your generated password: ", generated_password)

art.tprint("PassGen")


    