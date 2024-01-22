from random import choice, randint


def create_punctuation():

    punctuation = ""

    setter = input("Simple of complex punctuation?: ")

    if setter == "simple":

        punctuation = "$!#&@?%=_"

        return punctuation

    elif setter == "complex":

        punctuation = "–!”#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

        return punctuation

    else:

        print("Try again.")


def role_playing_game(length):

    password = []

    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    punctuation = str(create_punctuation())

    character_list = uppercase + lowercase + digits + punctuation

    for i in range(length):

        random_character = choice(character_list)
        password.append(random_character)

    print("".join(password))


def role_playing_game_vb():
    """
    For websites where the above function generates a password
    that's considered too complicated.
    """

    password = []

    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"

    character_list = uppercase + lowercase + digits

    for i in range(12):

        random_character = choice(character_list)
        password.append(random_character)

    print("".join(password))


if __name__ == "__main__":
    need = input("Simple or complex?: ")

    if need == "simple":
        role_playing_game_vb()

    elif need == "complex":
        length = int(input("Enter password length: "))
        role_playing_game(length)

    print(randint(1, 25))
