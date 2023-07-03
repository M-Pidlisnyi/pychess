import pygame as pg
from random import randint
from math import sqrt

COLS=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ROWS=['8', '7', '6', '5', '4', '3', '2', '1']


#TODO: add coords on screeen
        


class Chessboard:
    dark_square_color = (0,0,0)
    white_square_color = (255,255,255)

    squares: list = []

    def __init__(self, win:pg.Surface):
        self.window = win

    def build(self,size = 800, squares_num = 64):

        self.squares_num = squares_num
        self.rows = int(sqrt(squares_num))
        self.cols = self.rows

        square_size = size/self.rows, size/self.cols

        x = 10
        y = 10 

        for i in range(self.rows):
            for j in range(self.cols):
                new_square = Square(self, (x,y), square_size, (COLS[j],ROWS[i]))
                self.squares.append(new_square)
                x += square_size[0]
    


            x = 10
            y += square_size[1]
        

            
    def draw(self):
       for s in self.squares:
           pg.draw.rect(self.window, s.color, s)


    def set_colors(self, white:tuple, dark:tuple):
        self.white_square_color = white
        self.dark_square_color = dark

        for s in self.squares:
            s.set_color()
    
    def set_size(self, new_size = 800, new_squares_num = 64 ):
        self.squares = []

        self.build(new_size, new_squares_num)



class Square(pg.Rect):
    def __init__(self, board:Chessboard, x_y: tuple[2], size:tuple[2], coords:tuple[str,str]):
        super().__init__(x_y, size)
        self.board = board
        self.coords = coords

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
                       
                       
          
                   





