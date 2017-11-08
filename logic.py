#a game of reversi: one-human-player vs ai (on command line)

class Board(object):
  board = []
  def __init__(self, row, col, blank):
    self.row = row
    self.col = col
    self.blank = blank
  
  def createBoard(self):
    for i in range(self.row):
      self.board.append([self.blank]*self.col) #initialize board with "O" to represent open space

  def setBoard(self, set_row, set_col, color):
    self.board[set_row][set_col] = color
  
  def printBoard(self):
    print()
    for i in self.board:
      print("  ".join(i))
    print()

  def endCheck(self, color):
    pass


class Player(object):
  def __init__(self, color, my_board):
    self.color = color
    self.my_board = my_board

  def selectPoint(self):
    self.row = int(input("row: "))
    self.col = int(input("col: "))
    self.putStone()

  def putStone(self):
    if self.row not in range(self.my_board.row) or self.col not in range(self.my_board.col):
      print("invalid input (out of range)")
      self.selectPoint()
    elif self.my_board.board[self.row][self.col]==my_board.blank:
      if self.countUp(self.row, self.col)>0:
        self.my_board.board[self.row][self.col] = self.color
      else:
        print("invalid input (unflippable)")
        self.selectPoint()
    else:
      print("invalid input (already taken)")
      self.selectPoint()
    self.flipStone()

  def flipStone(self):
    #down
    for i in range(self.row+1, my_board.row): #this will not be executed if self.row is out of range
      if my_board.board[i][self.col]==self.color:
        for ii in range(self.row+1, i):
          my_board.board[ii][self.col] = self.color
        break
      elif my_board.board[i][self.col]==my_board.blank:
        break
    #right
    for i in range(self.col+1, my_board.col):
      if my_board.board[self.row][i]==self.color:
        for ii in range(self.col+1, i):
          my_board.board[self.row][ii] = self.color
        break
      elif my_board.board[self.row][i]==my_board.blank:
        break
    #up
    for i in range(self.row-1,-1,-1):
      if my_board.board[i][self.col]==self.color:
        for ii in range(self.row-1,i,-1):
          my_board.board[ii][self.col] = self.color
        break
      elif my_board.board[i][self.col]==my_board.blank:
        break
    #left
    for i in range(self.col-1,-1,-1):
      if my_board.board[self.row][i]==self.color:
        for ii in range(self.col-1,i,-1):
          my_board.board[self.row][ii] = self.color
        break
      elif my_board.board[self.row][i]==my_board.blank:
        break
    #left-upper
    limit = min(self.row, self.col)
    for i in range(1,limit+1):
      if my_board.board[self.row-i][self.col-i]==self.color:
        for ii in range(1,i):
          my_board.board[self.row-ii][self.col-ii] = self.color
        break
      elif my_board.board[self.row-1][self.col-1]==my_board.blank:
        break
    #right-lower
    limit = min(my_board.row-self.row, my_board.col-self.col)
    for i in range(1,limit):
      if my_board.board[self.row+i][self.col+i]==self.color:
        for ii in range(1,i):
          my_board.board[self.row+ii][self.col+ii] = self.color
        break
      elif my_board.board[self.row+i][self.col+i]==my_board.blank:
        break
    #left-lower
    limit = min(my_board.row-self.row, self.col+1)
    for i in range(1,limit):
      if my_board.board[self.row+i][self.col-i]==self.color:
        for ii in range(1,i):
          my_board.board[self.row+ii][self.col-ii] = self.color
        break
      elif my_board.board[self.row+i][self.col-i]==my_board.blank:
        break
    #right-upper
    limit = min(self.row+1, my_board.col-self.col)
    for i in range(1,limit):
      if my_board.board[self.row-i][self.col+i]==self.color:
        for ii in range(1,i):
          my_board.board[self.row-ii][self.col+ii] = self.color
        break
      elif my_board.board[self.row-i][self.col+i]==my_board.blank:
        break

  def countUp(self, row, col):
    count=0
    #down
    for i in range(row+1, my_board.row):
      if my_board.board[i][col]==self.color:
        for ii in range(row+1, i):
          count+=1
        break
      elif my_board.board[i][col]==my_board.blank:
        break
    #right
    for i in range(col+1, my_board.col):
      if my_board.board[row][i]==self.color:
        for ii in range(col+1, i):
          count+=1
        break
      elif my_board.board[row][i]==my_board.blank:
        break
    #up
    for i in range(row-1,-1,-1):
      if my_board.board[i][col]==self.color:
        for ii in range(row-1,i,-1):
          count+=1
        break
      elif my_board.board[i][col]==my_board.blank:
        break
    #left
    for i in range(col-1,-1,-1):
      if my_board.board[row][i]==self.color:
        for ii in range(col-1,i,-1):
          count+=1
        break
      elif my_board.board[row][i]==my_board.blank:
        break
    #left-upper
    limit = min(row, col)
    for i in range(1,limit+1):
      if my_board.board[row-i][col-i]==self.color:
        for ii in range(1,i):
          count+=1
        break
      elif my_board.board[row-1][col-1]==my_board.blank:
        break
    #right-lower
    limit = min(my_board.row-row, my_board.col-col)
    for i in range(1,limit):
      if my_board.board[row+i][col+i]==self.color:
        for ii in range(1,i):
          count+=1
        break
      elif my_board.board[row+i][col+i]==my_board.blank:
        break
    #left-lower
    limit = min(my_board.row-row, col+1)
    for i in range(1,limit):
      if my_board.board[row+i][col-i]==self.color:
        for ii in range(1,i):
          count+=1
        break
      elif my_board.board[row+i][col-i]==my_board.blank:
        break
    #right-upper
    limit = min(row+1, my_board.col-col)
    for i in range(1,limit):
      if my_board.board[row-i][col+i]==self.color:
        for ii in range(1,i):
          count+=1
        break
      elif my_board.board[row-i][col+i]==my_board.blank:
        break
    return count


class ArtificialIntelligence(Player):
  def aiCalculate(self):
    #check the four-corners first
    max_count = 0
    for i in range(2):
      for j in range(2):
        if my_board.board[i*(my_board.row-1)][j*(my_board.col-1)]==my_board.blank:
          count = self.countUp(i*(my_board.row-1),j*(my_board.col-1))
          if count>max_count:
            max_count = count
            self.row = i*(my_board.row-1)
            self.col = j*(my_board.col-1)
    if max_count>0:
      self.putStone()
    else:
      #if corner not possible, select point to get highest return in that round (if multiple choice, select point that appears first)
      max_count = 0
      for i in range(my_board.row):
        for j in range(my_board.col):
          if my_board.board[i][j]==my_board.blank:
            count = self.countUp(i,j)
            if count>max_count:
              max_count = count
              self.row = i
              self.col = j
      if max_count>0: #(could also be written " if max_count: " )
        self.putStone()
      else: #if there are no possible choices left
        my_board.endCheck(self.color)


my_board = Board(8,8,"O")
my_player = Player("B", my_board) #set my_player.color to "B" to represent black
my_ai = ArtificialIntelligence("W", my_board) #set my_ai.color to "W" to represent white
my_board.createBoard()
my_board.setBoard(4,3,my_player.color)
my_board.setBoard(3,4,my_player.color)
my_board.setBoard(3,3,my_ai.color)
my_board.setBoard(4,4,my_ai.color)

while True:
  my_board.printBoard()
  my_player.selectPoint()
  my_board.printBoard()
  my_ai.aiCalculate()

"""
- end process
"""