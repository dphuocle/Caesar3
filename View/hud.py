import pygame as pg
import sys
from os import getcwd

sys.path.insert(0, '..')
from Model.logique import *


Path_font = f"{getcwd()}/Interface/C3_policy.TTF"
Textefont = pg.font.Font( Path_font , 14 )
Chiffrefont = pg.font.Font(None, 20)
Test_screen = pg.display.set_mode( ( 0 , 0 ) , pg.FULLSCREEN)
( window_width , winddow_height) = Test_screen.get_size()
action = None


class button_text_hub():

   def __init__( self  , pos , size ,text, event) :
        
        self.left = pos[0] - size[0]/2
        self.up = pos[1] - size[1]/2
        self.pos = ( self.left , self.up )
        self.size = size
        self.width = size[0]
        self.height = size[1]
        self.text = text
        self.event = event
        self.text_surface = Textefont.render(self.text , True , (0,0,0) , (255,255,255))
        self.rect = self.text_surface.get_rect()
        self.back = pg.Surface( ( self.width , self.text_surface.get_size()[1] + 10 ))
        self.back.fill( (255,255,255))



   def draw( self , screen ) : 
        #Faire une surface de fond 

        screen.blit(self.back, self.pos)
        screen.blit(self.text_surface , ( self.left + 5 , self.up + 5 ))

   def collide( self ,posi ) :
      return self.pos[0] <= posi[0] <= self.pos[0]  + self.width and self.pos[1]  <= posi[1] <= self.pos[1] + self.height

   def clicked( self ) :
      pos = pg.mouse.get_pos()
      if self.collide(pos) :
         pg.event.post(pg.event.Event(self.event))
         return self.event


class button_hud():

    def __init__(self, path, path_over, path_clicked, pos, size_button, event_number):
        self.__transparent = False
        self.__image = pg.image.load(path)
        self.__image_over = pg.image.load(path_over)
        self.__image_cliked = pg.image.load(path_clicked)
        self.__image = pg.transform.scale(self.__image, size_button)
        self.__image_over = pg.transform.scale(self.__image_over, size_button)
        self.__image_cliked = pg.transform.scale(self.__image_cliked, size_button)
        self.__left = pos[0] - self.__image.get_width() / 2
        self.__up = pos[1] - self.__image.get_height() / 2
        self.__pos = (self.__left, self.__up)
        self.__clicked = False
        self.__event = event_number

    def is_clicked(self):
        return self.__clicked

    def get_width(self):
        return self.__image.get_width()

    def get_height(self):
        return self.__image.get_height()

    def get_up(self):
        return self.__up

    def get_left(self):
        return self.__left

    def get_image(self):
        return self.__image

    def get_image_over(self):
        return self.__image_over

    def get_image_clicked(self):
        return self.__image_cliked

    def get_pos(self):
        return self.__pos

    def transparenci(self, pos, screen):

        if self.overhead(pos, screen):
            if not self.__transparent:
                self.__transparent = True
                white_rect = pg.Surface((self.get_width(), self.get_height()))
                white_rect.fill((255, 255, 255))
                white_rect.set_alpha(100)
                screen.blit(white_rect, (self.get_left(), self.get_up()))
        else:
            self.__transparent = False
            screen.blit(self.get_image(), (self.get_left(), self.get_up()))

    def overhead(self, pos):
        return self.get_left() <= pos[0] <= self.get_left() + self.get_width() and self.get_up() <= pos[
            1] <= self.get_up() + self.get_height()

    def draw(self, screen):

        if self.__clicked:
            screen.blit(self.get_image_clicked(), self.get_pos())
        else:
            if self.overhead(pg.mouse.get_pos()):
                screen.blit(self.get_image_over(), self.get_pos())
            else:
                screen.blit(self.get_image(), self.get_pos())

    def set_cliked(self):
        self.__clicked = self.overhead(pg.mouse.get_pos())
        if self.__clicked:
            pg.event.post(pg.event.Event(self.__event))
            global action
            action = self.__event
            return self.__event


