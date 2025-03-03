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
        case "m" | "w" | "x" | "#" | "q":
            return 5
        case "!" | "'":
            return 1
        case _:
            return 0


def calculateWidthOfWord(word):
    """Returns the number of pixels wide a word is
    :param word: The word to calculate the width of
    :returns the width of the word in pieces"""
    characters = list(word)
    width_of_word = 0
    for character in characters:
        width_of_word += widthOfCharacter(character)
    width_of_word += len(characters) - 1
    return width_of_word


def makeLine(text, width):
    """Given the width of the mosaic, fit as many words on a line. Will return the line as a string, the height of
    the line, and the rest of the text as a second string.
    :param text: the text for the mosaic
    :param width: the width of the mosaic
    :returns (the text for the line, the height of the line, the rest of the text that doesn't fit on the line)"""
    single_line = []
    pieces_left_in_line = width
    words = text.split()
    while pieces_left_in_line > 0 and len(words) > 0:
        current_word_length = calculateWidthOfWord(words[0])
        if current_word_length <= pieces_left_in_line:
            single_line.append(words[0])
            words.remove(words[0])
            pieces_left_in_line -= current_word_length
            if len(single_line) > 1:
                pieces_left_in_line -= 2
                if pieces_left_in_line < 0:
                    word_to_move = single_line[-1]
                    single_line.remove(word_to_move)
                    temp = [word_to_move]
                    temp.extend(words)
                    words = temp
                    words.append(word_to_move)
                    break
        else:
            break

    line_final = ' '.join(single_line)
    remaining_text = ' '.join(words)
    # Find height of line. If line contains ' or ? the height is 6 instead of 5
    if "?" in line_final:
        return line_final, 6, remaining_text
    elif "'" in line_final:
        return line_final, 6, remaining_text
    else:
        return line_final, 5, remaining_text


def make_lines_list(text, width):
    """Takes the text and splits the words into lines within the width provided.
    :param text: the text for the mosaic
    :param width: width of the mosaic
    :returns the list of lines. Each line is a tuple of (text, the height of the line)"""
    lines = []
    rest_of_text = text
    while len(rest_of_text) > 0:
        result = makeLine(rest_of_text, width)
        line_tuple = (result[0], result[1])
        lines.append(line_tuple)
        rest_of_text = result[2]
    return lines


def calculateMinimumSize(text):
    """Calculates the minimum dimensions of the mosaic
    :param text: The text to be drawn in the mosaic
    :returns min cubes wide, min cubes tall, lines"""
    min_width = 0
    words = text.split()
    # Find the longest word. This will be the minimum width of the mosaic in pieces
    for word in words:
        word_width = calculateWidthOfWord(word)
        if word_width > min_width:
            min_width = word_width
    # Fit as much text on each line, determine how many lines will be needed
    min_height = 0
    lines = make_lines_list(text, min_width)
    for line in lines:
        min_height += line[1]
    min_height += len(lines)

    min_cubes_tall = math.ceil(min_height / 3)
    min_cubes_wide = math.ceil(min_width / 3)

    return min_cubes_wide, min_cubes_tall, lines


def centerText(text, width):
    """Returns the number of pixels to add (if any) before the text to center it on the mosaic."""
    width_of_text = 0
    words = text.split()
    number_of_spaces = len(words) - 1
    for word in words:
        for letter in word:
            width_of_text += widthOfCharacter(letter) + 1
        width_of_text -= 1
    width_of_text += number_of_spaces
    pieces_before = math.floor((width - width_of_text) / 2)
    if pieces_before < 0:
        pieces_before = 0
    print("centerText function says:")
    print(f"{pieces_before} | {text} = {width_of_text} | {pieces_before} = {width}")
    return pieces_before
