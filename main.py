import pygame as pg
from chessboard import Chessboard
from pieces import Piece

WIDTH = 1300
HEIGHT = 820

SIZE = (WIDTH, HEIGHT)

FPS = 60

BACK = (100, 125, 200)


PIECE_NAMES = ["rook", "knight", "bishop", "queen", "king"]
PIECE_NAMES += PIECE_NAMES[2::-1]

def starting_position(board:Chessboard):
    pieces:list[Piece] = []
    for i in range(64):
        if i < 8:
            piece_name = "black_"+PIECE_NAMES[i%8]+".png"
            new_piece = Piece(board.squares[i], is_white=False)
            new_piece.image = pg.transform.scale(pg.image.load("imgs/"+piece_name), (new_piece.square.width, new_piece.square.height))
 
        if i >= 8 and i < 16:
            new_piece = Piece(board.squares[i], is_white=False)
            new_piece.image = pg.transform.scale(pg.image.load("imgs/black_pawn.png"), (new_piece.square.width, new_piece.square.height))
            new_piece.draw()

        elif i >= 16 and i < 48:
            continue

        elif i >= 48 and i < 56:
            new_piece = Piece(board.squares[i], is_white=True)
            new_piece.image = pg.transform.scale(pg.image.load("imgs/white_pawn.png"), (new_piece.square.width, new_piece.square.height))
            new_piece.draw()
        
        elif i >= 56:
            piece_name = "white_"+PIECE_NAMES[i%8]+".png"
            new_piece = Piece(board.squares[i], is_white=False)
            new_piece.image = pg.transform.scale(pg.image.load("imgs/"+piece_name), (new_piece.square.width, new_piece.square.height))

        pieces.append(new_piece)
    
    return pieces

def run():
    window = pg.display.set_mode(SIZE)
    window.fill(BACK)
    
    board = Chessboard(window)

    board.build()
    pieces = starting_position(board)

    reset_button = pg.Rect(WIDTH-100, 0, 100, 50)
    pg.draw.rect(window, (255,0,0), reset_button)
    


    game_over = False
    choosen_piece = None

    while not game_over:

        for e in pg.event.get():
            if e.type == pg.QUIT:
                game_over = True
            if e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
                if reset_button.collidepoint(e.pos):
                    pieces = starting_position(board)
                if choosen_piece is None:
                    for p in pieces:
                        if p.square.collidepoint(e.pos):
                            p.check_touch()
                            choosen_piece = p
                            break
                else:
                    for s in board.squares:
                        if s.collidepoint(e.pos):
                            choosen_piece.move(new_square=s)
                            choosen_piece = None

            

                    

        
        board.draw()
        for p in pieces:
            p.draw()

        pg.display.update()
        pg.time.Clock().tick(FPS)



if __name__ == "__main__":
    run()

