def drawA(current_x, current_y):
    """
    Adds the letter A to the mosaic matrix array at the current coordinates
    :param current_x: The x coordinate where the top left of the letter will be inserted
    :param current_y: The y coordinate where the top left of the letter will be inserted
    :returns a list of pixel coordinates
    """
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 3), (current_x, current_y + 4), (current_x + 1, current_y),
            (current_x + 1, current_y + 2), (current_x + 2, current_y), (current_x + 2, current_y + 1),
            (current_x + 2, current_y + 2), (current_x + 2, current_y + 3), (current_x + 2, current_y + 4)]


def drawB(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 3), (current_x, current_y + 4), (current_x + 1, current_y),
            (current_x + 1, current_y + 2), (current_x + 1, current_y + 4), (current_x + 2, current_y + 1),
            (current_x + 2, current_y + 3)]


def drawC(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 3), (current_x, current_y + 4), (current_x + 1, current_y),
            (current_x + 1, current_y + 4), (current_x + 2, current_y), (current_x + 2, current_y + 4)]


def drawD(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 3), (current_x, current_y + 4), (current_x + 1, current_y),
            (current_x + 1, current_y + 4), (current_x + 2, current_y + 1), (current_x + 2, current_y + 2),
            (current_x + 2, current_y + 3)]


def drawE(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 3), (current_x, current_y + 4), (current_x + 1, current_y),
            (current_x + 1, current_y + 2), (current_x + 1, current_y + 4), (current_x + 2, current_y),
            (current_x + 2, current_y + 4)]


def drawF(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 3), (current_x, current_y + 4), (current_x + 1, current_y),
            (current_x + 1, current_y + 2)]


def drawG(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 3), (current_x, current_y + 4), (current_x + 1, current_y),
            (current_x + 1, current_y + 4), (current_x + 2, current_y), (current_x + 2, current_y + 3),
            (current_x + 2, current_y + 4)]


def drawH(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 3), (current_x, current_y + 4), (current_x + 1, current_y + 2),
            (current_x + 2, current_y), (current_x + 2, current_y + 1), (current_x + 2, current_y + 2),
            (current_x + 2, current_y + 3), (current_x + 2, current_y + 4), ]


def drawI(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 4), (current_x + 1, current_y),
            (current_x + 1, current_y + 1), (current_x + 1, current_y + 2), (current_x + 1, current_y + 3),
            (current_x + 1, current_y + 4), (current_x + 2, current_y), (current_x + 2, current_y + 4)]


def drawJ(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 3), (current_x, current_y + 4),
            (current_x + 1, current_y), (current_x + 1, current_y + 4), (current_x + 2, current_y),
            (current_x + 2, current_y + 1), (current_x + 2, current_y + 2), (current_x + 2, current_y + 3),
            (current_x + 2, current_y + 4), (current_x + 3, current_y)]


def drawK(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 3), (current_x, current_y + 4), (current_x + 1, current_y + 2),
            (current_x + 2, current_y), (current_x + 2, current_y + 1), (current_x + 2, current_y + 3),
            (current_x + 2, current_y + 4)]


def drawL(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 3), (current_x, current_y + 4), (current_x + 1, current_y + 4),
            (current_x + 2, current_y + 4)]


def drawM(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 3), (current_x, current_y + 4), (current_x + 1, current_y + 1),
            (current_x + 2, current_y + 2), (current_x + 3, current_y + 1), (current_x + 4, current_y),
            (current_x + 4, current_y + 1), (current_x + 4, current_y + 2), (current_x + 4, current_y + 3),
            (current_x + 4, current_y + 4)]


def drawN(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 3), (current_x, current_y + 4), (current_x + 1, current_y + 1),
            (current_x + 2, current_y + 2), (current_x + 3, current_y), (current_x + 3, current_y + 1),
            (current_x + 3, current_y + 2), (current_x + 3, current_y + 3), (current_x + 3, current_y + 4)]


def drawO(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 3), (current_x, current_y + 4), (current_x + 1, current_y),
            (current_x + 1, current_y + 4), (current_x + 2, current_y), (current_x + 2, current_y + 1),
            (current_x + 2, current_y + 2), (current_x + 2, current_y + 3), (current_x + 2, current_y + 4)]


def drawP(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 3), (current_x, current_y + 4), (current_x + 1, current_y),
            (current_x + 1, current_y + 2), (current_x + 2, current_y), (current_x + 2, current_y + 1),
            (current_x + 2, current_y + 2)]


def drawQ(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 3), (current_x, current_y + 4), (current_x + 1, current_y),
            (current_x + 1, current_y + 4), (current_x + 2, current_y), (current_x + 2, current_y + 1),
            (current_x + 2, current_y + 2), (current_x + 2, current_y + 3), (current_x + 2, current_y + 4),
            (current_x + 3, current_y + 4)]


def drawR(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 3), (current_x, current_y + 4), (current_x + 1, current_y),
            (current_x + 1, current_y + 2), (current_x + 2, current_y), (current_x + 2, current_y + 1),
            (current_x + 2, current_y + 3), (current_x + 2, current_y + 4)]


def drawS(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 4), (current_x + 1, current_y), (current_x + 1, current_y + 2),
            (current_x + 1, current_y + 4), (current_x + 2, current_y), (current_x + 2, current_y + 2),
            (current_x + 2, current_y + 3), (current_x + 2, current_y + 4)]


def drawT(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x + 1, current_y), (current_x + 1, current_y + 1),
            (current_x + 1, current_y + 2), (current_x + 1, current_y + 3), (current_x + 1, current_y + 4),
            (current_x + 2, current_y)]


def drawU(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 3), (current_x, current_y + 4), (current_x + 1, current_y + 4),
            (current_x + 2, current_y), (current_x + 2, current_y + 1), (current_x + 2, current_y + 2),
            (current_x + 2, current_y + 3), (current_x + 2, current_y + 4)]


def drawV(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 3), (current_x + 1, current_y + 4), (current_x + 2, current_y),
            (current_x + 2, current_y + 1), (current_x + 2, current_y + 2), (current_x + 2, current_y + 3)]


def drawW(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x, current_y + 3), (current_x, current_y + 4), (current_x + 1, current_y + 4),
            (current_x + 2, current_y + 3), (current_x + 3, current_y + 4), (current_x + 4, current_y),
            (current_x + 4, current_y + 1), (current_x + 4, current_y + 2), (current_x + 4, current_y + 3),
            (current_x + 4, current_y + 4)]


def drawX(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 4), (current_x + 1, current_y + 1),
            (current_x + 1, current_y + 3), (current_x + 2, current_y + 2), (current_x + 3, current_y + 1),
            (current_x + 3, current_y + 3), (current_x + 4, current_y), (current_x + 4, current_y + 4)]


def drawY(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 2),
            (current_x + 1, current_y + 2), (current_x + 1, current_y + 3), (current_x + 1, current_y + 4),
            (current_x + 2, current_y), (current_x + 2, current_y + 1), (current_x + 2, current_y + 2)]


def drawZ(current_x, current_y):
    """See documentation for drawA()"""
    return [(current_x, current_y), (current_x, current_y + 1), (current_x, current_y + 4),
            (current_x + 1, current_y), (current_x + 1, current_y + 2), (current_x + 1, current_y + 4),
            (current_x + 2, current_y), (current_x + 2, current_y + 3), (current_x + 2, current_y + 4)]
