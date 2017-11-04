import sys
import tkinter
from time import sleep
import random

map = [	[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,1,-1,0,0,0],
		[0,0,0,-1,1,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0]]

panel = tkinter.Tk()
panel.title("fumi's")
panel.geometry("804x804")

canvas = tkinter.Canvas(panel, width=800, height=800)
canvas.create_rectangle(0,0,800,800, fill='#116611')
canvas.place(x=0, y=0)

for i in range(1,8):
	canvas.create_line(100*i,0,100*i,800, fill='#005500', width=4)
	canvas.create_line(0,100*i,800,100*i, fill='#005500', width=4)

shiro = tkinter.PhotoImage(file='./images/shiro.pgm')
kuro = tkinter.PhotoImage(file='./images/kuro.pgm')
canvas.create_image(350,350,image=shiro)
canvas.create_image(450,450,image=shiro)
canvas.create_image(350,450,image=kuro)
canvas.create_image(450,350,image=kuro)

ai_x = 0
ai_y = 0
def ai_calc(whos): #algorithm of ai comes here
	global ai_x, ai_y
	#see the corners
	for i in range(0,2):
		for j in range(0,2):
			if (map[i*7][j*7] == 0):
				cnt = count_up((i*7)*100+50, (j*7)*100+50, whos)
				if (cnt != 0):
					ai_x = i*7
					ai_y = j*7
					return cnt
	max_count = 0
	for i in range(0,8):
		placex = i*100+50
		for j in range(0,8):
			placey = j*100+50
			if map[i][j]==0:
				max_count = max(max_count, count_up(placex, placey, whos) ) # 1 represents the color of the ai stone
	rnd = random.randint(1,2)
	if (rnd==1):
		for i in range(0,8):
			placex = i*100+50
			for j in range(0,8):
				placey = j*100+50
				if map[i][j]==0 and count_up(placex, placey, whos)==max_count:
					ai_x = i
					ai_y = j
					return max_count
	else:
		for i in range(7,-1,-1):
			placex = i*100+50
			for j in range(7,-1,-1):
				placey = j*100+50
				if map[i][j]==0 and count_up(placex, placey, whos)==max_count:
					ai_x = i
					ai_y = j
					return max_count


#since black does the first move (according to the rule), set black as the player
whos = -1 # -1->balck, 1->white # better not to use global argument
def draw_stone(event):
	global whos
	placex = int(event.x/100)*100+50
	placey = int(event.y/100)*100+50
	count = count_up(placex, placey, whos)
	#if (there are places to put stone):
	if (map[int((placex - 50) / 100)][int((placey - 50) / 100)] == 0) and (count!=0):
		if whos==1: #white, computer's turn
			print("dead branch")
			# this is a dead branching from two player code
		else: #whos==-1, black, player's turn
			canvas.create_image(placex, placey, image=kuro)
			flip_stone(placex, placey, whos, kuro)
			whos = 1
			#ai moves from below
			global ai_x, ai_y	#
			#time.sleep(1) #wait for 1 sec
			ai_possible = ai_calc(whos)	#
			print("ai_possible: " + str(ai_possible))
			if (ai_possible != 0):
				#palcex = ai_x*100+50#
				print("ai_x: " + str(ai_x))
				#placey = ai_y*100+50#
				print("ai_y: " + str(ai_y))
				#canvas.create_image(placex, placey, image=shiro)
				#flip_stone(placex, placey, whos, shiro)
				canvas.create_image(ai_x*100+50, ai_y*100+50, image=shiro)
				flip_stone(ai_x*100+50, ai_y*100+50, whos, shiro)
				whos = -1
			else: #if there are no place that the ai can put
				finish_check()
			#ai moves until here
	#if (there aren't any places to place stone left):
	else:
		finish_check()
			

def finish_check():
	global whos
	end = 0
	for i in range(0,8):
		for j in range(0,8):
			if map[i][j]==0:
				end = count_up(i*100+50,j*100+50,whos)
				if end!=0: # if there still are possible spaces left
					return
	if end==0: # no possible space to put stone
		#the following block checks whether the opponent can put their stone at spaces left
		#end = 0 #reset end
		for i in range(0,8):
			for j in range(0,8):
				if map[i][j]==0:
					end = count_up(i*100+50,j*100+50,whos*-1)
					if end!=0: # if there still are possible spaces left
						whos *= -1
						return
		#no possible choice for both player; end of game
		white_cnt=0
		black_cnt=0
		for i in range(0,8):
			for j in range(0,8):
				if map[i][j]==1:
					white_cnt+=1
				elif map[i][j]==-1:
					black_cnt+=1
		print("\n-------------\nGAME FINISHED\nRESULT")
		print("white:\t" + str(white_cnt) +"\nblack:\t" + str(black_cnt))
		if (white_cnt>black_cnt):
			print("WINNER:\twhite\n-------------\n")
		elif (black_cnt>white_cnt):
			print("WINNER:\tblack\n-------------\n")
		else:
			print("DRAW\n-------------\n")
		sys.exit()


