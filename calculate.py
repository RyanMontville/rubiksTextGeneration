"""Things still needed to be added somewhere:
    It will also determine if a word is too long and must be split into multiple lines
    If text includes ' or ? shift row down one more pixel. 6 pixels tall instead of 5
"""
import math


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


def calculateSizeOfWord(word):
    """Returns the number of pixels wide a word is
    :param word: The word to calculate the width of
    :returns the number of pieces needed to draw the word in both width and height"""
    characters = list(word)
    width_of_word = 0
    for character in characters:
        width_of_word += widthOfCharacter(character)
    width_of_word += len(characters) - 1
    if "?" in word or "'" in word:
        return width_of_word, 6
    else:
        return width_of_word, 5


def calculateMinimumSize(text):
    """Calculates the minimum dimensions of the mosaic
    :param text: The text to be drawn in the mosaic
    :returns the minimum number of cube needed to draw the text"""
    min_width = 0
    min_height = 0
    min_cubes_tall = 0
    min_cubes_wide = 0
    words = text.split()
    for word in words:
        size = calculateSizeOfWord(word)
        if size[0] > min_width:
            min_width = size[0]
        min_height += size[1]
    min_height += len(words) + 1
    min_width += 2
    min_cubes_tall = math.ceil(min_height / 3)
    min_cubes_wide = math.ceil(min_width / 3)

    return min_cubes_wide, min_cubes_tall


def makeLine(text, width):
    """Given the width of the mosaic, fit as many words on a line. Will return the line as a string and the rest of
    the text as a second string."""
    single_line = []
    pieces_left_in_line = width
    words = text.split()
    while pieces_left_in_line > 0:
        current_word = calculateSizeOfWord(words[0])
        if current_word <= width:
            single_line.append(words[0])
            words.remove(words[0])
        else:
            line_final = ' '.join(single_line)
            remaining_text = ' '.join(words)
            return line_final, remaining_text


def centerText(text):
    """Returns the number of pixels to add (if any) before the text to center it on the mosaic."""
    pass


def recommendedDimensions():
    """Will Determine the recommended dimensions of the mosaic"""
    # Might remove this since calculateMinimumSize() exists, but this function might be used to optimize the best
    # layout. Or that could also be added to calculateMinimumSize().
    # This could also be completed using determineTextBreak()
    pass
