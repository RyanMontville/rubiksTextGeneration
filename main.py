from PIL import Image, ImageDraw
import letters
import otherCharacters
import calculate

# Change order so the program asks for text first, then makes all calculations, then recommends min number of
# cubes and dimensions of the mosaic

# red, orange, yellow, green, blue, white
colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (50, 205, 50), (0, 0, 255), (255, 255, 255)]


def generate_grid(background_color, width, height):
    """
    Generate a matrix array for the mosaic
    and fills every pixel the background color
    :param background_color: The background color of the mosaic
    :param width: How wide will the mosaic be. (Number of cubes * 3 pieces)
    :param height: How tall will the mosaic be. (Number of cubes * 3 pieces)
    """
    grid = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(background_color)
        grid.append(row)

    return grid


def generateImage(pixel_rows, width, height, name_of_image):
    """Generates the image where one pixel is one piece of a cube.
    Then enlarges the image 5 times to make it easier to read.
    Shows and save the image.
    :param pixel_rows: The matrix array of piece colors
    :param width: width of image - one pixel = one piece of a cube
    :param height: height of the image - one pixel = one piece of a cube
    :param name_of_image: Name of image to be saved to device
    """
    # Create small image
    img_small = Image.new('RGB', (width, height), "WHITE")
    for y in range(len(pixel_rows)):
        row = pixel_rows[y]
        for x in range(len(row)):
            color_rgb = colors[row[x]]
            img_small.putpixel((x, y), color_rgb)
    # Enlarge image
    image = img_small
    original_width, original_height = image.size
    new_size = (original_width * 50, original_height * 50)
    larger_image = image.resize(new_size, Image.NEAREST)
    # Draw grid lines
    width = new_size[0]
    height = new_size[1]
    draw = ImageDraw.Draw(image)
    for y in range(0, height, 20):
        draw.line([(0, y), (width, y)], fill=(0, 0, 0))

    larger_image.save(f"{name_of_image}.png")
    draw_grid_lines(f"{name_of_image}.png")


def draw_grid_lines(image):
    """
    Draws the grid lines on the image.
    Args:
        image: name of the image.
    """
    img = Image.open(image).convert("RGB")
    draw = ImageDraw.Draw(img)
    width, height = img.size
    line_count = 0
    for y in range(0, height, 50):
        if line_count % 3 == 0:
            draw.line([(0, y), (width, y)], fill=(0, 0, 0), width=4)
        else:
            draw.line([(0, y), (width, y)], fill=(0, 0, 0))
        line_count += 1
    line_count = 0
    for x in range(0, width, 50):
        if line_count % 3 == 0:
            draw.line([(x, 0), (x, height)], fill=(0, 0, 0), width=4)
        else:
            draw.line([(x, 0), (x, height)], fill=(0, 0, 0))
        line_count += 1

    img.save(image)
    img.show()


def getIntFromUser(prompt, is_color, min_num, max_num):
    """Prompts the user for a number, then check if the input is a number and
    if it is within the proper range
    :param prompt: The missing word from the prompt
    :param is_color: Boolean to determine which prompt phrase to use
    :param min_num: The number the user input should be larger than
    :param max_num: The number the user input should be smaller than
    """
    is_input_number = False
    while not is_input_number:
        if is_color:
            response = input(f"Enter the number of the color for the {prompt} color [1: red, 2: orange, 3: yellow, 4: green, 5: blue, 6: white]: ")
        else:
            response = input(f"Enter how many cubes {prompt} the mosaic will be: ")
        try:
            int(response)
            if min_num < int(response) < max_num:
                return int(response)
            else:
                if is_color:
                    print("Please enter a number 1 - 6")
                else:
                    print(f"Please enter a number larger than {min_num}")
        except ValueError:
            print("Please enter a number")


