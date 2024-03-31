import tkinter as tk
from PIL import Image, ImageOps


window = tk.Tk()
window.title("GUI вместе с tkinter")
window.geometry('300x350')

lbl = tk.Label(text="---")
lbl.pack()

canvas = tk.Canvas(window, width=150, height=150, bg="white")

def recognize():
    print("Hello")
    canvas.postscript(file='my_draw.ps', colormode='gray')
    img = Image.open("my_draw.ps")
    img = ImageOps.invert(img.convert("L").resize((28, 28)))
    img = ImageOps.invert(img)
    # img.show()
    lbl.configure(text="Новый текст")


canvas = tk.Canvas(window,  width=150, height=150, bg="white")
canvas.pack()

btn = tk.Button(window, text="Распознать", command=recognize)
clr = tk.Button(window, text='Очистить', command=lambda: canvas.delete("all"))
btn.pack()
clr.pack()


def draw(event):
    # рисуем линию на холсте
    x1, y1 = (event.x - 4), (event.y - 4)
    x2, y2 = (event.x + 4), (event.y + 4)
    canvas.create_oval(x1, y1, x2, y2, fill="black")

# привязываем обработчики событий
canvas.bind("<B1-Motion>", draw)

window.mainloop()