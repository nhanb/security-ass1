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

        if key <= 0:
            return "Invalid input: key must be a positive number."

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
                return column(input_text, key, alphabet, action)
            else:
                return "Invalid action. Must be 'e' or 'd'"

    except IOError:
        return "Error reading " + inputf

    except ValueError:
        return "Please enter a valid integer as the key!"


# Encrypt logic
def encrypt(input_text, key, alphabet):
    size = len(input_text)
    table = []

    maxY = size / key
    maxX = key
    if size % key > 0:
        maxY += 1
    i = 0
    for y in range(maxY):
        table.append([])
        for x in range(maxX):
            if i >= size:
                char = " "
            else:
                char = input_text[i]
            table[y].append(char)
            i += 1

    output = ""
    for x in range(maxX):
        for y in range(maxY):
            output += table[y][x]

    return output


# Decrypt logic
def decrypt(input_text, key, alphabet):
    size = len(input_text)
    table = []

    if size % key != 0:
        return "Invalid input: cipher length must be divisible by key"

    maxY = size / key
    maxX = key

    i = 0
    for x in range(maxX):
        table.append([])
        for y in range(maxY):
            table[x].append(input_text[i])
            i += 1

    output = ""
    for y in range(maxY):
        for x in range(maxX):
            output += table[x][y]

    return output


# Actual columnar cipher logic
def column(input_text, key, alphabet, action):
    if action == "e":
        return encrypt(input_text, key, alphabet)
    else:
        return decrypt(input_text, key, alphabet)


# Run script and print result to standard output
print run(sys.argv)
