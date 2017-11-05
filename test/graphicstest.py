import sys
import tkinter
from tkinter import messagebox

panel = tkinter.Tk()
panel.title("fumi's")
panel.geometry("700x700")

def DeleteEntryValue(event):
	box1.delete(0, tkinter.END)

def check(event):
	global val1
	global val2
	text = ""
	if val1.get() == True:
		text += "AI checked\n"
	else: 
		text += "AI not-checked\n"
	if val2.get() == True:
		text += "human checked\n"
	else:
		text += "human not-checked\n"
	messagebox.showinfo('info', text)

def draw(event):
	canvas1.create_rectangle(0,0,100,100, fill='brown', outline='black', width='3.0', tag="rectangle")

def erase(event):
	canvas1.delete("rectangle")

label1 = tkinter.Label(text="fumi's reversi", foreground='#0000ff', background='#aaccff')
label1.pack()

box1 = tkinter.Entry(width=30)
box1.insert(tkinter.END, "input player name here")
box1.pack()
value = box1.get()

button1 = tkinter.Button(text='delete', width=10)
button1.bind("<Button-1>", DeleteEntryValue)
button1.pack()

val1 = tkinter.BooleanVar()
val2 = tkinter.BooleanVar()
val1.set(True)
val2.set(False)
check1 = tkinter.Checkbutton(text='vs AI', variable=val1)
check1.pack()
check2 = tkinter.Checkbutton(text='vs human', variable=val2)
check2.pack()

button2 = tkinter.Button(text='select', width=10)
button2.bind("<Button-1>", check)
button2.pack()

canvas1 = tkinter.Canvas(panel, width=100, height=100)
canvas1.create_rectangle(0,0,100,100, fill='brown', outline='black', width='3.0', tag="rectangle")
canvas1.place(x=0, y=0)

button3 = tkinter.Button(text='draw', width=10)
button3.bind("<Button-1>", draw)
button3.pack()

button4 = tkinter.Button(text='erase', width=10)
button4.bind("<Button-1>", erase)
button4.pack()

panel.mainloop()





"""
参考:
・panel = tkinter.Tk() と panel.mainloop() の間に処理の内容を記述する
・"tk"は"tool kit"の略。"inter"は"interface"?
・pack()で自動的に位置を揃えてウィンドウ上に配置してくれる
・canvas.~ :
	create_line()	直線（折れ線）
	create_oval()	楕円
	create_arc()	円弧（楕円の円周の一部）
	create_rectangle()	矩形
	create_polygon()	多角形
	create_image()	イメージ
	create_bitmap()	ビットマップ
	create_text()	文字列
		fill = 色	内部を塗りつぶす色
		stipple = ビットマップ	内部を塗りつぶすときの模様になるビットマップ
		outline = 色	枠の色
		width = 幅	枠の幅（デフォルトは 1.0）

提案:
・オリジナルなインターフェース。
　リバーシというありふれたゲームをユニークに演出する。
　myiconを白と黒で用意する、のも一つの案。
・タイトル画面では、characterが表と裏でひっくり返っていて、（繰り返し）、
　白黒がひっくり返り続ける。
"""