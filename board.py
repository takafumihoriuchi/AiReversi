import sys
import tkinter

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


whos = -1 # -1->balck, 1->white # better not to use global argument
def draw_stone(event):
	global whos
	placex = int(event.x/100)*100+50
	placey = int(event.y/100)*100+50
	count = count_up(placex, placey, whos)
	if (map[int((placex - 50) / 100)][int((placey - 50) / 100)] == 0) and (count!=0):
		if whos==1:
			canvas.create_image(placex, placey, image=shiro)
			flip_stone(placex, placey, whos, shiro)
			whos = -1
		else:
			canvas.create_image(placex, placey, image=kuro)
			flip_stone(placex, placey, whos, kuro)
			whos = 1
	else:
		end = 0
		for i in range(0,8):
			for j in range(0,8):
				if map[i][j]==0:
					end = count_up(i*100+50,j*100+50,whos)
					if end!=0:
						return
		if end==0:
			white_cnt=0
			black_cnt=0
			for i in range(0,8):
				for j in range(0,8):
					if map[i][j]==1:
						white_cnt+=1
					elif map[i][j]==-1:
						black_cnt+=1
			print("GAME FINISHED\nRESULT")
			print("white:\t" + str(white_cnt) +"\nblack:\t" + str(black_cnt))
			if (white_cnt>black_cnt):
				print("WINNER:\twhite")
			elif (black_cnt>white_cnt):
				print("WINNER:\tblack")
			else:
				print("DRAW")
			sys.exit()
			"""
			must modify so that all the possible spaces get filled, switching and skipping turns
			"""

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

"""