from tkinter import *
from tkinter import ttk
from datetime import datetime
import pyglet
pyglet.font.add_file('fontes/digital-7.ttf')

# Color
color1 = "#050101" # black
color2 = "#e8e8e8" # white
color3 = "#03fc1c" # green
color4 = "#e02402" # red
color5 = "#736e6d" # gray
color6 = "#0650b8" # blue

global cor
fundo = color1
cor = color2

window = Tk()
window.title("Digital Watch")
window.geometry("400x210")
window.resizable(width=FALSE, height=FALSE) #Não permite que altere o tamanho da pagina
window.config(bg=color1)


def watch():
    time = datetime.now()
    hour = time.strftime("%H:%M:%S")
    day_week = time.strftime("%A")
    day = time.day
    month = time.strftime("%b")
    year = time.strftime("%Y")

    label_hour.config(text=hour)
    label_hour.after(200, watch)
    label_date.config(text=day_week + "   " + str(day) + " / " + str(month) + " / " + str(year))


def alter_color(cor):
    label_hour.config(fg=cor)
    label_date.config(fg=cor)


def color_blue():
    global cor
    cor = color6
    alter_color(cor)


def color_green():
    global cor
    cor = color3
    alter_color(cor)


def color_red():
    global cor
    cor = color4
    alter_color(cor)


#Label
label_hour = Label(window, text=" ", font="digital-7 80", bg=fundo, fg=cor)
label_hour.grid(row=0, column=0, sticky=NW, padx=5)

label_date = Label(window, text=" ", font="digital-7 20", bg=fundo, fg=cor)
label_date.grid(row=1, column=0, sticky=NW, padx=5)

#Button
bblue = Button(window, command=color_blue, text="Azul", width=5, height=2, bg=color6, font='Ivy 10',
relief=RAISED, overrelief=RIDGE)
bblue.place(x=10, y=160)

bgreen = Button(window, command=color_green, text="Verde", width=5, height=2, bg=color3, font='Ivy 10',relief=RAISED, overrelief=RIDGE)
bgreen.place(x=80, y=160)

bred = Button(window, command=color_red, text="Vermelho", width=6, height=2, bg=color4, font='Ivy 10',
            relief=RAISED, overrelief=RIDGE)
bred.place(x=150, y=160)


watch()
window.mainloop()


