def draw1(rows, current_x, current_y, text_color, background_color):
    """
    Adds the number 1 to the mosaic matrix array at the current coordinates
    Args:
        rows: The matrix array of mosaic pieces
        current_x: The x coordinate where the top left of the letter will be inserted
        current_y: The y coordinate where the top left of the letter will be inserted
        text_color: The color of the text
        background_color: The color of the background of the mosaic
    """
    altered_rows = rows

    return altered_rows


def draw2(rows, current_x, current_y, text_color, background_color):
    """ See documentation for draw1() """
    altered_rows = rows

    return altered_rows


def draw3(rows, current_x, current_y, text_color, background_color):
    """ See documentation for draw1() """
    altered_rows = rows

    return altered_rows


def draw4(rows, current_x, current_y, text_color, background_color):
    """ See documentation for draw1() """
    altered_rows = rows

    return altered_rows


def draw5(rows, current_x, current_y, text_color, background_color):
    """ See documentation for draw1() """
    altered_rows = rows

    return altered_rows


def draw6(rows, current_x, current_y, text_color, background_color):
    """ See documentation for draw1() """
    altered_rows = rows

    return altered_rows


def draw7(rows, current_x, current_y, text_color, background_color):
    """ See documentation for draw1() """
    altered_rows = rows

    return altered_rows


def draw8(rows, current_x, current_y, text_color, background_color):
    """ See documentation for draw1() """
    altered_rows = rows

    return altered_rows


def draw9(rows, current_x, current_y, text_color, background_color):
    """ See documentation for draw1() """
    altered_rows = rows

    return altered_rows


def draw0(rows, current_x, current_y, text_color, background_color):
    """ See documentation for draw1() """
    altered_rows = rows

    return altered_rows


def drawPound(rows, current_x, current_y, text_color, background_color):
    """ See documentation for draw1() """
    altered_rows = rows

    return altered_rows


def drawExclamation(rows, current_x, current_y, text_color, background_color):
    """ See documentation for draw1() """
    altered_rows = rows

    return altered_rows


def drawQuestion(rows, current_x, current_y, text_color, background_color):
    """ See documentation for draw1() """
    altered_rows = rows

    return altered_rows


def drawApostrophe(rows, current_x, current_y, text_color, background_color):
    """ See documentation for draw1() """
    altered_rows = rows

    return altered_rows


def drawSpace(rows, current_x, current_y, text_color, background_color):
    """ See documentation for draw1() """
    altered_rows = rows
    # first column
    rows[current_y][current_x] = background_color
    rows[current_y + 1][current_x] = background_color
    rows[current_y + 2][current_x] = background_color
    rows[current_y + 3][current_x] = background_color
    rows[current_y + 4][current_x] = background_color
    # second column
    rows[current_y][current_x + 1] = background_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = background_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = background_color

    return altered_rows


def drawBetweenLetters(rows, current_x, current_y, text_color, background_color):
    """ See documentation for draw1() """
    altered_rows = rows
    # first column
    rows[current_y][current_x] = background_color
    rows[current_y + 1][current_x] = background_color
    rows[current_y + 2][current_x] = background_color
    rows[current_y + 3][current_x] = background_color
    rows[current_y + 4][current_x] = background_color

    return altered_rows
