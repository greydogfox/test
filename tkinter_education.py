# Учебник по tkinter https://metanit.com/python/tkinter/2.1.php

from tkinter import *
from tkinter import ttk


def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")


root = Tk()  # создаем корневой объект - окно
root.title("Приложение на Tkinter")  # устанавливаем заголовок окна
root.geometry("300x300+600+200")  # устанавливаем размеры окна и позиционирование
root.iconbitmap(default="favicon.ico") # Устанавливает иконку окна. Файл должен быть в папке с файлом программы

# root.resizable(False, False) # запрет растягивания окна. Можно запретить растягивание только по одной стороне
# root.minsize(200, 200)
# root.maxsize(400,400)
label = Label(text="Hello Sergey Onegin")  # создаем текстовую метку
label.pack()  # размещаем метку в окне
root.protocol("WM_DELETE_WINDOW", finish) # Закрытие приложения
# root.attributes("-fullscreen", True) # С помощью attributes можно задавать различные параметры,
# для которых нет определнных команд. Например: -fullsreen (полноэкранный режим), -alpha (прозрачность окна)
# -toolwindow (отключение верхней панели окна (за исключением заголовка и крестика для закрытия)) и др.
# root.attributes("-alpha", 0.5)
# root.attributes("-toolwindow", True)

# виджеты
# btn = Button(text="Exit") # Класический виджет
btn = ttk.Button(text="Exit") # Виджет с использовании библиотеки TTK
btn.pack()



root.mainloop()