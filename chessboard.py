import pygame as pg
from piece import Piece

ROWS = [8,7,6,5,4,3,2,1]
COLUMNS_legacy = ['a','b','c','d','e','f','g','h']
PIECE_NAMES_LIST = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
COLUMNS = {'a': 'rook', 'b': 'knight', 'c': 'bishop', 'd': 'queen', 'e': 'king', 'f': 'bishop', 'g': 'knight', 'h': 'rook'}

LIGHT_SQUARE_COLOR = (230,220,220)
DARK_SQUARE_COLOR  = (170, 150, 50)
class ChessBoard:

    def __init__(self):

        self.squares = []

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


    def starting_position(self) -> list[Piece]:
        pieces = []

        for square in self.squares:
            #black pieces
            if square.coords[1] == 8:
                piece_name = COLUMNS[square.coords[0]]
                pieces.append(Piece(piece_name, square, is_white=False))

            #black pawns
            if square.coords[1] == 7:
                pieces.append(Piece("pawn", square, is_white=False))

            #white pawns
            if square.coords[1] == 2:
                pieces.append(Piece("pawn", square, is_white=True))

            #white pieces
            if square.coords[1] == 1:
                piece_name = COLUMNS[square.coords[0]]
                pieces.append(Piece(piece_name, square, is_white=True))

        return  pieces


    def __str__(self):
        res = ""
        for square in self.squares:
            res += str(square.coords)
        return  res

class Square(pg.Rect):
    def __init__(self, pos: tuple[int,int], coords:tuple[str,int], size:int = 100, is_white=True) -> None:
        super().__init__(pos, (size,size))
        self.coords = coords#coordinates in algebraic chess notation e.g. e4 -> (e,4)

        if is_white:
            self.color = LIGHT_SQUARE_COLOR
        else:
            self.color = DARK_SQUARE_COLOR
        #     self.piece = None


    # def set_piece(self, piece):
    #     if self.piece:
    #         self.piece = None
    #         print("already a piece at " + str(self.coords))
    #     else:
    #         print(str(piece) + " placed at " + str(self.coords))
    #     self.piece = piece


