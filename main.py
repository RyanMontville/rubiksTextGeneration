from PIL import Image
from letters import drawA
rows = []

def generate_grid(background_color):
    pass


current_x = 1
current_y = 1
# rows = drawA(rows, current_x, current_y, "white", "red")

print(rows)

# img = Image.new('RGB', (30, 30), "WHITE")
#     for row in rows:
#         x_cord = int(row[0])
#         y_cord = int(row[1])
#         color = row[2]
#         rgb = hex_to_rgb(color)
#         img.putpixel((x_cord, y_cord), rgb)
#     username_parts = username.split("@")
#     file_name = f"{username_parts[0]}.png"
#     img.save(file_name)
#     img.show()
