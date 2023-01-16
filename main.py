from random import randint as role1
from random import sample as role2
import string


def random_password():
    """
    Original version of the random password generator. Note how does not make
    use of the string package.
    """

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "123456789"
    symbols = "[]{}()*;/,._-"
    characters = lower + upper + numbers + symbols
    password_length = 24
    # random.sample was changed to role2 after update
    password = "".join(role2(characters, password_length))
    return password


def game():
    """
    New version of the random password generator. Makes use of the string
    package, and obfuscation.
    """

    characters = string.ascii_lowercase + string.ascii_uppercase \
        + string.digits + string.punctuation
    length = role1(16, 32)
    playing = role2(characters, length)
    playing = "".join(playing)
    return playing


def blind():
    """
    Uses the returned values from the previous functions to generate a new
    value.
    """

    layer1 = random_password()
    layer2 = game()
    layer3 = layer1 + layer2
    layer4 = (len(layer1) + len(layer2)) // 2
    layer5 = role2(layer3, layer4)
    layer6 = "".join(layer5)
    print(layer6)


if __name__ == "__main__":
    blind()