class Hud:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.current_action = None

        # menu hud
        self.menu1 = pg.image.load("View/Graphique/paneling_00017.png")
        self.menu2 = pg.image.load("View/Graphique/paneling_00018.png")
        self.menu3 = pg.image.load("View/Graphique/paneling_00485.png")
        self.menu4 = pg.image.load("View/Graphique/paneling_00527.png")
        self.menu5 = pg.image.load("View/Graphique/paneling_00479.png")
        self.menu6 = pg.image.load("View/Graphique/paneling_00521.png")

        self.menu7 = pg.image.load("View/Graphique/paneling_00492.png")
        self.menu8 = pg.image.load("View/Graphique/paneling_00486.png")
        self.menu9 = pg.image.load("View/Graphique/paneling_00526.png")
        self.menu10 = pg.image.load("View/Graphique/paneling_00480.png")
        self.menu11 = pg.image.load("View/Graphique/paneling_00519.png")

        self.sous_menu = pg.image.load("View/Graphique/paneling_00020.png")


        # Menu bandeau

        self.bandeau = pg.image.load("View/Graphique/Paneling_bandeau.PNG")
        self.value = pg.image.load("View/Graphique/paneling_00015.PNG")
        self.bandeau_size = self.bandeau.get_size()


        self.dim = self.menu1.get_size()
        self.pos = (width - self.dim[0], self.bandeau_size[1])
        size_button = (9.4 / 36 * self.dim[0], 6.5 / 95 * self.dim[1])
        size_large_button = (16 / 36 * self.dim[0], 5 / 95 * self.dim[1])
        size_little_button = (1.55/8* self.dim[0], 5 / 95 * self.dim[1])
        # Menu overlay

        

        self.overlay = button_text_hub( (self.pos[0] + self.dim[0] * (14.8/38), self.pos[1] + self.dim[1] * (2.5/93)),( self.dim[0] * 3/4 ,  self.dim[1] * 3.5/93 ), "Overlay" , Nume_overlay)



        # Buttons :

        U1 = self.pos[1] + 55 / 95 * self.dim[1] + self.bandeau_size[1]
        U2 = self.pos[1] + 63 / 95 * self.dim[1] + self.bandeau_size[1]
        U3 = self.pos[1] + 70 / 95 * self.dim[1] + self.bandeau_size[1]
        U4 = self.pos[1] + 78 / 95 * self.dim[1] + self.bandeau_size[1]
        U5 = self.pos[1] +  self.dim[1]  + self.bandeau_size[1]
        U6 = self.pos[1] + 5 / 4 * self.dim[1] + self.bandeau_size[1]
        L1 = self.pos[0] + 6.9 / 32 * self.dim[0]
        L2 = self.pos[0] + 16 / 32 * self.dim[0]
        L3 = self.pos[0] + 26 / 32 * self.dim[0]



        self.maison = button_hud("View/Graphique/paneling_00123.png", "View/Graphique/paneling_00124.png",
                                 "View/Graphique/paneling_00125.png", (L1, U1), size_button, Nume_maison)
        self.eau = button_hud("View/Graphique/paneling_00127.png", "View/Graphique/paneling_00128.png",
                              "View/Graphique/paneling_00129.png", (L1, U2), size_button, Nume_eau)
        self.prefecture = button_hud("View/Graphique/paneling_00159.png", "View/Graphique/paneling_00160.png",
                                     "View/Graphique/paneling_00161.png", (L2, U4), size_button, Nume_prefecure)
        self.nourriture = button_hud("View/Graphique/paneling_00155.png", "View/Graphique/paneling_00156.png",
                                     "View/Graphique/paneling_00157.png", (L3, U4), size_button, Nume_nourriture)
        self.ingenieur = button_hud("View/Graphique/paneling_00167.png", "View/Graphique/paneling_00168.png",
                                    "View/Graphique/paneling_00169.png", (L1, U4), size_button, Nume_ingenieur)
        self.santé = button_hud("View/Graphique/paneling_00163.png", "View/Graphique/paneling_00164.png",
                                "View/Graphique/paneling_00165.png", (L2, U2), size_button, Nume_sante)
        self.route = button_hud("View/Graphique/paneling_00135.png", "View/Graphique/paneling_00136.png",
                                "View/Graphique/paneling_00137.png", (L3, U1), size_button, Nume_route)
        self.administratif = button_hud("View/Graphique/paneling_00139.png", "View/Graphique/paneling_00140.png",
                                        "View/Graphique/paneling_00141.png", (L3, U3), size_button, Nume_administratif)
        self.theatre = button_hud("View/Graphique/paneling_00143.png", "View/Graphique/paneling_00144.png",
                                  "View/Graphique/paneling_00145.png", (L2, U3), size_button, Nume_theatre)
        self.pelle = button_hud("View/Graphique/paneling_00131.png", "View/Graphique/paneling_00132.png",
                                "View/Graphique/paneling_00133.png", (L2, U1), size_button, Nume_pelle)
      
        self.fountain = button_hud("View/Graphique/Fountain.png","View/Graphique/Fountain2.png","View/Graphique/Fountain3.png",(L1,U3) , size_button , Nume_fountain)

        self.speed_up = button_hud("View/Graphique/paneling_00247.png","View/Graphique/paneling_00248.png","View/Graphique/paneling_00249.png",(L1 , U5), size_button , Nume_increase_speed)
        self.speed_down = button_hud("View/Graphique/paneling_00251.png","View/Graphique/paneling_00252.png","View/Graphique/paneling_00253.png",(L2 , U5),size_button , Nume_decrease_speed)
        self.speed_pause = button_hud("View/Graphique/paneling_00097.png","View/Graphique/paneling_00098.png","View/Graphique/paneling_00099.png", ( L3 , U5) , size_button,Nume_pause_speed)


        save_pos = (self.pos[0] + 0.88*self.dim[0] , self.pos[1] + 3.8/100 * self.dim[1])
        self.save = button_hud("View/Graphique/paneling_00239.png","View/Graphique/paneling_00240.png","View/Graphique/paneling_00241.png", save_pos , size_little_button, Nume_save)
      

    def draw(self, screen):
        # screen.blit(self.menu1, (pg.display.Info().current_w - 162, pg.display.Info().current_h - 840))
        
        screen.blit(self.menu1, self.pos)
        screen.blit(self.bandeau, (0, 0))
        screen.blit(self.sous_menu, (self.pos[0] , self.pos[1] + self.dim[1]))
        # Placer le bandeau

        coef = self.bandeau_size[1] / self.value.get_size()[1]
        for i in range(self.width // self.bandeau_size[0] + 1):
            screen.blit(self.bandeau, (i * (self.bandeau_size[0]), 0))

        self.value = pg.transform.scale(self.value, (self.value.get_size()[0] * coef, self.value.get_size()[1] * coef))
        screen.blit(self.value, (self.width / 4, 0))
        screen.blit(self.value, (self.width / 2, 0))
         

        self.pop_surface = Chiffrefont.render("Pop : " + str(m.get_Population()) , True , (255,255,255) ) 
        screen.blit(Chiffrefont.render("Pop : " + str(m.get_Population()) , True , (0,0,0) , (255,255,255)) , (self.width / 4 + self.value.get_width()/2 - self.pop_surface.get_width() /2,  self.value.get_height() /2 - self.pop_surface.get_height() / 2  ))

        U6 = self.pos[1] + 1.05 * self.dim[1]  + self.bandeau_size[1]  
         
        self.speed_surface =  Chiffrefont.render( str(get_speed_game()) + "%" , True , (0,0,0) , (255,255,255)) 
        L4 = self.pos[0] + 16/32 * self.dim[0] - self.speed_surface.get_width()/2
        screen.blit(Chiffrefont.render( str(get_speed_game()) + "%" , True , (0,0,0) , (255,255,255)) , (L4,U6) )


        # screen.blit(self.menu2, (pg.display.Info().current_w - 162, pg.display.Info().current_h - 166))

        # corner
        # screen.blit(self.menu3, (pg.display.Info().current_w - 16, pg.display.Info().current_h - 390))
        # screen.blit(self.menu4, (pg.display.Info().current_w - 16, pg.display.Info().current_h - 182))
        # screen.blit(self.menu5, (pg.display.Info().current_w - 160, pg.display.Info().current_h - 390))
        # screen.blit(self.menu6, (pg.display.Info().current_w - 160, pg.display.Info().current_h - 182))

        # for a in range(12):
        #     screen.blit(self.menu7, (pg.display.Info().current_w - 16, pg.display.Info().current_h - 374 + 16 * a))
        #     screen.blit(self.menu8, (pg.display.Info().current_w - 160, pg.display.Info().current_h - 374 + 16 * a))
        # for b in range(8):
        #    screen.blit(self.menu9, (pg.display.Info().current_w - 144 + 16 * b, pg.display.Info().current_h - 182))
        #    screen.blit(self.menu10, (pg.display.Info().current_w - 144 + 16 * b, pg.display.Info().current_h - 390))
        # for c in range(8):
        #     for d in range(12):
        #        screen.blit(self.menu11, (pg.display.Info().current_w - 144 + 16 * c, pg.display.Info().current_h - 374 + 16 * d))

        self.maison.draw(screen)
        self.eau.draw(screen)
        self.prefecture.draw(screen)
        self.nourriture.draw(screen)
        self.route.draw(screen)
        self.theatre.draw(screen)
        self.administratif.draw(screen)
        self.pelle.draw(screen)
        self.ingenieur.draw(screen)
        self.santé.draw(screen)
        self.speed_down.draw(screen)
        self.speed_up.draw(screen)
        self.speed_pause.draw(screen)
        self.overlay.draw(screen)
        self.fountain.draw(screen)
        self.save.draw(screen)



    def overhead_all( self):

         self.maison.set_cliked()
         self.eau.set_cliked()
         self.prefecture.set_cliked()
         self.nourriture.set_cliked()
         self.route.set_cliked()
         self.theatre.set_cliked()
         self.administratif.set_cliked()
         self.pelle.set_cliked()
         self.ingenieur.set_cliked()
         self.santé.set_cliked()
         self.speed_down.set_cliked()
         self.speed_up.set_cliked()
         self.speed_pause.set_cliked()
         self.fountain.set_cliked()
         self.overlay.clicked()
         self.save.set_cliked()
         
         global action 
         return action 

    def is_overhead_all( self ) :
         pos = pg.mouse.get_pos()
         return self.maison.overhead(pos) or self.eau.overhead(pos) or self.prefecture.overhead(pos) or self.nourriture.overhead(pos) or self.route.overhead(pos) \
         or self.theatre.overhead(pos) or self.administratif.overhead(pos) or self.pelle.overhead(pos) or self.ingenieur.overhead(pos) or self.santé.overhead(pos) or \
         self.speed_down.overhead(pos) or self.speed_up.overhead(pos) or self.speed_pause.overhead(pos) or self.overlay.collide(pos) or self.fountain.overhead(pos)
      
         

    def modif_speed( self ): 
      pos = pg.mouse.get_pos()
      return self.speed_down.overhead(pos) or self.speed_up.overhead(pos) or self.speed_pause.overhead(pos)
