import pygame as pg


class Piece():
    def __init__(self, square:pg.Rect, is_white = True) -> None:
        super().__init__()
        self.name = "abstract piece"
        size = square.width-25, square.height-25
        self.image = pg.Surface(size)
        if is_white:
            self.image.fill((200,200,200))
        else:
            self.image.fill((50,50,50))
        self.image = pg.transform.scale(self.image, size)
        self.square = square
    
    def move(self, new_square):
        self.square = new_square
        print(f"{self.name} {new_square.coords[0]}{new_square.coords[1]}")


    def draw(self):
        self.square.board.window.blit(self.image, self.square)

    def check_touch(self):
        print(f"touched {self.name} at {self.square.coords[0]}{self.square.coords[1]}")


    
