from tkinter import *
root = Tk()
screen = Canvas(root)
screen.pack()
i=[]
a=0 #создаём окошко, холст, массив и т.д.
for j in "red","green","blue",'black',"white","red","green","blue",'black',"white":  #создаём набор квадратиков 
    a+=10
    i.append(screen.create_rectangle((10+a, 10+a, 30+a, 30+a), fill=j, tags=('i')))

def onmotion(event): # самое интересное 
    x = root.winfo_pointerx()-root.winfo_x() # получаем координаты курсора относительно окна
    y = root.winfo_pointery()-root.winfo_y() #
    print (screen.find_overlapping(x+0.5,y-0.5,x+0.5,y+0.5),x,y ) # выводим, какую фигуру(-ы) накрывает квадрат 1х1 пиксель
    print ( screen.itemcget(screen.find_overlapping(x+0.5,y-0.5,x+0.5,y+0.5)[-1], "fill" ) ) # выводим цвет самой верхней фигуры

screen.bind("<Button-1>",onmotion) #привязываем к клику лкм функцию

root.mainloop() # запускаемся