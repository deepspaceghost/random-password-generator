def random_password():

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "123456789"
    symbols = "[]{}()*;/,._-"
    characters = lower + upper + numbers + symbols
    password_length = 24
    password = "".join(random.sample(characters, password_length))
    print(password)

random_password()
