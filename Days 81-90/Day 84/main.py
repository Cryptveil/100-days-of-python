from PIL import Image


def watermark_with_transparency(input_image_path,
                                output_image_path,
                                watermark_image_path,
                                position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path).thumbnail((500, 100))
    width, height = base_image.size
    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    transparent.paste(watermark, position, mask=watermark)
    transparent.save(output_image_path)


if __name__ == '__main__':
    img = 'images/1.jpg'
    watermark_with_transparency(img, 'output.png',
                                'images/2.png', position=(0,0))
