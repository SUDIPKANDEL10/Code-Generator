## create a code generator 

import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = int(input("enter the length of the password: "))
generate_password = generate_password(password_length)
print("Generated password : ", generate_password)

    