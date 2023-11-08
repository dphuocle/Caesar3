from os import getcwd
import pygame as pg
from pygame.locals import * 
import sys
from tkinter import simpledialog
import tkinter as tk 
pg.init()
Test_screen = pg.display.set_mode( ( 0 , 0 ) , pg.FULLSCREEN)
( window_width , winddow_height) = Test_screen.get_size()
Path_font = f"{getcwd()}/Interface/C3_policy.TTF"
Textefont = pg.font.Font( Path_font , 36 )
# from Data_controller import *

# SP_text_S  = pg.Surface((window_width/4 , winddow_height/8 ))
# SP_text_nom  = Textefont.render("Nom de la partie" ,True , (0,0,0))
# SP_text_R  =SP_text_nom.get_rect()
# SP_text_R.center = (window_width/2 , winddow_height/2 )
# SP_new_game_name = ""





class InputBoxName :

    def __init__( self , screen , pos , size) :
        
        self.left = pos[0] - size[0]/2
        self.up = pos[1] - size[1]/2
        self.pos = ( self.left , self.up )
        self.size = size
        self.width = size[0]
        self.height = size[1]
        self.text = 'Terminus'
        self.text_surface = Textefont.render(self.text , True , (0,0,0) , (255,255,255))
        self.rect = self.text_surface.get_rect()
        self.screen = screen
        self.back = pg.Surface( ( self.width , self.text_surface.get_size()[1] + 10 ))
        self.back.fill( (255,255,255))
        self.writing = False


    def draw( self , screen ) : 
        #Faire une surface de fond 

        screen.blit(self.back, self.pos)
        screen.blit(self.text_surface , ( self.left + 5 , self.up + 5 ))


    def ajout_char(self, event ,screen ) :
        

        if len(self.text) < 18 and self.writing :
            if ord(event.unicode) in range(ord('a'), ord('z')+1) or ord(event.unicode) in range(ord('0'), ord('9')+1) or ord(event.unicode) in range( ord('A') , ord('Z') +1 ):

                self.text += event.unicode

            elif event.unicode == " " :
                self.text += " "
            elif event.unicode == "\b" :
                self.text = self.text[:-1]

        else :
            if event.unicode == "\b" :
                self.text = self.text[:-1] 
        

        self.text_surface = Textefont.render( self.text , True , (0,0,0))
        self.draw(screen)

        

    def collide( self ,pos ) :
        tmp = self.back.get_rect()
        tmp.center = ( window_width / 2 , winddow_height / 2 )
        self.writing = tmp.collidepoint(pos)
        return self.writing






SP_input = InputBoxName(None , ( window_width/2 , winddow_height/2) , ( ( 2*window_width/7 , winddow_height/16)))
# running = True
# timer = pg.time.Clock()
# Test_screen.fill((122,122,122))
# while running :

#     timer.tick(60)
#     mouse_pos = pg.mouse.get_pos()
    
            
#     pg.display.update() 
#     pg.display.flip()

#     for event in pg.event.get() :

#         SP_input.draw(Test_screen)

#         if event.type == pg.QUIT :
#             running = False
#             pg.quit()
#             sys.exit()

#         if event.type == pg.MOUSEBUTTONDOWN :
#             SP_input.collide( mouse_pos ) 


#         if event.type == pg.KEYDOWN : 
#             SP_input.ajout_char( event , Test_screen )
            