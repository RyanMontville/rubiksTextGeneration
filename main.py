from PIL import Image
from letters import drawA


def generate_grid(background_color, width, height):
    mosaic_pixel_width = width * 3
    mosaic_pixel_height = height * 3
    grid = []
    for y in range(mosaic_pixel_height):
        row = []
        for x in range(mosaic_pixel_width):
            row.append(background_color)
        grid.append(row)

    return grid


def color_name_to_rgb(color_name):
    match color_name:
        case "red":
            return 255, 0, 0
        case "yellow":
            return 255, 255, 0
        case "orange":
            return 255, 165, 0
        case "green":
            return 50, 205, 50
        case "blue":
            return 0, 0, 255
        case "white":
            return 255, 255, 255


def enlargeImage(original_image, new_image_name):
    image = original_image
    original_width, original_height = image.size
    new_size = (original_width * 50, original_height * 50)
    larger_image = image.resize(new_size, Image.NEAREST)
    larger_image.save(new_image_name)
    larger_image.show()


def generateImage(pixel_rows):
    img_small = Image.new('RGB', (30, 30), "WHITE")
    for y in range(len(rows)):
        row = rows[y]
        for x in range(len(row)):
            color_name = row[x]
            color_rgb = color_name_to_rgb(color_name)
            img_small.putpixel((x, y), color_rgb)
    return img_small


mosaic_background_color = input("Enter background color [red, orange, yellow, green, blue, white]: ")
mosaic_text_color = input("Enter text color [red, orange, yellow, green, blue, white]: ")
width_cubes = int(input("Enter how many cubes wide the mosaic will be: "))
height_cubes = int(input("Enter how many cubes tall the mosaic will be: "))
print(f"{width_cubes} cubes wide * {height_cubes} cubes tall = {width_cubes * height_cubes} cubes total")
rows = generate_grid(mosaic_background_color, 10, 10)
current_x = 1
current_y = 1

rows = drawA(rows, current_x, current_y, mosaic_text_color, mosaic_background_color)

img = generateImage(rows)
enlargeImage(img, "final.png")
