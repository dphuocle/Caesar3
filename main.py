import pygame as pg
from game import Game


def main():

    running = True
    playing = True

    pg.init()
    pg.mixer.init()
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    clock = pg.time.Clock()


    # implement game
    game = Game(screen, clock)

    while running:


        while playing:
            # game loop here
            game.run()



if __name__ == "__main__":
    main()