from tkinter import *
from tkinter import Tk, font
import string
import pyglet, os
import random
import tkinter as tk
##############  Добавление шрифта  ##########################
pyglet.font.add_file('PonomarUnicode.otf')  # Your TTF file name here

# root = tk.Tk()
# MyLabel = tk.Label(root,text="ф",font=('PonomarUnicode',25))
#
# MyLabel.pack()
# root.mainloop()
#############################################################
#
# units = {"a҃": 1, "в҃": 2, "г҃": 3, "д҃": 4, "е҃": 5, "ѕ҃": 6, "з҃": 7, "и҃": 8, "ф҃": 9, }  #словарь цифири 1 - 10
units = ["a҃", "в҃", "г҃", "д҃", "е҃", "ѕ҃", "з҃", "и҃", "ф҃"]      # 1 - 9
dozens = ["і҃", "к҃", "л҃", "м҃", "н҃", "ѯ҃", "о҃", "п҃", "ч҃"]     #словарь десятков 10 - 90

# спросить какое это число в цифири
# варианты ответов
# считать ответ
# вывести результат

# window = Tk()
# window.title("Церковно-славянский язык")
#
# window.geometry('400x250')
# lbl = Label(window, text="a҃", font=("PonomarUnicode", 40))
# lbl.grid(column=0, row=0)
# btn = Button(window, text="Не нажимать!")
# btn.grid(column=1, row=0)
# font.families()
# # print(font.families())
# # print("1",chr(483))
# print("a҃")
# window.mainloop()
r = random.randrange(0, 8, 1)
print("Введите числовое значение цифири: ", units[r])

# print(r)
if (int(input())-1 == r):
    print("Верно!")
else:
    print("Неверно!")
