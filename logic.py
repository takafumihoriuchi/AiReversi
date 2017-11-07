#a game of reversi: one-human-player vs ai (on command line)

class Board(object):
  board = []
  def __init__(self, row, col):
    self.row = row
    self.col = col
  
  def createBoard(self):
    for i in range(self.row):
      self.board.append(["O"]*self.col) #initialize board with "O" to represent open space

  def setBoard(self, row, col, color):
    self.board[row][col] = color
  
  def printBoard(self):
    print()
    for i in self.board:
      print("  ".join(i))
    print()


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
    elif self.my_board.board[self.row][self.col]=="O":
      self.my_board.board[self.row][self.col] = self.color
    else:
      print("invalid input (already taken)")
      self.selectPoint()
    self.flipStone()

  def flipStone(self):
    pass


class ArtificialIntelligence(Player):
  pass


my_board = Board(8,8)
my_board.createBoard()
my_board.setBoard(4,3,"B")
my_board.setBoard(3,4,"B")
my_board.setBoard(3,3,"W")
my_board.setBoard(4,4,"W")
my_board.printBoard()

my_player = Player("B", my_board) #set my_player.color to "B" to represent black
my_ai = ArtificialIntelligence("W", my_board) #set my_ai.color to "W" to represent white

while True:
  my_player.selectPoint()
  my_board.printBoard()
