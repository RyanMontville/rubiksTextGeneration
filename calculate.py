"""Things still needed to be added somewhere:
    It will also determine if a word is too long and must be split into multiple lines
    If text includes ' or ? shift row down one more pixel. 6 pixels tall instead of 5
"""


def addWidthOfCharacter(character):
    """Returns the number of pixels wide a character is"""
    # If any other characters are entered other than those with defined functions, replace that character with a space
    pass


def calculateWidthOfWord(word):
    """Returns the number of pixels wide a word is"""
    # Calls addWidthOfCharacter()
    pass


def determineTextBreak(text):
    """Returns boolean determining whether the text can fit on one line or if 
    it needs to be split into multiple lines"""
    pass


def centerText(text):
    """Returns the number of pixels to add before the text to center it on the mosaic"""
    pass


def recommendedDimensions():
    """Will Determine the minimum number of cubes needed and the recommended dimensions of the mosaic"""
    # Might split this into 2 functions
    pass
