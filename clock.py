import tkinter as tk
from tkinter import font
from math import *
from datetime import datetime
from time import sleep
from PIL import ImageTk, Image

master = tk.Tk()
master.wm_title("clock")
canvas = tk.Canvas(master, width=300, height=300, background='#F9B7FF', borderwidth=5, relief='raised')

image = Image.open("./res/1.jpg")
photo = ImageTk.PhotoImage(image.resize((700, 700), Image.ANTIALIAS))
#photo = ImageTk.PhotoImage(file="./res/1.jpg")
canvas.create_image(0, 0, image=photo)

canvas.pack(padx=10, pady=10)

f = font.Font(family="Arial", size=10, name="1", weight=font.NORMAL, slant=font.ROMAN, underline=False, overstrike=False)

radiussecond = datetime.now().second
radiusminute = datetime.now().minute
radiushour = datetime.now().hour % 12

x = int(canvas['height']) / 4
y = int(canvas['width']) / 4

diameter = 150


def drawBackground():
    canvas.create_oval(x + 1, y + 1, x + diameter, y + diameter, fill="#0F1010", outline="#5BDB90", width=1)
    canvas.update()


def drawTimeIndicator():
    canvas.create_text(x + diameter / 2 + 1, y + 10, text=str("XII"), anchor="c", fill="#FAFDFD", font=f)
    canvas.create_text(x + 10, y + diameter / 2 + 1, text=str("IX"), anchor="c", fill="#FAFDFD", font=f)
    canvas.create_text(x + diameter / 2 + 1, y + diameter - 10, text=str("VI"), anchor="c", fill="#FAFDFD", font=f)
    canvas.create_text(x + diameter - 10, y + diameter / 2 + 1, text=str("III"), anchor="c", fill="#FAFDFD", font=f)
    canvas.update()


def line(*pts, fill='silver', width=1):
    try:
        if len(pts) == 1:
            new_pts = pts[0]
        else:
            new_pts = list(pts)
        for i in range(len(new_pts)):
            new_pts[i] = new_pts[i] + 1
        l = canvas.create_line(new_pts, fill=fill, width=width, capstyle=tk.ROUND)
        canvas.update()
        return l
    except Exception as e:
        pass


def drawLinesecond(radius):
    angle = radians(radius * 6)
    x1 = 60 * sin(angle)
    y1 = -60 * cos(angle)
    return line(x + diameter / 2 + x1, y + diameter / 2 + y1, x + diameter / 2, y + diameter / 2)


def drawLinemintue(radius):
    angle = radians(radius * 6)
    x1 = 50 * sin(angle)
    y1 = -50 * cos(angle)
    return line(x + diameter / 2 + x1, y + diameter / 2 + y1, x + diameter / 2, y + diameter / 2, fill="#AA5BDB", width=1.2)


def drawLinehour(radius):
    angle = radians(radius * 30)
    x1 = 40 * sin(angle)
    y1 = -40 * cos(angle)
    return line(x + diameter / 2 + x1, y + diameter / 2 + y1, x + diameter / 2, y + diameter / 2, fill="#DB5B88", width=1.5)


i = 2

while True:
    drawBackground()
    drawTimeIndicator()
    lineS = drawLinesecond(radiussecond)
    lineM = drawLinemintue(radiusminute)
    limeH = drawLinehour(radiushour)

    sleep(1)
    canvas.delete(lineS)
    radiussecond += 1
    if radiussecond == 60:
        radiusminute += 1
        radiussecond = 0
        canvas.delete(lineM)
    if radiusminute == 60:
        radiushour += 1
        radiusminute = 0
        canvas.delete(limeH)
        image = Image.open("./res/%s.jpg" % (i))
        photo = ImageTk.PhotoImage(image.resize((700, 700), Image.ANTIALIAS))
        #photo = ImageTk.PhotoImage(file="./res/%s.jpg" % (i))
        canvas.create_image(0, 0, image=photo)
        i += 1
        if i == 12:
            i = 1
    if radiushour == 12:
        radiushour = 0

tk.mainloop()
