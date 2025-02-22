"""Things still needed to be added somewhere:
    It will also determine if a word is too long and must be split into multiple lines
    If text includes ' or ? shift row down one more pixel. 6 pixels tall instead of 5
"""


def widthOfCharacter(character):
    """Returns the number of pieces needed to draw the character.
    If any other characters are entered other than those with defined functions,
    replace that character with a space.
    :param character: The character to calculate the width of
    :returns the number of pieces needed to draw the character"""
    match character:
        case "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "k" | "l" | "o" | "p" | "r" | "s" | "t" | "u" | \
             "v" | "y" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0" | "?":
            return 3
        case "j" | "n":
            return 4
        case "m" | "w" | "x" | "#":
            return 5
        case "!" | "'":
            return 1
        case _:
            return 2


def calculateWidthOfWord(word):
    """Returns the number of pixels wide a word is
    :param word: The word to calculate the width of
    :returns the number of pieces needed to draw the word"""
    characters = list(word)
    width_of_word = 0
    for character in characters:
        width_of_word += widthOfCharacter(character)
    width_of_word += len(characters) - 1
    return width_of_word


def determineTextBreak(text):
    """Determines whether the text can be drawn on one line or if it
    needs to be split into multiple line
    :returns boolean if text can be drawn on a single line"""
    pass


def centerText(text):
    """Returns the number of pixels to add before the text to center it on the mosaic"""
    pass


def recommendedDimensions():
    """Will Determine the minimum number of cubes needed and the recommended dimensions of the mosaic"""
    # Might split this into 2 functions
    pass
