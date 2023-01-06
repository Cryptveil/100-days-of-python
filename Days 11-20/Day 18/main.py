import turtle
import colorgram as cg

rgb_colors = []
color_list = cg.extract("image.jpg", 6)

for i in range(len(color_list)):
    r = color_list.rgb.r
    g = color_list.rgb.g
    b = color_list.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
