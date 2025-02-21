def drawA(rows, current_x, current_y, text_color, background_color):
    altered_rows = rows
    # first col
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x] = text_color
    rows[current_y + 2][current_x] = text_color
    rows[current_y + 3][current_x] = text_color
    rows[current_y + 4][current_x] = text_color
    # second col
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x + 1] = background_color
    rows[current_y + 2][current_x + 1] = text_color
    rows[current_y + 3][current_x + 1] = background_color
    rows[current_y + 4][current_x + 1] = background_color
    # third row
    rows[current_y][current_x] = text_color
    rows[current_y + 1][current_x + 2] = text_color
    rows[current_y + 2][current_x + 2] = text_color
    rows[current_y + 3][current_x + 2] = text_color
    rows[current_y + 4][current_x + 2] = text_color

    return altered_rows

