import tkinter


def f(event):
    c.create_oval((event.x - 10,event.y - 10), (event.x + 10,event.y + 10), fill=color)


def keypress(event):
    global color
    if event.keysym == "r":
        color = "red"
    if event.keysym == "g":
        color = "green"
    if event.keysym == "b":
        color = "blue"


w = tkinter.Tk()
color = "red"
c = tkinter.Canvas(width=500, height=500, background="white")
c.pack()
c.bind("<Motion>", f)
w.bind("<KeyPress>", keypress)
w.mainloop()
