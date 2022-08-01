import tkinter

root = tkinter.Tk()
root.title('Pawnfork')
frame = tkinter.Frame(root)
frame.pack()
canvas = tkinter.Canvas(frame, height = 1000, width = 1000)
canvas.pack()
background = tkinter.PhotoImage(file = './static/images/chessboard.png')
canvas.create_image(0, 0, image = background, anchor = tkinter.NW)
root.mainloop()