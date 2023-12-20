import pygame as pg


class Piece(pg.sprite.Sprite):
    def __init__(self, name:str, square:pg.Rect, size=(75,80), is_white:bool=True):
        super().__init__()
        self.is_white = is_white
        if is_white:
            filename = "imgs/white_"+name+".png"
        else:
            filename = "imgs/black_"+name+".png"
        self.image =  pg.transform.scale(pg.image.load(filename), size)
        self.rect = square
        self.name = name

    def reset(self, window:pg.Surface, shift_x=10, shift_y=10):
        window.blit(self.image, (self.rect.x+shift_x, self.rect.y+shift_y))

    def __str__(self):
        return self.name