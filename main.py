import tkinter


def draw():
    c.create_rectangle((0, 0), (500, 500), fill="white")
    for i in range(n):
        for j in range(m):
            if board[i][j] in colors:
                color = colors[board[i][j]]
            else:
                color = "white"
            c.create_rectangle((i * cw + 2, j * ch + 2), ((i + 1) * cw, (j + 1) * ch), outline="black", fill=color)
            c.create_text(i * cw + cw // 2, j * ch + ch // 2, text=board[i][j])


def f(event):
    ci = event.x // cw
    cj = event.y // ch
    board[ci][cj] += 1
    draw()


w = tkinter.Tk()
c = tkinter.Canvas(width=500, height=500, background="white")
c.pack()
n, m = 10, 10
board = [[0] * n for i in range(m)]
colors = {0: "white", 1: "green", 2: "blue", 3: "red"}
cw, ch = 500 // n, 500 // m
draw()
c.bind("<Button-1>", f)
w.mainloop()
