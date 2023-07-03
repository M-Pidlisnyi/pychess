import pygame as pg

WIDTH = 1300
HEIGHT = 700

SIZE = (WIDTH, HEIGHT)

FPS = 60

BACK = (100, 125, 200)



def run():
    window = pg.display.set_mode(SIZE)
    window.fill(BACK)
    
    game_over = False

    while not game_over:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                game_over = True


        pg.display.update()
        pg.time.Clock().tick(FPS)



if __name__ == "__main__":
    run()