def drawCharacter(character, x_cord, y_cord, mosaic_grid, text_color, is_first_character):
    """Adds the letter to the mosaic array and moves the x coordinate to the proper spot for the next character.
    :param character: the current character to add to the mosaic
    :param x_cord: the x coordinate of the top left corner of the character
    :param y_cord: the y coordinate of the top left corner of the character
    :param mosaic_grid: the mosaic grid to add the character pieces to
    :param text_color: the color of the text
    :param is_first_character: boolean to tell the function to not add a space before the first letter
    :returns (updated_grid, x_cord)"""
    updated_grid = []
    if not is_first_character:
        x_cord += 1
    match character:
        case "a":
            updated_grid = letters.drawA(mosaic_grid, x_cord, y_cord, text_color)
        case "b":
            updated_grid = letters.drawB(mosaic_grid, x_cord, y_cord, text_color)
        case "c":
            updated_grid = letters.drawC(mosaic_grid, x_cord, y_cord, text_color)
        case "d":
            updated_grid = letters.drawD(mosaic_grid, x_cord, y_cord, text_color)
        case "e":
            updated_grid = letters.drawE(mosaic_grid, x_cord, y_cord, text_color)
        case "f":
            updated_grid = letters.drawF(mosaic_grid, x_cord, y_cord, text_color)
        case "g":
            updated_grid = letters.drawG(mosaic_grid, x_cord, y_cord, text_color)
        case "h":
            updated_grid = letters.drawH(mosaic_grid, x_cord, y_cord, text_color)
        case "i":
            updated_grid = letters.drawI(mosaic_grid, x_cord, y_cord, text_color)
        case "j":
            updated_grid = letters.drawJ(mosaic_grid, x_cord, y_cord, text_color)
        case "k":
            updated_grid = letters.drawK(mosaic_grid, x_cord, y_cord, text_color)
        case "l":
            updated_grid = letters.drawL(mosaic_grid, x_cord, y_cord, text_color)
        case "m":
            updated_grid = letters.drawM(mosaic_grid, x_cord, y_cord, text_color)
        case "n":
            updated_grid = letters.drawN(mosaic_grid, x_cord, y_cord, text_color)
        case "o":
            updated_grid = letters.drawO(mosaic_grid, x_cord, y_cord, text_color)
        case "p":
            updated_grid = letters.drawP(mosaic_grid, x_cord, y_cord, text_color)
        case "q":
            updated_grid = letters.drawQ(mosaic_grid, x_cord, y_cord, text_color)
        case "r":
            updated_grid = letters.drawR(mosaic_grid, x_cord, y_cord, text_color)
        case "s":
            updated_grid = letters.drawS(mosaic_grid, x_cord, y_cord, text_color)
        case "t":
            updated_grid = letters.drawT(mosaic_grid, x_cord, y_cord, text_color)
        case "u":
            updated_grid = letters.drawU(mosaic_grid, x_cord, y_cord, text_color)
        case "v":
            updated_grid = letters.drawV(mosaic_grid, x_cord, y_cord, text_color)
        case "w":
            updated_grid = letters.drawW(mosaic_grid, x_cord, y_cord, text_color)
        case "x":
            updated_grid = letters.drawX(mosaic_grid, x_cord, y_cord, text_color)
        case "y":
            updated_grid = letters.drawY(mosaic_grid, x_cord, y_cord, text_color)
        case "z":
            updated_grid = letters.drawZ(mosaic_grid, x_cord, y_cord, text_color)
        case "0":
            updated_grid = otherCharacters.draw0(mosaic_grid, x_cord, y_cord, text_color)
        case "1":
            updated_grid = otherCharacters.draw1(mosaic_grid, x_cord, y_cord, text_color)
        case "2":
            updated_grid = otherCharacters.draw2(mosaic_grid, x_cord, y_cord, text_color)
        case "3":
            updated_grid = otherCharacters.draw3(mosaic_grid, x_cord, y_cord, text_color)
        case "4":
            updated_grid = otherCharacters.draw4(mosaic_grid, x_cord, y_cord, text_color)
        case "5":
            updated_grid = otherCharacters.draw5(mosaic_grid, x_cord, y_cord, text_color)
        case "6":
            updated_grid = otherCharacters.draw6(mosaic_grid, x_cord, y_cord, text_color)
        case "7":
            updated_grid = otherCharacters.draw7(mosaic_grid, x_cord, y_cord, text_color)
        case "8":
            updated_grid = otherCharacters.draw8(mosaic_grid, x_cord, y_cord, text_color)
        case "9":
            updated_grid = otherCharacters.draw9(mosaic_grid, x_cord, y_cord, text_color)
        case "?":
            updated_grid = otherCharacters.drawQuestion(mosaic_grid, x_cord, y_cord, text_color)
        case "'":
            updated_grid = otherCharacters.drawApostrophe(mosaic_grid, x_cord, y_cord, text_color)
        case "!":
            updated_grid = otherCharacters.drawExclamation(mosaic_grid, x_cord, y_cord, text_color)
        case "#":
            updated_grid = otherCharacters.drawPound(mosaic_grid, x_cord, y_cord, text_color)
        case _:
            pass

    x_cord += calculate.widthOfCharacter(character)
    return updated_grid, x_cord


