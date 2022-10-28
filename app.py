from sys import argv
from PIL import Image
from flask import Flask,render_template
import urllib.request

#CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
#CHARS = ["@", "%", "#", "*", "+", "=", "-", ":", ".", " "]
CHARS = '''@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''
#CHARS = ["$","@", "B", "%", "8", "&", "W", "M", "#", "*", "o", "a", "h", "k", "b", "d", "p", "q", "w", "m", "Z", "O", "0", "Q", "L", "C", "J", "U", "Y", "X", "z", "c", "v", "u", "n", "x", "r", "j", "f", "t", "/", "\\", "|", "(", ")", "1", "{", "}", "[", "]", "?", "-", "_", "+", "~", "<", ">", "i", "!", "l", "I", ";", ":", ",", '"', "^", "`", "'", ".", " " ]
#CHARS = '@#W$9876543210!abc;:+=,._ '

app = Flask(__name__)


def resize_img(img):
    MAX_WIDTH = 96 
    MAX_HEIGHT = 54
    width, height = img.size
    return img.resize((MAX_WIDTH, MAX_HEIGHT))


def grayify(img):
    return img.convert('L')


def gray_to_ascii(img):
    pixels = img.getdata()
    print(list(pixels))
    characters = "".join([CHARS[int((len(CHARS)-1)*pixel / 255)] for pixel in pixels])
    return characters


def generate_row(chars, width):
    for index in range(0, len(chars), width):
        yield " ".join((chars[index:index+width]))


@app.route("/img2ascii/<path:url>")
def img2ascii(url):
    urllib.request.urlretrieve(url, "image.png")
    with Image.open("image.png") as im:
        im.load()
    im.show()
    gray_img = grayify(im)
    img = resize_img(gray_img)
    width, _ = img.size
    ascii_chars = gray_to_ascii(img)
    return render_template('ascii.html', ascii_list=generate_row(ascii_chars, width))

