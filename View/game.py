import sys

sys.path.insert(0, '..')
import pygame as pg
import sys
from View.map import Map
from View.settings import *
# from utils import draw_text
from View.camera import Camera
from View.hud import Hud
from Model import logique as l 
from Model import Test_logique as Test_l
from Interface.InputBoxName import SP_input
from Interface.Data_controller import set_screen_HP

list_event = {l.Nume_administratif, l.Nume_eau, l.Nume_ingenieur, l.Nume_maison, l.Nume_nourriture, l.Nume_pelle,
              l.Nume_prefecure, l.Nume_route, l.Nume_sante, l.Nume_theatre}

pos_souris_down = (0,0)

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
        self.hud = Hud(self.width, self.height)

        overlay = ""
        self.selection =[[],[]]
        self.action = None 
        self.mouse_button = [[],[],[]]
        self.playing = True

    def run(self):
        
        self.playing = True

        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

        return self.playing

        

    def events(self):

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

                if event.key == pg.K_l:
                    l.loadfile("Fichier_de_demonstration.pkl")          

                if event.key == pg.K_s:
                    l.savefile("Fichier_de_demonstration.pkl")

                if event.key == pg.K_m : 
                    l.event_to_logic(l.Nume_save , None , None , SP_input.text)
                    self.playing = False 

                if event.key == pg.K_p :
                    l.event_to_logic(l.Nume_pause_speed , None , None )

                if event.key == pg.K_F1 : 
                    Test_l.Construction_maison_1()

                if event.key == pg.K_F2 : 
                    Test_l.Construction_maison_2()

                if event.key == pg.K_F3 : 
                    Test_l.Construction_maison_3()

                if event.key == pg.K_F4 : 
                    Test_l.Construction_maison_4()

                if event.key == pg.K_F5 : 
                    Test_l.Construction_maison_5()

                if event.key == pg.K_F6 : 
                    Test_l.Construction_maison_6()

                if event.key == pg.K_F7 : 
                    Test_l.Construction_maison_7()

                
            self.mouse_button = pg.mouse.get_pressed()
            self.mouse_pos = pg.mouse.get_pos()


            if event.type == pg.MOUSEBUTTONDOWN :


                if self.hud.save.overhead(self.mouse_pos) :
                    l.event_to_logic(l.Nume_save,None,None,SP_input.text)

                elif self.hud.modif_speed() :
                    self.action = self.hud.overhead_all()
                    l.event_to_logic(self.action ,None ,None)
                    self.action = None

                elif self.hud.overlay.collide(self.mouse_pos) :
                    l.event_to_logic(l.Nume_overlay ,None,None)

                elif self.hud.is_overhead_all() and  self.mouse_button[0]:
                    self.action = self.hud.overhead_all()
                    self.selection = [[],[]]

                elif self.mouse_button[2] :
                    self.action = None
                    self.selection = [[],[]]
                    self.hud.overhead_all()

                elif self.mouse_button[0] :
                    self.selection[0] = self.mouse_to_tiles()


            if event.type == pg.MOUSEBUTTONUP :

                if self.action and self.selection[0] != []:
                    self.selection[1] = self.mouse_to_tiles()


            if self.action != None and self.selection[0] != [] and self.selection[1] != [] :
                l.event_to_logic(self.action , self.selection[0] , self.selection[1] )
                self.selection = [[],[]]

            #if event.type == pg.MOUSEMOTION and self.selection[0] != []:
            #    init_clique_pos = self.mouse_to_tiles()

    def update(self):
        Test_l.Tour_jeu()
        self.camera.update()
        self.map.create_map()
        self.map.create_walkeur()
        self.draw()

    def draw(self):
        self.screen.fill(BLACK)

        self.map.draw(self.screen, self.camera)
        self.hud.draw(self.screen)
        self.map.draw_mini(self.screen, self.camera)

        p = self.map.map[self.mouse_to_tiles()[0]][self.mouse_to_tiles()[1]]["iso_poly"]
        p = [(x + self.map.grass_tiles.get_width() / 2 + self.camera.scroll.x, y - (self.map.tiles["case"].get_height() - TILE_SIZE) + self.camera.scroll.y) for x, y in p]

        if self.action != None:
            pg.draw.polygon(self.screen, (255, 255, 255), p, 4)
        else:
            pg.draw.polygon(self.screen, (255, 205, 0), p, 2)

        self.draw_text(
            self.screen,
            str("(" + str(self.mouse_to_tiles()[0]) + "," + str(self.mouse_to_tiles()[1]) + ")"),
            15,
            (255, 205, 0),
            (p[1][0], p[1][1] + 10)
        )

        batiment = l.m.Mat_batiment[self.mouse_to_tiles()[1]][self.mouse_to_tiles()[0]]

        if batiment.id in (10, 11, 12) and batiment.name != "Herb": #MAISONS
            self.draw_text(
                self.screen,
                str('Quantité de blé : ' + str(batiment.nourriture[0][1])),
                15,
                (255, 255, 255),
                (10, 90)
            )
            self.draw_text(
                self.screen,
                str('Population : ' + str(batiment.curpop)),
                15,
                (255, 255, 255),
                (10, 105)
            )

        self.draw_text(
            self.screen,
            'fps={}'.format(round(self.clock.get_fps())),
            25,
            (255, 255, 255),
            (10, 30)
         )

        if self.map.overlay == "fire":
            self.draw_text(self.screen, 'Overlay Feu', 25, (255, 255, 255), (10, 75))

        elif self.map.overlay == "bat":
            self.draw_text(self.screen, 'Overlay Effondrement', 25, (255, 255, 255), (10, 75))

        elif self.map.overlay == "water":
            self.draw_text(self.screen, 'Overlay Eau', 25, (255, 255, 255), (10, 75))

        position_write = "(" + str(self.mouse_to_tiles()[0]) + "," + str(self.mouse_to_tiles()[1]) + ")"

        self.draw_text(self.screen, position_write, 15, (255, 255, 255), (10, 55))

        pg.display.flip()

    def mouse_to_tiles(self):
        mouse = pg.mouse.get_pos()

        on_grid_x = -self.camera.scroll.x + mouse[0] - self.map.grass_tiles.get_width() / 2
        on_grid_y = - self.camera.scroll.y + mouse[1]

        iso_y = (2 * on_grid_y - on_grid_x) / 2
        iso_x = iso_y + on_grid_x

        grid_x = int(iso_x // TILE_SIZE)
        grid_y = int(iso_y // TILE_SIZE)

        if grid_x < 0:
            grid_x = 0
        if grid_x > 39:
            grid_x = 39

        if grid_y < 0:
            grid_y = 0
        if grid_y > 39:
            grid_y = 39

        return (grid_x, grid_y)

    def draw_text(self, screen, text, size, colour, pos):

        font = pg.font.SysFont(None, size)
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect(topleft=pos)

        screen.blit(text_surface, text_rect)