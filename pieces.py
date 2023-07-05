import pygame as pg


class Piece():
    def __init__(self, size: tuple[int, int], square, is_white = True) -> None:
        super().__init__()
        self.image = pg.Surface(size)
        if is_white:
            self.image.fill((200,200,200))
        else:
            self.image.fill((50,50,50))
        self.image = pg.transform.scale(self.image, size)
        self.square = square
    
    def draw(self):
        self.square.board.window.blit(self.image, self.square)


    
    def check_touch(self):
        print(f"touched piece at {self.square.coords[0]}{self.square.coords[1]}")


    
