def draw1(current_x, current_y):
    """
    :param current_x: The x coordinate where the top left of the letter will be inserted
    :param current_y: The y coordinate where the top left of the letter will be inserted
    :returns a list of pixel coordinates
    """
    return [(current_x, current_y + 1), (current_x, current_y + 4), (current_x + 1, current_y),
            (current_x + 1, current_y + 1), (current_x + 1, current_y + 2), (current_x + 1, current_y + 3),
            (current_x + 1, current_y + 4), (current_x + 2, current_y + 4)]


def draw2(current_x, current_y):
    """ See documentation for draw1() """
    return [(current_x, current_y), (current_x, current_y + 2), (current_x, current_y + 3),
            (current_x, current_y + 4), (current_x + 1, current_y), (current_x + 1, current_y + 2),
            (current_x + 1, current_y + 4), (current_x + 2, current_y), (current_x + 2, current_y + 1),
            (current_x + 2, current_y + 2), (current_x + 2, current_y + 4)]


def draw3(current_x, current_y):
    """ See documentation for draw1() """
    return [(current_x, current_y), (current_x, current_y + 2), (current_x, current_y + 4),
            (current_x + 1, current_y), (current_x + 1, current_y + 2), (current_x + 1, current_y + 4),
            (current_x + 2, current_y), (current_x + 2, current_y + 1), (current_x + 2, current_y + 2),
            (current_x + 2, current_y + 3), (current_x + 2, current_y + 4)]


def draw4(current_x, current_y):
    """ See documentation for draw1() """
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x + 1, current_y + 2), (current_x + 2, current_y), (current_x + 2, current_y + 1),
            (current_x + 2, current_y + 2), (current_x + 2, current_y + 3), (current_x + 2, current_y + 4)]


def draw5(current_x, current_y):
    """ See documentation for draw1() """
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 4), (current_x + 1, current_y), (current_x + 1, current_y + 2),
            (current_x + 1, current_y + 4), (current_x + 2, current_y), (current_x + 2, current_y + 2),
            (current_x + 2, current_y + 3), (current_x + 2, current_y + 4)]


def draw6(current_x, current_y):
    """ See documentation for draw1() """
    return [(current_x, current_y), (current_x, current_y + 1),
            (current_x, current_y + 2), (current_x, current_y + 3), (current_x, current_y + 4),
            (current_x + 1, current_y), (current_x + 1, current_y + 2), (current_x + 1, current_y + 4),
            (current_x + 2, current_y), (current_x + 2, current_y + 2), (current_x + 2, current_y + 3),
            (current_x + 2, current_y + 4)]


def draw7(current_x, current_y):
    """ See documentation for draw1() """
    return [(current_x, current_y), (current_x + 1, current_y),(current_x + 2, current_y),
            (current_x + 2, current_y + 1), (current_x + 2, current_y + 2), (current_x + 2, current_y + 3),
            (current_x + 2, current_y + 4)]


def draw8(current_x, current_y):
    """ See documentation for draw1() """
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 3), (current_x, current_y + 4), (current_x + 1, current_y),
            (current_x + 1, current_y + 2), (current_x + 1, current_y + 4), (current_x + 2, current_y),
            (current_x + 2, current_y + 1), (current_x + 2, current_y + 2), (current_x + 2, current_y + 3),
            (current_x + 2, current_y + 4)]


def draw9(current_x, current_y):
    """ See documentation for draw1() """
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x + 1, current_y), (current_x + 1, current_y + 2), (current_x + 2, current_y),
            (current_x + 2, current_y + 1), (current_x + 2, current_y + 2), (current_x + 2, current_y + 3),
            (current_x + 2, current_y + 4)]


def draw0(current_x, current_y):
    """ See documentation for draw1() """
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 3), (current_x, current_y + 4), (current_x + 1, current_y),
            (current_x + 1, current_y + 4), (current_x + 2, current_y), (current_x + 2, current_y + 1),
            (current_x + 2, current_y + 2), (current_x + 2, current_y + 3), (current_x + 2, current_y + 4)]


def drawPound(current_x, current_y):
    """ See documentation for draw1() """
    return [(current_x, current_y + 1), (current_x, current_y + 3), (current_x + 1, current_y),
            (current_x + 1, current_y + 1), (current_x + 1, current_y + 2), (current_x + 1, current_y + 3),
            (current_x + 1, current_y + 4), (current_x + 2, current_y + 1), (current_x + 2, current_y + 3),
            (current_x + 3, current_y), (current_x + 3, current_y + 1), (current_x + 3, current_y + 2),
            (current_x + 3, current_y + 3), (current_x + 3, current_y + 4), (current_x + 4, current_y + 1),
            (current_x + 4, current_y + 3)]


def drawExclamation(current_x, current_y):
    """ See documentation for draw1() """
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 4)]


def drawQuestion(current_x, current_y):
    """ See documentation for draw1() """
    return [(current_x, current_y), (current_x + 1, current_y - 1),
            (current_x + 1, current_y + 2), (current_x + 1, current_y + 4),
            (current_x + 2, current_y), (current_x + 2, current_y + 1)]


def drawApostrophe(current_x, current_y):
    """ See documentation for draw1() """
    return [(current_x, current_y - 1), (current_x, current_y)]