#return the number of stones that can be flipped, in response to arguments placex and placey 
def count_up(placex, placey, color):
	x = int((placex - 50) / 100)
	y = int((placey - 50) / 100)
	count = 0

	for i in range(x+1,8): #right
		if (map[i][y]==color):
			for ii in range(x+1,i):
				count+=1
			break
		elif (map[i][y]==0):
			break
	
	for i in range(x-1,-1,-1): #left
		if (map[i][y]==color):
			for ii in range(x-1,i,-1):
				count+=1
			break
		elif (map[i][y]==0):
			break
	
	for j in range(y+1,8): #down
		if (map[x][j]==color):
			for jj in range(y+1,j):
				count+=1
			break
		elif (map[x][j]==0):
			break
	
	for j in range(y-1,-1,-1): #up
		if (map[x][j]==color):
			for jj in range(y-1,j,-1):
				count+=1
			break
		elif (map[x][j]==0):
			break
	
	v = min(7-x,y) #right-upper
	for i in range(1,v+1):
		if (map[x+i][y-i]==color):
			for ii in range(1,i):
				count+=1
			break
		elif (map[x+1][y-1]==0):
			break
	
	v = min(7-x,7-y) #right-lower
	for i in range(1,v+1):
		if (map[x+i][y+i]==color):
			for ii in range(1,i):
				count+=1
			break
		elif (map[x+1][y+1]==0):
			break

	v = min(x,y) #left-upper
	for i in range(1,v+1):
		if (map[x-i][y-i]==color):
			for ii in range(1,i):
				count+=1
			break
		elif (map[x-1][y-1]==0):
			break

	v = min(x,7-y) #left-lower
	for i in range(1,v+1):
		if (map[x-i][y+i]==color):
			for ii in range(1,i):
				count+=1
			break
		elif (map[x-1][y+1]==0):
			break

	return count



def flip_stone(placex, placey, color, img):
	x = int((placex - 50) / 100)
	y = int((placey - 50) / 100)
	map[x][y] = color
	
	#flip stones on right, left, down, up

	for i in range(x+1,8): #right
		if (map[i][y]==color):
			for ii in range(x+1,i):
				map[ii][y] = color
				canvas.create_image(ii*100+50, y*100+50, image=img) #better to delete the old image
			break
		elif (map[i][y]==0):
			break
	
	for i in range(x-1,-1,-1): #left
		if (map[i][y]==color):
			for ii in range(x-1,i,-1):
				map[ii][y] = color
				canvas.create_image(ii*100+50, y*100+50, image=img) #better to delete the old image
			break
		elif (map[i][y]==0):
			break
	
	for j in range(y+1,8): #down
		if (map[x][j]==color):
			for jj in range(y+1,j):
				map[x][jj] = color
				canvas.create_image(x*100+50, jj*100+50, image=img) #better to delete the old image
			break
		elif (map[x][j]==0):
			break
	
	for j in range(y-1,-1,-1): #up
		if (map[x][j]==color):
			for jj in range(y-1,j,-1):
				map[x][jj] = color
				canvas.create_image(x*100+50, jj*100+50, image=img) #better to delete the old image
			break
		elif (map[x][j]==0):
			break
	
	#flip stones on diagonals
	
	v = min(7-x,y) #right-upper
	for i in range(1,v+1):
		if (map[x+i][y-i]==color):
			for ii in range(1,i):
				map[x+ii][y-ii] = color
				canvas.create_image((x+ii)*100+50, (y-ii)*100+50, image=img)
			break
		elif (map[x+1][y-1]==0):
			break
	
	v = min(7-x,7-y) #right-lower
	for i in range(1,v+1):
		if (map[x+i][y+i]==color):
			for ii in range(1,i):
				map[x+ii][y+ii] = color
				canvas.create_image((x+ii)*100+50, (y+ii)*100+50, image=img)
			break
		elif (map[x+1][y+1]==0):
			break

	v = min(x,y) #left-upper
	for i in range(1,v+1):
		if (map[x-i][y-i]==color):
			for ii in range(1,i):
				map[x-ii][y-ii] = color
				canvas.create_image((x-ii)*100+50, (y-ii)*100+50, image=img)
			break
		elif (map[x-1][y-1]==0):
			break

	v = min(x,7-y) #left-lower
	for i in range(1,v+1):
		if (map[x-i][y+i]==color):
			for ii in range(1,i):
				map[x-ii][y+ii] = color
				canvas.create_image((x-ii)*100+50, (y+ii)*100+50, image=img)
			break
		elif (map[x-1][y+1]==0):
			break

canvas.bind("<Button>", draw_stone)

panel.mainloop()



"""
- rewrite in object-orientation
- organize code; make it readable
- 保守などのことを考えて、整理されたコードで書く必要がある。デザインパターン、設計原則を意識する。
- アルゴリズムは間違っていないと思われる。しかし、まるでmapが更新されていないかのように、上書きされてしまう時がある。
- 時間のラグが発生しているのは、おそらくpanel.mainloop()を回している中で、関数などを使用しているから。
"""