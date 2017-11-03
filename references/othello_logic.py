#Brian Wong 34216498 Project 4 ICS 32 Lab 13

NONE = ' '
WHITE = 'O'
BLACK = 'X'

def opposite_color(color: str) -> str:
    """changes the color"""
    if color == BLACK:
        return WHITE
    else:
        return BLACK

    
from collections import namedtuple
Location = namedtuple('Location', ['col', 'row'])



class Piece:
    def __init__(self, color: str, col: int, row: int):
        """Initializes Piece to have a col, row, and color"""
        self._color = color
        self._col = col
        self._row = row

    def get_row(self) -> int:
        """gets the # of rows"""
        return self._row

    def get_col(self) -> int:
        """gets the # of cols"""
        return self._col

    def get_color(self) -> str:
        """Returns color of this Piece"""
        return self._color

    def flipper(self):
        """flips the color of the pieces"""
        if self._color == WHITE:
            self._color = BLACK
        else:
            self._color = WHITE
        



class Board:
    def __init__(self, cols: int, rows:int, top_left_pos: str):
        """Initializes Board to have a col, row, and color"""
        if (cols%2==0 and cols>=4 and cols<=16 and rows%2==0
            and rows>=4 and rows<=16):
            self._col = cols
            self._row = rows
            self._board = self.board() #saves board changes
            self.starting_positions(top_left_pos)
        else:
            raise ValueError()  #handle error in UI, ask user again

    def get_columns(self):
        """gets column number"""
        return self._col

    def get_rows(self):
        """gets row number"""
        return self._row

    def get_board(self):
        """get board"""
        return self._board
    
    def board(self)->list:
        """Creates new board"""
        
        board = []
        for i in range(self._col):
            row = []
            for j in range(self._row):
                row.append(NONE)
            board.append(row)
        return board

    def starting_positions(self, top_left_pos:str):
        """drops pieces in starting locations"""
        if top_left_pos == BLACK:
            opposite_color = WHITE
        else:
            opposite_color = BLACK
        x = int(self._col/2)
        y = int(self._row/2)
        self.drop_on_board(x-1, y-1, top_left_pos)
        self.drop_on_board(x, y, top_left_pos)
        self.drop_on_board(x, y-1, opposite_color)
        self.drop_on_board(x-1, y, opposite_color)
        

    def drop_on_board(self, col: int, row: int, color: str):
        """Puts a piece on the board, checks if it fits on the board, but
           not if its a valid Othello move"""
        self._board[col][row] = Piece(color, col, row)

    def print_board(self) -> None:
        """
        Prints the current state of the board
        """
        board = self._board
        print(' ', end=' ')
        for i in range(len(board)):
            print('{:2d}'.format(i+1), end = ' ') 
        print()

        for row in range(self._row):
            print('{:2d}'.format(row+1), end= ' ')
            for col in range(self._col):
                box = board[col][row] 
                if(box == NONE):
                    print('{:2s}'.format('.'), end=' ')
                else:
                    print('{:2s}'.format(box.get_color()), end=' ')
            print()

        
    

