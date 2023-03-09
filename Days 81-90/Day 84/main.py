from tkinter import Tk, Button, filedialog, Canvas
from PIL import Image, ImageTk, ImageDraw


def open_image():
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path).convert("RGBA")
    return img


def add_watermark():
    global img1, photo, result
    img1 = open_image()

    alpha = 0.5
    # Creating a transparent image
    watermark = Image.new('RGBA', img1.size, (0, 0, 0, 0))
    # Creating a drawing object
    draw = ImageDraw.Draw(watermark)
    # Drawing the watermark text on the transparent image
    draw.text((img1.size[0]/2, img1.size[1]/2), "Watermark",
              fill=(255, 255, 255, int(255*alpha)), align="center")
    # Combining the original image and the watermark image
    result = Image.alpha_composite(img1.convert("RGBA"), watermark)
    photo = ImageTk.PhotoImage(result)

    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=photo)
    canvas.config(width=photo.width(), height=photo.height())


def save_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    print(file_path)
    result.save(file_path)


root = Tk()
root.title("Watermark")

button1 = Button(root, text="Open Image", command=add_watermark)
button1.pack()

canvas = Canvas(root)
canvas.pack()

button2 = Button(root, text="Save Image", command=save_image)
button2.pack()

root.mainloop()
