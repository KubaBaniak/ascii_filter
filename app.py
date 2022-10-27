from sys import argv
from PIL import Image

CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_img(img, new_width=100):
    width, height = img.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = img.resize((new_width, new_height))
    return resized_image


def grayify(img):
    return img.convert('L')


def gray_to_ascii(img):
    pixels = img.getdata()
    characters = "".join([CHARS[pixel//25] for pixel in pixels])
    return characters

def generate_row(chars, width):
    for index in range(0, len(chars), width):
        yield " ".join((chars[index:index+width]))

def main():
    img_path = argv[1] if len(argv) > 1 else "image.png"
    new_width = int(float((argv[2].replace(',', '.')))) if len(argv) > 2 else 32
    with Image.open(img_path) as im:
        im.load()
    img = resize_img(im, new_width)
    gray_img = grayify(img)
    ascii_chars = gray_to_ascii(gray_img)
    for row in generate_row(ascii_chars, new_width):
        print(row)


if __name__ == "__main__":
    main()
