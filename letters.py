def drawA(rows, current_x, current_y, text_color, background_color):
    """
    Adds the letter A to the mosaic matrix array at the current coordinates
    Args:
        rows: The matrix array of mosaic pieces
        current_x: The x coordinate where the top left of the letter will be inserted
        current_y: The y coordinate where the top left of the letter will be inserted
        text_color: The color of the text
        background_color: The color of the background of the mosaic
    """
    altered_rows = rows
    # first col
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second col
    rows[current_y][current_x + 1] = text_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = text_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = background_color
    # third row
    rows[current_y][current_x + 2] = text_color
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows

