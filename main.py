import pygame as pg
from chessboard import Chessboard
from pieces import Piece

WIDTH = 1300
HEIGHT = 820

SIZE = (WIDTH, HEIGHT)

FPS = 60

BACK = (100, 125, 200)



def run():
    window = pg.display.set_mode(SIZE)
    window.fill(BACK)
    
    board = Chessboard(window)
    board.build()
   
    pieces:list[Piece] = []
    for i in range(64):
        
        if i < 16:
            new_piece = Piece( (board.squares[i].width-25, board.squares[i].height-25),board.squares[i], is_white=False )
            #window.blit(new_piece.image, board.squares[i])
            new_piece.draw()
        elif i >= 16 and i < 48:
            continue
        elif i >= 48:
            new_piece = Piece( (board.squares[i].width-25, board.squares[i].height-25),board.squares[i], is_white=True )
            #window.blit(new_piece.image, board.squares[i+32])
            new_piece.draw()
        pieces.append(new_piece)




    game_over = False
    while not game_over:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                game_over = True
            if e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
                for p in pieces:
                    if p.square.collidepoint(e.pos):
                        p.check_touch()
        
        board.draw()
        for p in pieces:
            p.draw()

        pg.display.update()
        pg.time.Clock().tick(FPS)



if __name__ == "__main__":
    run()

