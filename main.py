from PIL import Image
import letters
import otherCharacters
import calculate

# Change order so the program asks for text first, then makes all calculations, then recomends min number of
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
                print(f"Please enter a number less than {max_num}")
        except ValueError:
            print("Please enter a number")


# First prompt for text
text_for_mosaic = input("Enter the text for the mosaic: ")
width_of_word = calculate.calculateWidthOfWord(text_for_mosaic)
print(width_of_word)

# Calculate the min / recommended
# Print min / recommended

# Then set min to give to getIntFromUser() for width_cubes and height_cubes
# Prompt for dimensions
width_cubes = getIntFromUser("wide", False, 0, 100) * 3
height_cubes = getIntFromUser("tall", False, 0, 100) * 3
print(f"{int(width_cubes / 3)} cubes wide * {int(height_cubes / 3)} cubes tall = {int((width_cubes / 3) * (height_cubes / 3))} cubes total")

# Prompt for colors
mosaic_background_color = getIntFromUser("background", True, 0, 7) - 1
mosaic_text_color = getIntFromUser("text", True, 0, 7) - 1
# Maybe provide a warning / prompt again if background color and text color are the same

# Prompt for name of image to be save to device
image_name = input("Enter name of image (image will be overwritten if already exists): ")

# Generate matrix array of pieces all set to background color
rows = generate_grid(mosaic_background_color, width_cubes, height_cubes)
current_x = 1
current_y = 1

# Add text to matrix array
rows = letters.drawW(rows, current_x, current_y, mosaic_text_color, mosaic_background_color)

# Generate the image
generateImage(rows, width_cubes, height_cubes, image_name)
