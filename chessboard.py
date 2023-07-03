import pygame as pg
from random import randint
from math import sqrt
pg.font.init()

COLS=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ROWS=['8', '7', '6', '5', '4', '3', '2', '1']


class Chessboard:
    dark_square_color = (0,0,0)
    white_square_color = (255,255,255)

    squares: list = []

    coords_font = pg.font.Font(None, 40)
    coords_font_size = 40

    def __init__(self, win:pg.Surface, size = 800, squares_num = 64):
        self.window = win
        self.size = size
        self.squares_num = squares_num
        self.rows = int(sqrt(squares_num))
        self.cols = self.rows
        

    def build(self):

        square_size = self.size/self.rows, self.size/self.cols

        x = 10
        y = 10 

        for i in range(self.rows):
            for j in range(self.cols):
                new_square = Square(self, (x,y), square_size, (COLS[j],ROWS[i]))
                self.squares.append(new_square)
                x += square_size[0]
    


            x = 10
            y += square_size[1]
        

            
    



    def set_colors(self, white:tuple, dark:tuple):
        self.white_square_color = white
        self.dark_square_color = dark

        for s in self.squares:
            s.set_color()
    
    def set_size(self, new_size = 800, new_squares_num = 64 ):
        self.size = new_size
        self.squares_num = new_squares_num

    

    def set_font(self, new_font=None, new_font_size=40):
        self.coords_font= pg.font.SysFont(new_font, new_font_size)

        self.build()

    def draw(self):
        self.build()
        for s in self.squares:
            #pg.draw.rect(self.window, s.color, s)
            s.draw()

class Square(pg.Rect):
    def __init__(self, board:Chessboard, x_y: tuple[2], size:tuple[2], coords:tuple[str,str]):
        super().__init__(x_y, size)
        self.board = board
        self.coords = coords

        self.coords_font = self.board.coords_font
        self.coords_font_size = self.board.coords_font_size


        self.color = (0,0,0)
        self.set_color()


    def set_color(self):
        if int(self.coords[1]) % 2 != 0:
            if ord(self.coords[0]) % 2 == 0:
                self.color = self.board.white_square_color
            else:
                self.color = self.board.dark_square_color
        else:
            if ord(self.coords[0]) % 2 != 0:
                self.color = self.board.white_square_color
            else:
                self.color = self.board.dark_square_color


    def draw(self):
        pg.draw.rect(self.board.window, self.color, self)
        if self.coords[0] == 'a':
            row_coord_text = self.coords_font.render(self.coords[1], True, (125,125,125))
            self.board.window.blit(row_coord_text, self.midleft)  
        if self.coords[1] == '1':
            col_coords_text = self.coords_font.render(self.coords[0], True, (125,125,125))
            self.board.window.blit(col_coords_text, (self.centerx, self.bottom-self.coords_font_size))
        
    
                   





