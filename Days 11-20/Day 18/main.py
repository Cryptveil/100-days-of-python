import turtle
import colorgram as cg

rgb_colors = []
color_list = cg.extract("image.jpg", 6)

for color in color_list:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)
