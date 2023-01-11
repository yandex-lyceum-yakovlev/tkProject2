import tkinter


w = tkinter.Tk()
c = tkinter.Canvas(width=500, height=500, background="white")
c.pack()
n, m = 10, 10
cw, ch = 500 // n, 500 // m
for i in range(n):
    for j in range(m):
        c.create_rectangle((i * cw + 2, j * ch + 2), ((i + 1) * cw, (j + 1) * ch), outline="black")
w.mainloop()
