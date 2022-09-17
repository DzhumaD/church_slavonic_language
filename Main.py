from tkinter import *
from tkinter import Tk, font
import pyglet, os
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
units = {}  #словарь цифири 1 - 10
dozens = {} #словарь десятков

# спросить какое это число в цифири
# варианты ответов
# считать ответ
# вывести результат

window = Tk()
window.title("Церковно-славянский язык")

window.geometry('400x250')
lbl = Label(window, text="Привет", font=("PonomarUnicode", 50))
lbl.grid(column=0, row=0)
btn = Button(window, text="Не нажимать!")
btn.grid(column=1, row=0)
font.families()
print(font.families())
window.mainloop()