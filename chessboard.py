import pygame as pg

ROWS = [8,7,6,5,4,3,2,1]
COLUMNS = ['a','b','c','d','e','f','g','h']
LIGHT_SQUARE_COLOR = (255,255,255)
DARK_SQUARE_COLOR  = (0, 0, 0)
class ChessBoard:

    def __init__(self):

        self.squares = []

        #TODO implement list of square as matrix
        start_x = 10
        y = 10
        square_size = 100
        is_white = True

        for row in ROWS:
            x = start_x
            for column in COLUMNS:
                sq = Square((x, y), (column, row), is_white=is_white)
                self.squares.append(sq)
                x += square_size
                is_white = not is_white#cycle white/black every square
            is_white = not is_white#also cycle first white/first black square every row
            y += square_size

    def draw(self, window):
        for square in self.squares:
            pg.draw.rect(window, square.color, square)


    def __str__(self):
        res = ""
        for square in self.squares:
            res += str(square.coords)
        return  res

class Square(pg.Rect):
    def __init__(self, pos: tuple[int,int], coords:tuple[str,int], size:int = 100, is_white=True) -> None:
        super().__init__(pos, (size,size))
        self.coords = coords
        self.piece = None
        if is_white:
            self.color = LIGHT_SQUARE_COLOR
        else:
            self.color = DARK_SQUARE_COLOR

    def set_piece(self, piece):
        #TODO implement pieces

        if self.piece:
            self.piece = None
            print("already a piece at " + str(self.coords))
        else:
            print(piece + " placed at " + str(self.coords))
        self.piece = piece


