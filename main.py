from random import choice, randint

def role_playing_game(length):

    password = []

    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    punctuation = "–!”#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    character_list = uppercase + lowercase + digits + punctuation

    for i in range(length):

        random_character = choice(character_list)
        password.append(random_character)

    print("".join(password))

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    role_playing_game(length)
    print(randint(1, 25))
