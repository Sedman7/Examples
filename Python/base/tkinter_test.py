import tkinter as tk
import io
from PIL import Image, ImageOps

# создаем холст
root = tk.Tk()
canvas = tk.Canvas(root, width=100, height=200, bg="white")
canvas.pack()

# рисуем на холсте
canvas.create_rectangle(10, 50, 100, 100, fill="blue")

root.update()

canvas.postscript(file='my_draw.ps', colormode='gray')

img = Image.open("my_draw.ps")
# img.show()
img = ImageOps.invert(img.convert("L").resize((10, 20)))
print(img)

# получаем массив пикселей изображения
pixels = list(img.getdata())

# выводим массив пикселей в консоль
print(pixels)