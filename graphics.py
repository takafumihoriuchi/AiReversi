import sys
import tkinter

panel = tkinter.Tk()
panel.title("fumi's reversi")
panel.geometry("700x700")

def DeleteEntryValue(event):
	box1.delete(0, tkinter.END)

label1 = tkinter.Label(text='game of reversi', foreground='#ff0000', background='#ffaacc')
label1.pack()
#label1.place(x=350, y=350)

box1 = tkinter.Entry(width=30)
box1.insert(tkinter.END, "input player name here")
box1.pack()
value = box1.get()

button1 = tkinter.Button(text='delete', width=10)
button1.bind("<Button-1>", DeleteEntryValue)
button1.pack()

check1 = tkinter.Checkbutton(text='vs AI')
check1.pack()
check2 = tkinter.Checkbutton(text='vs human')
check2.pack()

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