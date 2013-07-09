import random
import sys

key_file = "subst.key"
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .,()-!?\n0123456789'


# "Portal" to the program flow. Handle some validations before calling handle
# functions, which in turn call pure logic functions.
def run(args):

    if len(args) != 4:
        return "Invalid number of arguments."

    try:
        action = args[1]
        inputf = args[2]
        keyf = args[3]

        # Define the alphabet used in this Ceasar cipher implementation
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .,()-!?\n0123456789'

        if action == "g":
            handle_generate(inputf, alphabet)
        elif action in ["e", "d"]:
            substitute(inputf, keyf, alphabet)

        with open(inputf, 'r'), open(keyf, 'r') as input_file, key_file:

            input_text = input_file.read().upper()
            input_text = input_text[:-1]  # Remove trailing \n

            # Check that input text doesn't contain any illegal char
            if not is_within_alphabet(input_text):
                return "Input contains illegal character."


            # Call appropriate function according to action
            #if action in ["e", "d"]:
                #return ceasar(input_text, key, alphabet, action)
            #else:
                #return "Invalid action. Must be 'e' or 'd'"

    except IOError:
        return "Error reading %s & %s" % inputf, keyf


def is_within_alphabet(text):
    for char in text:
        if alphabet.find(char) == -1:
            return False, char
    return True


def handle_generate(key_file, alphabet):
    try:
        with open(key_file, "w") as keyf:
            keyf.write(generate(alphabet))

    except IOError as err:
        print err


def generate(alphabet):

    # For each character in the given alphabet, assign a random
    # character as is correspond value (val)
    vals = alphabet
    result = ""
    for char in alphabet:
        val = random.choice(vals)

        # Remove chosen char from list of possible values
        index = vals.find(val)
        vals = vals[:index] + vals[index + 1:]

        result += val
        #if char == "\n":
            #char = "\\n"
        #if val == "\n":
            #val = "\\n"
        #keyf.write(char + "->" + val + "\n")


run(sys.argv)
