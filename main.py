import pygame as pg

WIDTH = 1300
HEIGHT = 820

SIZE = (WIDTH, HEIGHT)

FPS = 60

BACK = (100, 125, 200)


def game():
    window = pg.display.set_mode(SIZE)
    window.fill(BACK)

    run = True
    while run:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                run = False



        pg.display.update()
        pg.time.Clock().tick(FPS)



if __name__ == "__main__":
    game()

