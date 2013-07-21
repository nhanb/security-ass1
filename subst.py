import random
import sys

# Define the alphabet used in this Ceasar cipher implementation
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .,()-!?\n0123456789'


# "Portal" to the program flow. Handle some validations before calling handle
# functions, which in turn call pure logic functions.
def run(args):

    if len(args) != 4:
        return "Invalid number of arguments."

    action = args[1]
    inputf = args[2]
    keyf = args[3]

    # Key generation mode
    if action == "g":
        try:
            with open(inputf, "w") as key_file:
                key_file.write(generate_key(alphabet))
                return "Key written to " + inputf
        except IOError:
            return "Could not write to " + inputf

    # Encrypt / Decrypt mode
    elif action in ["e", "d"]:
        try:
            with open(inputf, 'r') as input_file, open(keyf, 'r') as key_file:
                input_text = input_file.read().upper()
                input_text = input_text[:-1]  # Remove trailing \n
                key_text = key_file.read()[:-1]

                # Check that input text doesn't contain any illegal char
                if not (is_within_alphabet(input_text)
                        and is_within_alphabet(key_text)):
                    return "Input contains illegal character."
                else:
                    if action == "e":
                        enc = True
                    else:
                        enc = False
                    return substitute(input_text, key_text, enc)

        except IOError:
            return "Could not read from %s and %s" % (inputf, keyf)

    # Invalid action
    else:
        return "Unrecognized argument: " + action


def is_within_alphabet(text):
    for char in text:
        if alphabet.find(char) == -1:
            return False, char
    return True


def substitute(in_text, key, encrypt):
    result = ""
    if encrypt:
        for char in in_text:
            result += key[alphabet.find(char)]
    else:
        for char in in_text:
            result += alphabet[key.find(char)]
    return result


def generate_key(alphabet):

    # For each character in the given alphabet, assign a random
    # character as its correspond value (val)
    vals = alphabet
    result = ""
    for char in alphabet:
        val = random.choice(vals)

        # Remove chosen char from list of possible values
        index = vals.find(val)
        vals = vals[:index] + vals[index + 1:]

        result += val


print run(sys.argv)
