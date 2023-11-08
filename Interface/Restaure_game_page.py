from os import getcwd, listdir
from os.path import isfile,join
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
Chiffrefont = pg.font.Font(None, 36)

go_to_home_page =  pg.USEREVENT + 100
Play_sg_1 = pg.USEREVENT + 99
Play_sg_2 = pg.USEREVENT + 98
Play_sg_3 = pg.USEREVENT + 97

Emplacements = ["Emplacement 1" , "Emplacement 2" ,"Emplacement 3"]

class Save_page_button :

    def __init__(self , back_surface , text , pos , size = None , event = None ) :
        self.back = back_surface 
        self.text = text 
        self.event = event
        if size : 
            self.resize(size)
        if back_surface :
            self.pos = ( pos[0] - self.back.get_width()/2 , pos[1] - self.back.get_height()/2)
        else :
            self.pos = pos

    def draw(self, screen ) :
        
        if self.back :
            screen.blit( self.back , self.pos)
            
        if self.text : 
            text_size = Chiffrefont.size(self.text)
            if self.back : 
                decalage = ( self.back.get_width() / 2 - text_size[0]/2 ,  self.back.get_height() / 2 - text_size[1]/2 )
            else : 
                decalage = (  - text_size[0]/2 ,  - text_size[1]/2 )

            screen.blit(Chiffrefont.render(self.text , True , (255,255,255)) , (self.pos[0] + decalage[0] , self.pos[1] + decalage[1]))

            

    def resize(self ,size) :
        self.back = pg.transform.scale(self.back , size )

    def collide( self , pos ) : 
        return self.pos[0] <= pos[0] <= self.pos[0] + self.back.get_width() and self.pos[1] <= pos[1] <= self.pos[1] + self.back.get_height()

    def action( self ): 
        pos = pg.mouse.get_pos()
        if self.collide(pos) and self.event: 
            # pg.event.post(pg.event.Event(self.event))
            return self.event

class Save_page :

    def __init__( self ) :
        #printt("Je suis juste avant ")
        Fichiers_sauvegardes = [ f for f in listdir("Terminus_saves") if isfile("Terminus_saves/"+f) ]
        #printt("Fichiers sauvegarde :",Fichiers_sauvegardes)
        for i in range( 3-  len(Fichiers_sauvegardes)  ):
            Fichiers_sauvegardes.append(f"Emplacement {i+1}")

        #printt("Fichiers sauvegarde :",Fichiers_sauvegardes)
        save_1_n = "Emplacement 1"
        save_2_n = "Emplacement 2"
        save_3_n = "Emplacement 3"       
        #printtt("Fichiers sauvegarde :",Fichiers_sauvegardes)
        [save_1_n , save_2_n , save_3_n ] = Fichiers_sauvegardes
        #printt("Fichiers sauvegarde :",Fichiers_sauvegardes)
        if ".pkl" in save_1_n : 
            save_1_n= save_1_n[:-4]
            
        if ".pkl" in save_2_n : 
            save_2_n= save_2_n[:-4]

        if ".pkl" in save_3_n : 
            save_3_n= save_3_n[:-4]
        # printt("Fichiers sauvegarde :",Fichiers_sauvegardes)

        self.back = Save_page_button( pg.image.load(f"{getcwd()}/View/Sprites/Restaure_game_page/RP_back.PNG") ,None, (window_width /2 , winddow_height / 2) , (window_width , winddow_height ))
        self.support = Save_page_button( pg.image.load(f"{getcwd()}/View/Sprites/Restaure_game_page/RP_support.PNG")  ,None, (window_width /2 , winddow_height / 2) , (window_width /2 , winddow_height /2))
        self.save_1 = Save_page_button( pg.Surface( (window_width /4 , winddow_height / 8) ) ,save_1_n, (window_width /2 , winddow_height / 3) ,None , Play_sg_1)
        self.save_2 = Save_page_button( pg.Surface( (window_width /4 , winddow_height / 8)  ) ,save_2_n, (window_width /2 , winddow_height /2),None , Play_sg_2) 
        self.save_3 = Save_page_button( pg.Surface( (window_width /4 , winddow_height / 8)  ) ,save_3_n, (window_width /2 , winddow_height * 4/ 6),None , Play_sg_3)
        self.retour = Save_page_button( Chiffrefont.render("Return" , True , (255,255,255)) , "Return" , (window_width *7/10 , winddow_height *7/10) ,None,go_to_home_page)

    def draw ( self , screen ) :

        self.back.draw(screen)
        self.support.draw(screen)
        self.save_1.draw(screen)
        self.save_2.draw(screen)
        self.save_3.draw(screen)
        self.retour.draw(screen)


    def collide  ( self , pos ) :
        return self.back.collide(pos) or self.save_1.collide(pos) or self.save_2.collide(pos) or self.save_3.collide(pos) or self.retour.collide(pos)
        

    def action ( self ) : 
        event_ = None
        event_ = self.back.action()
        if event_ : return event_
        event_ = self.save_1.action()
        if event_ : return event_
        event_ = self.save_2.action()
        if event_ : return event_
        event_ = self.save_3.action()
        if event_ : return event_
        event_ = self.retour.action()
        return event_
        