class Game:
    def __init__(self, board_cols:int, board_rows: int,
                 color:str, top_left_pos:str):
        self._cols = board_cols
        self._rows = board_rows
        self._board = Board(board_cols, board_rows, top_left_pos)
        self._current_player = color

    def get_current_player(self):
        """gets current player"""
        return self._current_player

    def test_drop_valid_piece(self, drop_col: int, drop_row: int, color: str) ->list:
        """
          Test for valid drops
          #1 Test if its valid to drop the piece in that place
        """
        pieces = []
        directions = ['right', 'left', 'top', 'bottom', 'top_right', 'top_left', 'bottom_right', 'bottom_left']
        for direction in directions:
            pieces.extend(self.flip_each_direction(drop_col, drop_row, color, direction))
        return pieces
                      

    def drop_valid_piece(self, drop_col: int, drop_row:int):
        """
          Test for valid drops
          #1 flip the pieces that need to be flipped
          #2 drop the piece
        """
        pieces = self.test_drop_valid_piece(drop_col,drop_row,self._current_player)
        
        if len(pieces) != 0:
            for piece in pieces:
                piece.flipper()
            self._board.drop_on_board(drop_col, drop_row, self._current_player)
            self.flips_no_moves()
        else:
            raise ValueError()

        

    def flip_each_direction(self, starting_col: int, starting_row: int, color: str, direction: str) ->list:
        """Find flippable pieces in each direction, returns list of coordinates in that direction"""
        flippable_pieces = []
        loop_count = 0
        i = starting_col
        j = starting_row
        valid = False
        while True:
            if i == starting_col and j == starting_row:
                piece = self._board.get_board()[i][j]
                if type(piece)== Piece:
                    break
            elif i != starting_col or j != starting_row:
                piece = self._board.get_board()[i][j]
                if type(piece) == str: ##is empty
                    break
                elif loop_count == 1: ## piece next to starting point
                    if piece.get_color() == color:
                        break
                elif piece.get_color() == color:
                    valid = True
                    break

                flippable_pieces.append(piece)

            if direction == 'right':
                if i == self._cols-1:
                    break
                i +=1
            elif direction == 'left':
                if i == 0:
                    break
                i -= 1
            elif direction == 'top':
                if j == 0:
                    break
                j -= 1
            elif direction == 'bottom':
                if j == self._rows-1:
                    break
                j += 1
            elif direction == 'top_right':
                if i == self._cols-1 or j == 0:
                    break
                i += 1
                j -= 1
            elif direction == 'top_left':
                if i == 0 or j == 0:
                    break
                i -= 1
                j -= 1
            elif direction == 'bottom_right':
                if i == self._cols-1 or j == self._rows-1:
                    break
                i += 1
                j += 1
            elif direction == 'bottom_left':
                if i == 0 or j == self._rows - 1:
                    break
                i -= 1
                j += 1

            loop_count += 1
                
        if valid:
            return flippable_pieces
        else:
            return []
        
                                      
        ## 1.) if the FIRST spot has a piece that is the opposite color, then can keep going           
        ## 2.) if blank, it means it cant be valid even. if not, keep going
        ## 3.) if you hit a piece after the first one that is your color, it's a valid move
        

    def num_white_piece(self):
        """counts number of white pieces"""
        count = 0
        for column in self._board.get_board():
            for cell in column:
                if type(cell) == Piece and cell.get_color() == WHITE:
                    count +=1
        return count 

    def num_black_piece(self):
        """counts number of black pieces"""
        count = 0
        for column in self._board.get_board():
            for cell in column:
                if type(cell) == Piece and cell.get_color() == BLACK:
                    count +=1
        return count

    def opposite_turn(self):
        """given the player whose turn it is now, return the opposite player"""
        self._current_player = opposite_color(self._current_player)

    
    def list_of_valid_moves(self, color: str):
        """Returns a list of valid moves that a player has"""
        valid = []
        for col in range(self._cols):
            for row in range(self._rows):
                if type(self._board.get_board()[col][row]) == str:
                    flippable_pieces = self.test_drop_valid_piece(col, row, color)
                    if len(flippable_pieces) != 0:
                        valid.append(Location(col=col+1, row=row+1))
        return valid

    def flips_no_moves(self):
        """If the player has no more moves, flip to the next player.
           If the new player has no more moves end game(throw error)."""
        current_player_moves = self.list_of_valid_moves(self._current_player)
        next_color = opposite_color(self._current_player)
        opposite_player_moves = self.list_of_valid_moves(next_color)

        if len(opposite_player_moves) != 0:
            self.opposite_turn()
        elif len(opposite_player_moves) == 0 and len(current_player_moves) == 0:
            ## both players can't move; game over
            raise GameOverError()

class GameOverError(Exception):
    pass
        
        

        


