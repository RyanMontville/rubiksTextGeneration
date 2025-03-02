from PIL import Image, ImageDraw
import letters
import otherCharacters
import calculate

# Change order so the program asks for text first, then makes all calculations, then recommends min number of
# cubes and dimensions of the mosaic

# red, orange, yellow, green, blue, white
colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (50, 205, 50), (0, 0, 255), (255, 255, 255)]


def generateImage(pixels, width, height, name_of_image, background_color, text_color):
    """Generates the image where one pixel is one piece of a cube.
    Then enlarges the image 5 times to make it easier to read.
    Shows and save the image.
    :param pixels: The list of pixels coordinates
    :param width: width of image - one pixel = one piece of a cube
    :param height: height of the image - one pixel = one piece of a cube
    :param name_of_image: Name of image to be saved to device
    :param background_color: the background color of the image
    :param text_color: the color of the text
    """
    # Create small image
    background = colors[background_color]
    text = colors[text_color]
    img_small = Image.new('RGB', (width, height), background)
    for pixel in pixels:
        img_small.putpixel((pixel[0], pixel[1]), text)
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
    """Draws the grid lines on the image.
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


def drawCharacter(character_to_draw, x_cord, y_cord):
    """Adds the letter to the mosaic array and moves the x coordinate to the proper spot for the next character.
    :param character_to_draw: the current character to add to the mosaic
    :param x_cord: the x coordinate of the top left corner of the character
    :param y_cord: the y coordinate of the top left corner of the character
    :returns (pixels, x_cord)"""
    pixels = []
    match character_to_draw:
        case "a":
            pixels.extend(letters.drawA(x_cord, y_cord))
        case "b":
            pixels.extend(letters.drawB(x_cord, y_cord))
        case "c":
            pixels.extend(letters.drawC(x_cord, y_cord))
        case "d":
            pixels.extend(letters.drawD(x_cord, y_cord))
        case "e":
            pixels.extend(letters.drawE(x_cord, y_cord))
        case "f":
            pixels.extend(letters.drawF(x_cord, y_cord))
        case "g":
            pixels.extend(letters.drawG(x_cord, y_cord))
        case "h":
            pixels.extend(letters.drawH(x_cord, y_cord))
        case "i":
            pixels.extend(letters.drawI(x_cord, y_cord))
        case "j":
            pixels.extend(letters.drawJ(x_cord, y_cord))
        case "k":
            pixels.extend(letters.drawK(x_cord, y_cord))
        case "l":
            pixels.extend(letters.drawL(x_cord, y_cord))
        case "m":
            pixels.extend(letters.drawM(x_cord, y_cord))
        case "n":
            pixels.extend(letters.drawN(x_cord, y_cord))
        case "o":
            pixels.extend(letters.drawO(x_cord, y_cord))
        case "p":
            pixels.extend(letters.drawP(x_cord, y_cord))
        case "q":
            pixels.extend(letters.drawQ(x_cord, y_cord))
        case "r":
            pixels.extend(letters.drawR(x_cord, y_cord))
        case "s":
            pixels.extend(letters.drawS(x_cord, y_cord))
        case "t":
            pixels.extend(letters.drawT(x_cord, y_cord))
        case "u":
            pixels.extend(letters.drawU(x_cord, y_cord))
        case "v":
            pixels.extend(letters.drawV(x_cord, y_cord))
        case "w":
            pixels.extend(letters.drawW(x_cord, y_cord))
        case "x":
            pixels.extend(letters.drawX(x_cord, y_cord))
        case "y":
            pixels.extend(letters.drawY(x_cord, y_cord))
        case "z":
            pixels.extend(letters.drawZ(x_cord, y_cord))
        case "0":
            pixels.extend(otherCharacters.draw0(x_cord, y_cord))
        case "1":
            pixels.extend(otherCharacters.draw1(x_cord, y_cord))
        case "2":
            pixels.extend(otherCharacters.draw2(x_cord, y_cord))
        case "3":
            pixels.extend(otherCharacters.draw3(x_cord, y_cord))
        case "4":
            pixels.extend(otherCharacters.draw4(x_cord, y_cord))
        case "5":
            pixels.extend(otherCharacters.draw5(x_cord, y_cord))
        case "6":
            pixels.extend(otherCharacters.draw6(x_cord, y_cord))
        case "7":
            pixels.extend(otherCharacters.draw7(x_cord, y_cord))
        case "8":
            pixels.extend(otherCharacters.draw8(x_cord, y_cord))
        case "9":
            pixels.extend(otherCharacters.draw9(x_cord, y_cord))
        case "?":
            pixels.extend(otherCharacters.drawQuestion(x_cord, y_cord))
        case "'":
            pixels.extend(otherCharacters.drawApostrophe(x_cord, y_cord))
        case "!":
            pixels.extend(otherCharacters.drawExclamation(x_cord, y_cord))
        case "#":
            pixels.extend(otherCharacters.drawPound(x_cord, y_cord))
        case _:
            pass

    x_cord += calculate.widthOfCharacter(character)
    return pixels, x_cord


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

# Create lines of text with user's dimensions
final_lines = calculate.make_lines_list(text_for_mosaic, width_in_pieces)

# The line_spacing list stores the text for the line, the height of the line,
# and how many pieces are needed before the text to center the text on the mosaic
line_spacing = []
for line in final_lines:
    pieces_before = calculate.centerText(line[0], width_in_pieces)
    line_spacing.append((line[0], line[1], pieces_before))
for line in line_spacing:
    print(line)
pixels_to_place = []
y_cord = 1
if line_spacing[0][1] == 6:
    y_cord = 2
for line in line_spacing:
    x_cord = line[2]
    for character in line[0]:
        result = drawCharacter(character, x_cord, y_cord)
        x_cord = result[1]
        pixels_to_place.extend(result[0])
        if x_cord < width_in_pieces:
            x_cord += 1
    y_cord += line[1] + 1

# Generate the image
generateImage(pixels_to_place, width_in_pieces, height_in_pieces, image_name, mosaic_background_color, mosaic_text_color)
