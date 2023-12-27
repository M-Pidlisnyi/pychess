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

    chosen_piece = None
    run = True
    while run:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                run = False
            if e.type == pg.MOUSEBUTTONDOWN and e.button == 1:

                if chosen_piece is None:
                    for piece in pieces:
                        if piece.rect.collidepoint(e.pos):
                            chosen_piece = piece
                            original_square = chosen_piece.rect
                            # print("chosen piece is " + chosen_piece.name + " at " + str(chosen_piece.rect.coords))
                            break

                else:
                    for sq in chessboard.squares:
                        if sq.collidepoint(e.pos):
                            chosen_piece.update(sq)
                            chosen_piece = None
                            break





        chessboard.draw(window)

        # for piece in pieces:
        #     piece.reset(window)

        pg.display.update()
        pg.time.Clock().tick(FPS)



if __name__ == "__main__":
    game()

