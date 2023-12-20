import pygame as pg
from chessboard import Square, ChessBoard, ROWS, COLUMNS, LIGHT_SQUARE_COLOR,DARK_SQUARE_COLOR

WIDTH = 1300
HEIGHT = 820

SIZE = (WIDTH, HEIGHT)

FPS = 60

BACK = (100, 125, 200)


def game():
    window = pg.display.set_mode(SIZE)
    window.fill(BACK)

    chessboard = ChessBoard()
    chessboard.draw(window)

    print(chessboard)



    run = True
    while run:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                run = False
            if e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
                for square in chessboard.squares:
                    if square.collidepoint(e.pos):
                        square.set_piece("abstract piece")


        pg.display.update()
        pg.time.Clock().tick(FPS)



if __name__ == "__main__":
    game()

