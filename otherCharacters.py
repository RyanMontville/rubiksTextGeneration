def draw1(rows, current_x, current_y, text_color):
    """
    Adds the number 1 to the mosaic matrix array at the current coordinates
    :param rows: The matrix array of mosaic pieces
    :param current_x: The x coordinate where the top left of the letter will be inserted
    :param current_y: The y coordinate where the top left of the letter will be inserted
    :param text_color: The color of the text
    :returns the altered matrix array of pieces
    """
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 1][current_x + 1] = text_color
    rows[current_y + 2][current_x + 1] = text_color
    rows[current_y + 3][current_x + 1] = text_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows


def draw2(rows, current_x, current_y, text_color):
    """ See documentation for draw1() """
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 2][current_x + 1] = text_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows


def draw3(rows, current_x, current_y, text_color):
    """ See documentation for draw1() """
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 2][current_x + 1] = text_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows


def draw4(rows, current_x, current_y, text_color):
    """ See documentation for draw1() """
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    # second column
    rows[current_y + 2][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows


def draw5(rows, current_x, current_y, text_color):
    """ See documentation for draw1() """
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 2][current_x + 1] = text_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows


def draw6(rows, current_x, current_y, text_color):
    """ See documentation for draw1() """
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 2][current_x + 1] = text_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows


def draw7(rows, current_x, current_y, text_color):
    """ See documentation for draw1() """
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows


def draw8(rows, current_x, current_y, text_color):
    """ See documentation for draw1() """
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 2][current_x + 1] = text_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows


def draw9(rows, current_x, current_y, text_color):
    """ See documentation for draw1() """
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 2][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows


def draw0(rows, current_x, current_y, text_color):
    """ See documentation for draw1() """
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows


def drawPound(rows, current_x, current_y, text_color):
    """ See documentation for draw1() """
    altered_rows = rows
    # first column
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 1][current_x + 1] = text_color
    rows[current_y + 2][current_x + 1] = text_color
    rows[current_y + 3][current_x + 1] = text_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = text_color
    # fourth column
    rows[current_y][current_x + 3] = text_color
    rows[current_y + 1][current_x + 3] = text_color
    rows[current_y + 2][current_x + 3] = text_color
    rows[current_y + 3][current_x + 3] = text_color
    rows[current_y + 4][current_x + 3] = text_color
    # fifth column
    rows[current_y + 1][current_x + 4] = text_color
    rows[current_y + 3][current_x + 4] = text_color

    return altered_rows


def drawExclamation(rows, current_x, current_y, text_color):
    """ See documentation for draw1() """
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 4][current_x] = text_color

    return altered_rows


def drawQuestion(rows, current_x, current_y, text_color):
    """ See documentation for draw1() """
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    # second column
    rows[current_y - 1][current_x + 1] = text_color
    rows[current_y + 2][current_x + 1] = text_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = text_color

    return altered_rows


def drawApostrophe(rows, current_x, current_y, text_color):
    """ See documentation for draw1() """
    altered_rows = rows
    rows[current_y - 1][current_x] = text_color
    rows[current_y][current_x] = text_color

    return altered_rows
