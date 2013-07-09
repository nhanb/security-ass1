import sys


# "Portal" to the program flow. Handle some validations before calling pure
# logic function.
def run(args):

    if len(args) != 4:
        return "Invalid number of arguments."

    try:
        action = args[1]
        inputf = args[2]
        key = int(args[3])

        with open(inputf, 'r') as input_file:

            input_text = input_file.read().upper()
            input_text = input_text[:-1]  # Remove trailing \n

            # Define the alphabet used in this Ceasar cipher implementation
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .,()-!?\n0123456789'

            # Check that input text doesn't contain any illegal char
            for char in input_text:
                if alphabet.find(char) == -1:
                    return "Input can't contain character '" + char + "'."

            # Call appropriate function according to action
            if action in ["e", "d"]:
                return ceasar(input_text, key, alphabet, action)
            else:
                return "Invalid action. Must be 'e' or 'd'"

    except IOError:
        return "Error reading " + inputf

    except ValueError:
        return "Please enter a valid integer as the key!"


# Actual Ceasar cipher logic
def ceasar(plaintext, key, alphabet, action):
        size = len(alphabet)
        cipher = ""

        if action == "d":
            key = -key

        # For each character, find its place in the alphabet then shift the
        # index according to the key. Use modulo to wrap around boundaries.
        for char in plaintext:
            origin_char_index = alphabet.find(char)
            result_char_index = (origin_char_index + key) % size
            cipher += alphabet[result_char_index]

        return cipher


# Run script and print result to standard output
print run(sys.argv)
