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
  def __init__(self, color):
    self.color = color

  def selectPoint(self, which_board):
    self.row = int(input("row: "))
    self.col = int(input("col: "))
    self.putStone(which_board)

  def putStone(self, which_board):
    if self.row not in range(which_board.row) or self.col not in range(which_board.col):
      print("invalid input (out of range)")
      self.selectPoint(which_board) #error here
    elif which_board.board[self.row][self.col]=="O":
      which_board.board[self.row][self.col] = self.color
    else:
      print("invalid input (already taken)")
      self.selectPoint(which_board)
    self.flipStone(which_board)

  def flipStone(self, which_board):
    


class ArtificialIntelligence(Player):
  pass


my_board = Board(8,8)
my_board.createBoard()
my_board.setBoard(4,3,"B")
my_board.setBoard(3,4,"B")
my_board.setBoard(3,3,"W")
my_board.setBoard(4,4,"W")
my_board.printBoard()
my_player = Player("B") #set my_player.color to "B" to represent black
my_ai = ArtificialIntelligence("W") #set my_ai.color to "W" to represent white

while True:
  my_player.selectPoint(my_board)
  my_board.printBoard()


"""
board = []

for x in range(0, 8):
  board.append(["O"] * 8) #this is an alphabet 'O', not a zero!

def print_board(board):
  for row in board:
    print("  ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#print ship_row
#print ship_col

for turn in range(4):
  print("Turn", turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sank my battleship!")
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print("You guessed that one already.")
    else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    print_board(board)
    if turn == 3:
      print("Game Over")
"""