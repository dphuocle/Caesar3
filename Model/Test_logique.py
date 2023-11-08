import pygame as pg
import pickle
import sys

sys.path.insert(0, '..')

from Model.logique import *



def reset_maps() :

    print("Restet map")
    global actual_position
    actual_position = 0 
    m.Mat_perso = []
    m.Mat_batiment = []
    m.Mat_route = []
    m.Mat_fire = []
    m.Mat_water = []
    m.Population = 0 
    m.init_matrice_terrain(m.Mat_batiment,m.nb_cases_x , m.nb_cases_y)
    m.init_matrice_route(m.Mat_route)
    Add_bat_game(20,0 , m.name_id["Panneau Entree"])
    m.init_matrice_perso(m.Mat_perso,m.nb_cases_x , m.nb_cases_y)
    m.init_mat_fire()
    m.init_mat_water()
    Add_bat_game( 21 , 0 , m.name_id["Path"])

    


def Construction_1() : 
    for i in range(1,m.nb_cases_x) :
        Add_bat_game(1,i, m.name_id["Path"])

    Add_bat_game(2 , 20 , m.name_id["Maison1"])
    Add_bat_game(2 , 25 , m.name_id["EngineersPost"])
    m.add_perso(1,1,"Engineer" , m.Mat_perso , m.Mat_batiment[2][25] , None)
    m.add_perso(1,4,"Priest" , m.Mat_perso , m.Mat_batiment[2][20] , None)


def Construction_maison_1() : 
    reset_maps()
    for i in range ( 1 , m.nb_cases_y ) :
        Add_bat_game( 21 , i , m.name_id["Path"])
        if 10 < i < 20 :
            Add_bat_game(22 , i , m.name_id["Panneau"])

def Construction_maison_2() :
    reset_maps()
    for i in range ( 1 , m.nb_cases_y ) :
        Add_bat_game( 21 , i , m.name_id["Path"])
        if 10 < i < 20 :
            Add_bat_game(22 , i , m.name_id["Panneau"])

    Add_bat_game(23 , 15 , m.name_id["Well"])

def Construction_maison_3() :
    reset_maps()
    for i in range(1, m.nb_cases_y):
        Add_bat_game(21, i, m.name_id["Path"])
        if 10 < i < 20:
            Add_bat_game(22, i, m.name_id["Maison 1"])
        if i == 8:
            Add_bat_game(22, i, m.name_id["Prefecture"])
        if i == 22:
            Add_bat_game(22, i, m.name_id["Prefecture"])
        if i == 9:
            Add_bat_game(22, i, m.name_id["EngineersPost"])



def Construction_maison_4() :
    reset_maps()
    for i in range(1, m.nb_cases_y):
        Add_bat_game(21, i, m.name_id["Path"])
        if 10 < i < 20:
            Add_bat_game(22, i, m.name_id["Maison 1"])
        if i == 8:
            Add_bat_game(22, i, m.name_id["Prefecture"])
        if i == 22:
            Add_bat_game(22, i, m.name_id["Prefecture"])
        if i == 9:
            Add_bat_game(22, i, m.name_id["EngineersPost"])
        if i == 2:
            Add_bat_game(22, i, m.name_id["Farm"])
        if i == 2:
            Add_bat_game(18, i, m.name_id["Granary"])
        if i == 24:
            Add_bat_game(22, i, m.name_id["Market"])
        if i == 21:
            Add_bat_game(22,i,m.name_id["Fountain"])




def Construction_maison_5() :
    pass

def Construction_maison_6() :
    pass

def Construction_maison_7() :
    pass


