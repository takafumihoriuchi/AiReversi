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

label1 = tkinter.Label(text="fumi's reversi", foreground='#0000ff', background='#aaccff')
label1.pack()
#label1.place(x=350, y=350)

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

panel.mainloop()





"""
参考:
・panel = tkinter.Tk() と panel.mainloop() の間に処理の内容を記述する
・"tk"は"tool kit"の略。"inter"は"interface"?
・pack()で自動的に位置を揃えてウィンドウ上に配置してくれる

提案:
・オリジナルなインターフェース。
　リバーシというありふれたゲームをユニークに演出する。
　myiconを白と黒で用意する、のも一つの案。
"""