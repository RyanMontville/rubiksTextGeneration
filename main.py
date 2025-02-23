from PIL import Image
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
    larger_image.save(f"{name_of_image}.png")
    larger_image.show()


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
current_x = 1
current_y = 1

# This list stores the text for the line, the height of the line, and how many pieces are needed before the text to
# center the text on the mosaic
line_spacing = []
for line in final_lines:
    pieces_before = calculate.centerText(line[0], width_in_pieces)
    line_spacing.append((line[0], line[1], pieces_before))

# Add text to matrix array
# EX: rows = letters.drawW(rows, current_x, current_y, mosaic_text_color)

# Generate the image
# generateImage(rows, width_in_pieces, height_in_pieces, image_name)
