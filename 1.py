import tkinter


def f(event):
    c.create_oval((event.x - 10,event.y - 10), (event.x + 10,event.y + 10), fill="red")


w = tkinter.Tk()
c = tkinter.Canvas(width=500, height=500, background="white")
c.pack()
c.bind("<Motion>", f)
w.mainloop()
