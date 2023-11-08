import sys

sys.path.insert(0, '..')

import pygame as pg
from View.settings import *


class Camera:

    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.factorx = (144.3 * 1.0) / 1820
        self.factory = (111 * 1.0) / 1400
        self.scroll = pg.Vector2(520, 600)
        self.scroll_mini = pg.Vector2(0, 0)
        self.dx = 0
        self.dy = 0
        self.speed = 23
        self.rect = pg.Rect((1382.5, 59.5, 144.3, 111))

    def update(self):

        mouse_pos = pg.mouse.get_pos()
        # x movement
        if mouse_pos[0] > self.width * 0.99:
            self.dx = -self.speed
        elif mouse_pos[0] < self.width * 0.02:
            self.dx = self.speed
        else:
            self.dx = 0

        # y movement
        if mouse_pos[1] > self.height * 0.99:
            self.dy = -self.speed
        elif mouse_pos[1] < self.height * 0.02:
            self.dy = self.speed
        else:
            self.dy = 0

        # update camera scroll

        # camera-x
        self.scroll.x += self.dx
        self.scroll_mini.x += self.dx * self.factorx

        # limitation for scrolling camera-x
        if self.scroll.x < -1220:
            self.scroll.x = -1220
        if self.scroll.x > 600:
            self.scroll.x = 600

            # limitation for scrolling camera-mini-x
        if self.scroll_mini.x < -144.3 + 26:
            self.scroll_mini.x = -144.3 + 26
        if self.scroll_mini.x > 0:
            self.scroll_mini.x = 0

            # camera-y
        self.scroll.y += self.dy
        self.scroll_mini.y -= self.dy * self.factory

        # limitation for scrolling camera-y
        if self.scroll.y < -850:
            self.scroll.y = -850
        if self.scroll.y > 550:
            self.scroll.y = 550

        # limitation for scrolling camera-mini-y
        if self.scroll_mini.y > 111 - 20:
            self.scroll_mini.y = 111 - 20
        if self.scroll_mini.y < 0:
            self.scroll_mini.y = 0


