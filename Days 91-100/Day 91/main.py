import numpy as np
from PIL import Image

# Load the image and convert it to a NumPy array
img = Image.open("image.jpg")
img_data = np.asarray(img)

# Reshape the array to a 2D array of pixels
pixels = img_data.reshape(-1, 3)

# Find the unique colors and their frequency
unique_colors, counts = np.unique(pixels, axis=0, return_counts=True)

# Sort the colors by frequency in descending order
sorted_indices = np.argsort(-counts)
sorted_colors = unique_colors[sorted_indices]

# Convert RGB values to hex codes
hex_colors = [f"#{int(r):02x}{int(g):02x}"
              f"{int(b):02x}" for r, g, b in sorted_colors]

# Print the top 10 most common colors with hex codes
for i in range(10):
    print(f"{i+1}. Hex: {hex_colors[i]} Count: {counts[sorted_indices[i]]}")
