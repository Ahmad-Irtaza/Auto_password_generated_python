import random
import string

def generate_password():
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    password_uppercase = random.sample(uppercase_letters, 2)
    password_lowercase = random.sample(lowercase_letters, 2)
    password_digits = random.sample(digits, 2)
    password_symbols = random.sample(special_symbols, 2)

    password_chars = (
        password_uppercase +
        password_lowercase +
        password_digits +
        password_symbols
    )
    random.shuffle(password_chars)

    generated_password = ''.join(password_chars)

    return generated_password

password = generate_password()
print("Generated Password:", password)