# First prompt for text
text_for_mosaic = input("Enter the text for the mosaic: ").lower()

# Calculate the minimum number of cubes needed and the recommended dimensions
min_size = calculate.calculateMinimumSize(text_for_mosaic)
# Print the minimum number of cubes needed, the recommended dimensions, and a preview of how many lines the text will
# be split into.
print("\nMinimum cubes needed to make this mosaic:")
print(f"{min_size[0]} cubes wide by {min_size[1]} cubes tall")
print(f"{min_size[0] * min_size[1]} cubes needed in total")
print("\nPreview with minimum dimensions: ")
for line in min_size[2]:
    print(line[0])

# Prompt for dimensions
print("\n")
width_in_pieces = getIntFromUser("wide", False, min_size[0] - 1, 100) * 3
height_in_pieces = getIntFromUser("tall", False, min_size[1] - 1, 100) * 3
print(f"Your mosaic will be {int(width_in_pieces / 3)} cubes wide * {int(height_in_pieces / 3)} cubes tall ="
      f" {int((width_in_pieces / 3) * (height_in_pieces / 3))} cubes total\n")
# Prompt for colors
mosaic_background_color = getIntFromUser("background", True, 0, 7) - 1
mosaic_text_color = getIntFromUser("text", True, 0, 7) - 1
# Provide a warning / prompt again if background color and text color are the same
same_color = False
if mosaic_background_color == mosaic_text_color:
    same_color = True
while same_color:
    print("\nWarning! You have selected the same text color as the background. This will generate an image of one "
          "solid color.")
    color_to_change = input("Do you wan to change the [text] color or [background] color: ").lower()
    if color_to_change == "text":
        mosaic_text_color = getIntFromUser("text", True, 0, 7) - 1
    else:
        mosaic_background_color = getIntFromUser("background", True, 0, 7) - 1
    if mosaic_background_color != mosaic_text_color:
        same_color = False
# Prompt for name of image to be saved to device
image_name = input("Enter name of image (image will be overwritten if already exists): ")

# Create lines fo text with user's dimensions
final_lines = calculate.make_lines_list(text_for_mosaic, width_in_pieces)
# Generate matrix array of pieces all set to background color
rows = generate_grid(mosaic_background_color, width_in_pieces, height_in_pieces)
# The line_spacing list stores the text for the line, the height of the line,
# and how many pieces are needed before the text to center the text on the mosaic
line_spacing = []
for line in final_lines:
    pieces_before = calculate.centerText(line[0], width_in_pieces)
    line_spacing.append((line[0], line[1], pieces_before))

# Add text to matrix array
current_x = 0
current_y = 1
for line in line_spacing:
    if line[1] == 6:
        current_y += 1
    # current_x = line[2] - 2 this is the centering. Fix this!!!
    print(f"x cord on first letter: {current_x}")
    result = drawCharacter(line[0][0], current_x, current_y, rows, mosaic_text_color, True)
    rows = result[0]
    current_x = result[1]
    for i in range(1, len(line[0])):
        letter = line[0][i]
        print(f"Letter: {letter} = X: {current_x}, Y: {current_y}")
        result = drawCharacter(letter, current_x, current_y, rows, mosaic_text_color, False)
        rows = result[0]
        current_x = result[1]
    current_x = 0
    current_y += line[1] + 1


# Generate the image
generateImage(rows, width_in_pieces, height_in_pieces, image_name)
