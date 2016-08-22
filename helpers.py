def alphabet_position(letter):
    """returns position (0-25) of a letter
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter = letter.lower()
    value = alphabet.index(letter)
    return value

def rotate_character(char, rot):
    """rotates character by given number of spaces
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
#only rotating letters
    if char.isalpha():
#rotating position
        origPos = alphabet_position(char)
        newPos = origPos + rot
        newPos = newPos % 26
#calculating new character and maintaining capitalization
        if char == char.lower():
            newChar = alphabet[newPos]
        elif char == char.upper():
            newChar = alphabet[newPos].upper()
#if not a letter
    else:
        newChar = char
    return newChar
