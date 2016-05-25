from tkinter import *
window = Tk()
Figure = Canvas(window, width = 400, height = 400)
Figure.pack()
Figure.create_line(200,0,200,400)

pad1 = Figure.create_rectangle(10,25,20,75, fill = "blue")
pad2 = Figure.create_rectangle(380,325,390,375,fill = "red")

def pad1UP(e):
    Figure.move(pad1, 0, -10)

def pad1DOWN(e):
    Figure.move(pad1, 0, 10)

def pad2UP(e):
    Figure.move(pad2, 0, -10)

def pad2DOWN(e):
    Figure.move(pad2, 0, 10)

def moveball():
    x1, y1, x2, y2 = Figure.coords(ball["obj"])
    x = (x1 + x2) // 2
    y = (y1 + y2) // 2
    dx = 4
    if x < 10 or x > 390:
        ball["dx"] *= -1
    if y < 10 or y > 390:
        ball["dy"] *= -1

    Figure.move(ball["obj"],ball["dx"],ball["dy"])
    window.after(10,moveball)

ball = {"dx":4 , "dy": 4, "obj":Figure.create_oval(190, 190, 210, 210, fill = "yellow")}
window.bind("w", pad1UP)
window.bind("s",pad1DOWN)
window.bind("<Up>", pad2UP)
window.bind("<Down>", pad2DOWN)
window.after(10, moveball)

window.mainloop()
