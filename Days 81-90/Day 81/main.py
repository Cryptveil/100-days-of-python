from data import encode_table


def to_morse_code(string):
    encode = " ".join(encode_table[letter] for letter in string)
    return encode.replace("SPACE", "/")


string = input("Type something to be converted to morse code:\n").upper()

print(to_morse_code(string))
