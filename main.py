from PIL import Image
from letters import drawA

# red, orange, yellow, green, blue, white
colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (50, 205, 50), (0, 0, 255), (255, 255, 255)]


def generate_grid(background_color, width, height):
    grid = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(background_color)
        grid.append(row)

    return grid


def enlargeImage(original_image, new_image_name):
    image = original_image
    original_width, original_height = image.size
    new_size = (original_width * 50, original_height * 50)
    larger_image = image.resize(new_size, Image.NEAREST)
    larger_image.save(f"{new_image_name}.png")
    larger_image.show()


def generateImage(pixel_rows, width, height):
    img_small = Image.new('RGB', (width, height), "WHITE")
    for y in range(len(pixel_rows)):
        row = pixel_rows[y]
        for x in range(len(row)):
            color_rgb = colors[row[x]]
            img_small.putpixel((x, y), color_rgb)
    return img_small


def getIntFromUser(prompt, is_color, max_num):
    is_input_number = False
    while not is_input_number:
        if is_color:
            response = input(f"Enter the number of the color for the {prompt} color [1: red, 2: orange, 3: yellow, 4: green, 5: blue, 6: white]: ")
        else:
            response = input(f"Enter how many cubes {prompt} the mosaic will be: ")
        try:
            int(response)
            if int(response) < max_num:
                return int(response)
            else:
                print(f"Please enter a number less than {max_num}")
        except ValueError:
            print("Please enter a number")


mosaic_background_color = getIntFromUser("background", True, 7) - 1
mosaic_text_color = getIntFromUser("text", True, 7) - 1
width_cubes = getIntFromUser("wide", False, 100) * 3
height_cubes = getIntFromUser("tall", False, 100) * 3
print(f"{int(width_cubes / 3)} cubes wide * {int(height_cubes / 3)} cubes tall = {int((width_cubes / 3)  * (height_cubes / 3))} cubes total")
image_name = input("Enter name of image (image will be overwritten if already exists): ")
rows = generate_grid(mosaic_background_color, width_cubes, height_cubes)
current_x = 1
current_y = 1

rows = drawA(rows, current_x, current_y, mosaic_text_color, mosaic_background_color)

img = generateImage(rows, width_cubes, height_cubes)
enlargeImage(img, image_name)
