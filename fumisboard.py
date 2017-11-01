import sys
import tkinter

panel = tkinter.Tk()
panel.title("fumi's")
panel.geometry("804x804")

canvas = tkinter.Canvas(panel, width=800, height=800)
canvas.create_rectangle(0,0,800,800, fill='#116611')
canvas.place(x=0, y=0)

for i in range(1,8):
	canvas.create_line(100*i,0,100*i,800, fill='#005500', width=4)
	canvas.create_line(0,100*i,800,100*i, fill='#005500', width=4)

panel.mainloop()