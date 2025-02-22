def drawA(rows, current_x, current_y, text_color, background_color):
    """
    Adds the letter A to the mosaic matrix array at the current coordinates
    :param rows: The matrix array of mosaic pieces
    :param current_x: The x coordinate where the top left of the letter will be inserted
    :param current_y: The y coordinate where the top left of the letter will be inserted
    :param text_color: The color of the text
    :param background_color: The color of the background of the mosaic
    :returns the altered matrix array of pieces
    """
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = text_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = background_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows


def drawB(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = text_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = background_color
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = background_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = background_color

    return altered_rows


def drawC(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = background_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = background_color
    rows[current_y + 2][current_x + 2] = background_color
    rows[current_y + 3][current_x + 2] = background_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows


def drawD(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = background_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = background_color
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = background_color

    return altered_rows


def drawE(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = text_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = background_color
    rows[current_y + 2][current_x + 2] = background_color
    rows[current_y + 3][current_x + 2] = background_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows


def drawF(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = text_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = background_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = background_color
    rows[current_y + 2][current_x + 2] = background_color
    rows[current_y + 3][current_x + 2] = background_color
    rows[current_y + 4][current_x + 2] = background_color

    return altered_rows


def drawG(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = background_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = background_color
    rows[current_y + 2][current_x + 2] = background_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows


def drawH(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = background_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = text_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = background_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows


def drawI(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = background_color
    rows[current_y + 2][current_x] = background_color
    rows[current_y + 3][current_x] = background_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 1][current_x + 1] = text_color
    rows[current_y + 2][current_x + 1] = text_color
    rows[current_y + 3][current_x + 1] = text_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = background_color
    rows[current_y + 2][current_x + 2] = background_color
    rows[current_y + 3][current_x + 2] = background_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows


def drawJ(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = background_color
    rows[current_y + 2][current_x] = background_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = background_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = text_color
    # fourth column
    rows[current_y][current_x + 3] = text_color
    rows[current_y + 1][current_x + 3] = background_color
    rows[current_y + 2][current_x + 3] = background_color
    rows[current_y + 3][current_x + 3] = background_color
    rows[current_y + 4][current_x + 3] = background_color

    return altered_rows


def drawK(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = background_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = text_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = background_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = background_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows


def drawL(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = background_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = background_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = background_color
    rows[current_y + 1][current_x + 2] = background_color
    rows[current_y + 2][current_x + 2] = background_color
    rows[current_y + 3][current_x + 2] = background_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows


def drawM(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = background_color
    rows[current_y + 1][current_x + 1] = text_color
    rows[current_y + 2][current_x + 1] = background_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = background_color
    # third column
    rows[current_y][current_x + 2] = background_color
    rows[current_y + 1][current_x + 2] = background_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = background_color
    rows[current_y + 4][current_x + 2] = background_color
    # fourth column
    rows[current_y][current_x + 3] = background_color
    rows[current_y + 1][current_x + 3] = text_color
    rows[current_y + 2][current_x + 3] = background_color
    rows[current_y + 3][current_x + 3] = background_color
    rows[current_y + 4][current_x + 3] = background_color
    # fifth column
    rows[current_y][current_x + 4] = text_color
    rows[current_y + 1][current_x + 4] = text_color
    rows[current_y + 2][current_x + 4] = text_color
    rows[current_y + 3][current_x + 4] = text_color
    rows[current_y + 4][current_x + 4] = text_color

    return altered_rows


def drawN(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = background_color
    rows[current_y + 1][current_x + 1] = text_color
    rows[current_y + 2][current_x + 1] = background_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = background_color
    # third column
    rows[current_y][current_x + 2] = background_color
    rows[current_y + 1][current_x + 2] = background_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = background_color
    rows[current_y + 4][current_x + 2] = background_color
    # fourth column
    rows[current_y][current_x + 3] = text_color
    rows[current_y + 1][current_x + 3] = text_color
    rows[current_y + 2][current_x + 3] = text_color
    rows[current_y + 3][current_x + 3] = text_color
    rows[current_y + 4][current_x + 3] = text_color

    return altered_rows


def drawO(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = background_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows


def drawP(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = text_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = background_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = background_color
    rows[current_y + 4][current_x + 2] = background_color

    return altered_rows


def drawQ(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = background_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = text_color
    # fourth column
    rows[current_y][current_x + 3] = background_color
    rows[current_y + 1][current_x + 3] = background_color
    rows[current_y + 2][current_x + 3] = background_color
    rows[current_y + 3][current_x + 3] = background_color
    rows[current_y + 4][current_x + 3] = text_color

    return altered_rows


def drawR(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = text_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = background_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = background_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows


def drawS(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = background_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = text_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = background_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows


def drawT(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = background_color
    rows[current_y + 2][current_x] = background_color
    rows[current_y + 3][current_x] = background_color
    rows[current_y + 4][current_x] = background_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 1][current_x + 1] = text_color
    rows[current_y + 2][current_x + 1] = text_color
    rows[current_y + 3][current_x + 1] = text_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = background_color
    rows[current_y + 2][current_x + 2] = background_color
    rows[current_y + 3][current_x + 2] = background_color
    rows[current_y + 4][current_x + 2] = background_color

    return altered_rows


def drawU(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = background_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = background_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows


def drawV(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = background_color
    # second column
    rows[current_y][current_x + 1] = background_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = background_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = background_color

    return altered_rows


def drawW(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = background_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = background_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = background_color
    rows[current_y + 1][current_x + 2] = background_color
    rows[current_y + 2][current_x + 2] = background_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = background_color
    # fourth column
    rows[current_y][current_x + 3] = background_color
    rows[current_y + 1][current_x + 3] = background_color
    rows[current_y + 2][current_x + 3] = background_color
    rows[current_y + 3][current_x + 3] = background_color
    rows[current_y + 4][current_x + 3] = text_color
    # fifth column
    rows[current_y][current_x + 4] = text_color
    rows[current_y + 1][current_x + 4] = text_color
    rows[current_y + 2][current_x + 4] = text_color
    rows[current_y + 3][current_x + 4] = text_color
    rows[current_y + 4][current_x + 4] = text_color

    return altered_rows


def drawX(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = background_color
    rows[current_y + 2][current_x] = background_color
    rows[current_y + 3][current_x] = background_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = background_color
    rows[current_y + 1][current_x + 1] = text_color
    rows[current_y + 2][current_x + 1] = background_color
    rows[current_y + 3][current_x + 1] = text_color
    rows[current_y + 4][current_x + 1] = background_color
    # third column
    rows[current_y][current_x + 2] = background_color
    rows[current_y + 1][current_x + 2] = background_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = background_color
    rows[current_y + 4][current_x + 2] = background_color
    # fourth column
    rows[current_y][current_x + 3] = background_color
    rows[current_y + 1][current_x + 3] = text_color
    rows[current_y + 2][current_x + 3] = background_color
    rows[current_y + 3][current_x + 3] = text_color
    rows[current_y + 4][current_x + 3] = background_color
    # fifth column
    rows[current_y][current_x + 4] = text_color
    rows[current_y + 1][current_x + 4] = background_color
    rows[current_y + 2][current_x + 4] = background_color
    rows[current_y + 3][current_x + 4] = background_color
    rows[current_y + 4][current_x + 4] = text_color

    return altered_rows


def drawY(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = background_color
    rows[current_y + 4][current_x] = background_color
    # second column
    rows[current_y][current_x + 1] = background_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = text_color
    rows[current_y + 3][current_x + 1] = text_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = background_color
    rows[current_y + 4][current_x + 2] = background_color

    return altered_rows


def drawZ(rows, current_x, current_y, text_color, background_color):
    """See documentation for drawA()"""
    altered_rows = rows
    # first column
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = background_color
    rows[current_y + 3][current_x] = background_color
    rows[current_y + 4][current_x] = text_color
    # second column
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = text_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = text_color
    # third column
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = background_color
    rows[current_y + 2][current_x + 2] = background_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows
