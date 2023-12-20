import pygame as pg
from chessboard import Square, ChessBoard, ROWS, COLUMNS, LIGHT_SQUARE_COLOR,DARK_SQUARE_COLOR
from piece import  Piece
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

    pieces = chessboard.starting_position()

    run = True
    while run:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                run = False

        for piece in pieces:
            piece.reset(window)

        pg.display.update()
        pg.time.Clock().tick(FPS)



if __name__ == "__main__":
    game()

