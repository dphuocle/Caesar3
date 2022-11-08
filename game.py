import pygame as pg
import sys
from map import Map
from settings import TILE_SIZE
from utils import draw_text
from camera import Camera
# from hud import Hud

class Game:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        # map
        self.map = Map(40, 40, self.width, self.height)

        # camera
        self.camera = Camera(self.width, self.height)

        # hud
        # self.hud = Hud

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

    def update(self):
        self.camera.update()

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.screen.blit(self.map.grass_tiles, (self.camera.scroll.x, self.camera.scroll.y))

        for x in range(self.map.grid_length_x):
            for y in range(self.map.grid_length_y):

                render_pos = self.map.map[x][y]["render_pos"]

                tile = self.map.map[x][y]["tile"]
                if tile != "":
                    self.screen.blit(self.map.tiles[tile],
                                    (render_pos[0] + self.map.grass_tiles.get_width()/2 + self.camera.scroll.x,
                                     render_pos[1] - (self.map.tiles[tile].get_height() - TILE_SIZE) + self.camera.scroll.y))

                # p = self.map.map[x][y]["iso_poly"]
                # p = [(x + self.width/2, y) for x, y in p]
                # pg.draw.polygon(self.screen, (0, 0, 0), p, 1)

        # self.hud.draw(self.screen)

        draw_text(
            self.screen,
            'fps={}'.format(round(self.clock.get_fps())),
            25,
            (255, 255, 255),
            (10, 10)
        )

        pg.display.flip()

