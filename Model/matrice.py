import sys
import random

sys.path.insert(0, '..')
from Model import Priest as pr
from Model import Food_guy as F_G
from Model import terrain as t
from Model import maison as mais
from Model import Walker as w
from Model import water as wa
from Model import engineering as eng
from Model import security as sec
from Model import herb as h
from Model import delivery_guy as dv
from Model import administration as admin
from Model import path as pa
from Model import tree as tr
from Model import ferme as f
from Model import granary as g
from Model import warehouse as war
from Model import Immigrant as imm
from Model import ruines
from Model import market as mar
from Model import prefet as pref
from Model import engineer
from Model import temple
from copy import copy
from Model import Recruteur as rec
from Model import market as mar

# matrice de depart par defaut


matrix = [[3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
           0, 0, 0, 0],
          [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 3, 3, 3, 3, 3, 3, 3, 65, 3, 3, 3, 3,
           3, 3, 0, 0, 0],
          [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
           3, 3, 0, 0],
          [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
           3, 3, 3, 0],
          [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 0, 1, 1, 1, 1, 1, 0, 3, 3, 3, 3, 3, 0, 0, 0, 3, 3, 3,
           3, 3, 3, 3, 0],
          [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
           3, 3, 3, 0],
          [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 3, 3, 0, 3,
           3, 3, 3, 0],
          [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3, 3, 3, 3,
           3, 3, 3, 0],
          [3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3, 3,
           3, 3, 3, 3, 0],
          [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0,
           3, 3, 3, 0],
          [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
           3, 3, 3, 0],
          [3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 0, 3, 0, 0, 0, 3, 3, 3, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           3, 3, 3, 0],
          [3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1,
           1, 3, 1, 3],
          [3, 3, 3, 3, 3, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 1, 1, 1, 1,
           1, 1, 1, 1],
          [3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 1, 1,
           1, 1, 1, 1],
          [3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3,
           1, 1, 1, 1],
          [3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0,
           3, 3, 1, 1],
          [0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 3, 0, 0, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0,
           0, 0, 0, 3],
          [0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3,
           3, 3, 3, 3],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0],
          [115, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 116, 0],
          [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
           5, 5, 5, 5],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0],
          [0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
           3, 0, 0, 3],
          [1, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
           3, 3, 3, 3],
          [1, 1, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
           0, 3, 0, 3, 3],
          [1, 1, 1, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
           3, 0, 3, 3],
          [1, 1, 1, 1, 1, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
           3, 3, 3, 3, 3],
          [0, 1, 1, 1, 1, 0, 0, 3, 3, 3, 3, 0, 0, 0, 2, 0, 0, 2, 2, 3, 2, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3,
           3, 3, 3, 3],
          [3, 0, 1, 1, 1, 1, 1, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 2, 2, 0, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3,
           3, 3, 3, 3, 3],
          [3, 3, 3, 1, 1, 1, 1, 0, 0, 3, 0, 0, 2, 2, 0, 0, 0, 3, 3, 0, 0, 0, 2, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0,
           3, 3, 3, 3],
          [0, 3, 3, 1, 1, 1, 1, 1, 3, 0, 0, 0, 0, 2, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 2, 3, 0, 0, 3, 3, 0, 3, 3, 3, 3,
           3, 3, 3, 3, 3],
          [3, 3, 3, 3, 1, 1, 1, 1, 1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 0, 3, 0, 0, 0, 2, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3,
           3, 3, 3, 3],
          [3, 3, 3, 3, 0, 1, 1, 1, 1, 1, 2, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 3, 0, 0, 0, 2, 2, 0, 0, 0, 0, 3, 3, 3, 3,
           3, 0, 0, 3, 3],
          [3, 3, 3, 3, 0, 1, 1, 1, 1, 1, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 3],
          [3, 3, 0, 0, 0, 2, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0],
          [3, 0, 2, 0, 0, 0, 2, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 0, 3, 3, 2, 0, 0, 2, 2, 0, 2, 0, 0, 2, 0,
           0, 0, 2, 2],
          [0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0,
           0, 0, 0, 0],
          [0, 0, 0, 2, 0, 0, 2, 2, 0, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 2, 0, 2, 0,
           0, 0, 2, 2],
          [0, 0, 0, 0, 2, 2, 2, 0, 0, 1, 1, 1, 1, 1, 0, 3, 3, 0, 3, 3, 3, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 2, 2, 2, 0,
           0, 0, 2, 2]
          ]

nb_cases_x = 40
nb_cases_y = 40
nb_cases = 40

# liste servant a retenir l'ensemble des batiments servant a stocker des marchandises
Liste_stock = []

def SearchforSpace(type_march):
    if type_march == 'ble' or type_march == 'viande' or type_march == 'fruits':
        for i in range(len(Liste_stock)):
            if type(Liste_stock[i]) is g.Granary and not Liste_stock[i].isFull():
                return Liste_stock[i]
            i = 0
            for i in range(len(Liste_stock)):
                if not Liste_stock[i].isFull():
                    return Liste_stock[i]
    else:
        i = 0
        for i in range(len(Liste_stock)):
            if type(Liste_stock[i]) is war.Warehouse and not Liste_stock[i].isFull():
                return Liste_stock[i]
        i = 0
        for i in range(len(Liste_stock)):
            if not Liste_stock[i].isFull():
                return Liste_stock[i]
    return None


def SearchforFood():
    for i in range(len(Liste_stock)):
        if Liste_stock[i].hasFood:
            return Liste_stock[i]


# creer une matrice de taille passée en argument. (n'est pas utilisable en jeu)
def init_matrice_terrain(Mat, x, y):
    assert (Mat == [])
    for j in range(y):
        Mat.append([])
        for i in range(x):
            Mat[j].append(h.Herb(i, j))


# la fonction initialise le tableau des walker
# Mat [j][i] est un tableau avec la liste des personnages, si y en a aucun c'est le type walker par défaut. (parce qu'on a besoin de l'attribut name)
# en jeu on utilisera Mat_perso
def init_matrice_perso(Mat, x, y):
    assert (Mat == [])
    for j in range(y):
        Mat.append([])
        for i in range(x):
            Mat[j].append([])
            Mat[j][i].append([])
            Mat[j][i][0] = w.NoWalker()


# Créer une matrice route utile pour les déplacement des walkers 
def init_matrice_route(Mat_route, cases_x=nb_cases_x, cases_y=nb_cases_y):
    assert Mat_route == []
    for i in range(cases_x):
        Mat_route.append([])
        for j in range(cases_y):
            Mat_route[i].append([])
            Mat_route[i][j] = 0


################ a garder #############################

Mat_batiment = []
Mat_perso = []
Mat_route = []
unemployed = 0  # Le nombre de chômeurs
Nb_immigrant = 20  # Le nombre de migrants
Mat_fire = []
Mat_water = []
Population = 0 
init_matrice_terrain(Mat_batiment, nb_cases_x, nb_cases_y)
init_matrice_perso(Mat_perso, nb_cases_x, nb_cases_y)
init_matrice_route(Mat_route, nb_cases_x, nb_cases_y)


def init_mat_fire():  # matrice de booleen determinant l'emplacement de zones en feu
    assert Mat_fire == []
    for j in range(nb_cases_y):
        Mat_fire.append([])
        for i in range(nb_cases_x):
            Mat_fire[j].append([])
            Mat_fire[j][i] = 0


init_mat_fire()


def init_mat_water():
    global Mat_water
    assert Mat_water == []
    for j in range(nb_cases_y):
        Mat_water.append([])
        for i in range(nb_cases_x):
            Mat_water[j].append([])
            Mat_water[j][i] = 0


init_mat_water()


############################################

def update_water_map(x, y, r):
    global Mat_water
    for xi in range(x - r, x + r +1):
        for yi in range(y - r, y + r +1):
            if 0 <= xi <= nb_cases_x - 1 and 0 <= yi <= nb_cases_y - 1:
                Mat_water[xi][yi] = 1


def restructure_water_map():
    global Mat_water
    Mat_water = []
    init_mat_water()
    for xi in range(nb_cases_x):
        for yi in range(nb_cases_y):
            if Mat_batiment[yi][xi].name == "Well":
                update_water_map(xi, yi, 3)
            if Mat_batiment[yi][xi].name == "Fountain":
                update_water_map(xi, yi, 6)
            if Mat_batiment[yi][xi].name == "Reservoir":
                update_water_map(xi, yi, 9)


# Actualise la matrice de route
def actualiser_matrice_route():
    for i in range(nb_cases_x):
        for j in range(nb_cases_y):
            Mat_route[i][j] = isPath(i, j, Mat_batiment)


# test utiliser pour afficher la matrice des batiments ( utilise le nom )
def afficher_matrice_bat(Mat, x, y):
    for j in range(y):
        print("[", end='')
        for i in range(x):
            print(Mat[j][i].name, " ", end='')
        print("]")


# test utiliser pour afficher la matrice des personnage (utilise le type) (walker revient a ce qu'il n'y aie aucun perso dans la case)
def afficher_matrice_perso(Mat, x, y):
    for j in range(y):
        print("[", end='')
        for i in range(x):
            n = len(Mat[j][i])
            for k in range(n):
                print(Mat[j][i][k].name, " ", end='')
                if n > 1 and k != n - 1:
                    print("; ", end='')
            if i != x - 1:
                print("| ", end='')
        print("]")


# Regarde s'il y a des immigrants et les attributs aux batiments qui en ont besoins

# Ajouter tous les immigrants possible dans les batiments 


# Sortie des walker

def sortir_walker():
    for i in range(nb_cases_x):
        for j in range(nb_cases_y):
            pass
            # print(j,i)
            # if Mat_batiment[j][i].name not in  ["Herb" , "Path"] and Mat_batiment[j][i].walker_in and random.random()%2:
            #     print("Je sors le walker de la maison ",j," ",i)


# Afficher la carte de la route :


def afficher_mat_route(taille):
    for i in range(taille):
        print("[ ", end='')
        for j in range(taille):
            print(Mat_route[i][j], " ", end="")
        print("]")


# dictionnaire reliant l'id des batiments a la taille qu'ils occupent
id_size = {0: 1, 92: 1, 90: 3, 91: 1, 8: 1, 81: 1, 55: 1, 5: 1, 84: 2, 71: 3, 72: 3, 100: 3, 101: 3, 103: 3, 109: 2,
           111: 2, 114: 2, 1: 1, 2: 1, 3: 3, 115: 1, 116: 1, 7: 1, 10: 1, 70: 2}

# dictionnaire reliant le nom des batiments avec leur id
name_id = {"Well": 92, "Reservoir": 90, "Fountain": 91, "Aquaduct": 8, "EngineersPost": 81, "Prefecture": 55, "Path": 5,
           "Forum1": 84, "Water": 1, "Rock": 2, "Tree": 3, "Senate1": 4, "Maison 1": 10, "Maison 2": 11, "Maison 3": 12,
           "Forum1": 84, "Water": 1, "Rock": 2, "Tree": 3, "Senate1": 4, "Maison 1": 10, "Maison 2": 11, "Maison 3": 12,
           "Maison4": 13, "Farm": 100, "Granary": 71, "Warehouse": 71, "Herb": 0, "Panneau": 7, "Panneau Entree": 115,
           "Panneau Sortie": 116, "Market" : 70}


# permet de inserer un batiment dans la matrice sur toute la taille qu'il occupe (non utilisable en jeu)
def put_bat_mat(x, y, bat, Mat):
    for i in range(0, bat.nbr_cases):
        for j in range(0, bat.nbr_cases):
            Mat[y + j][x + i] = bat


# ajoute un batiment a une position specifiee en fonction de l'id
# on utilise Mat_batiment
# si le batiment est de type stockage, l'ajoute a la liste des batiments de stockage
def add_bat(x, y, id_bat, Mat=Mat_batiment):
    if id_bat == 7:
        Mat[y][x] = mais.Panneau(x, y)
    if id_bat == 92:
        well = wa.Well(x, y)
        Mat[y][x] = well
        update_water_map(x, y, 3)
    elif id_bat == 90:
        Reservoir = wa.Reservoir(x, y)
        update_water_map(x, y, 10)
        put_bat_mat(x, y, Reservoir, Mat)
    elif id_bat == 91:
        Fountain = wa.Fountain(x, y)
        Mat[y][x] = Fountain
        update_water_map(x, y, 6)
    elif id_bat == 8:
        Aquaduct = wa.Aquaduct(x, y)
        Mat[y][x] = Aquaduct
    elif id_bat == 81:
        EngineersPost = eng.EngineersPost(x, y)
        Mat[y][x] = EngineersPost
    elif id_bat == 55:
        Prefecture = sec.Prefecture(x, y)
        Mat[y][x] = Prefecture
    elif id_bat == 5:
        Route = pa.Path(x, y)
        Mat[y][x] = Route
        Mat_route[y][x] = 1
    elif id_bat == 84:
        Forum = admin.Forum1(x, y)
        put_bat_mat(x, y, Forum, Mat)
    elif id_bat == 1:
        Mat[y][x] = t.Water(x, y)
    elif id_bat == 2:
        Mat[y][x] = t.Rock(x, y)
    elif id_bat == 3:
        Mat[y][x] = tr.tree(x, y)
    elif id_bat == 4:
        Senate = admin.Senate1(x, y)
        put_bat_mat(x, y, Senate, Mat)
    elif id_bat == 10:
        Maison_1 = mais.Maison_1(x, y)
        put_bat_mat(x, y, Maison_1, Mat)
    elif id_bat == 11:
        Maison_2 = mais.Maison_2(x, y)
        put_bat_mat(x, y, Maison_2, Mat)
    elif id_bat == 12:
        Maison_3 = mais.Maison_3(x, y)
        put_bat_mat(x, y, Maison_3, Mat)
    elif id_bat == 13:
        Maison_4 = mais.Maison_4(x, y)
        put_bat_mat(x, y, Maison_4, Mat)
    elif id_bat == 100:
        Ferme = f.Ferme(x, y)
        put_bat_mat(x, y, Ferme, Mat)
    elif id_bat == 71:
        Granary = g.Granary(x, y)
        put_bat_mat(x, y, Granary, Mat)
        Liste_stock.append(Granary)
    elif id_bat == 72:
        Warehouse = war.Warehouse(x, y)
        put_bat_mat(x, y, Warehouse, Mat)
        Liste_stock.append(Warehouse)
    elif id_bat == 115:
        global Panneau_entree
        Panneau_entree = t.Enter_Pannel(x, y)
        Mat[y][x] = Panneau_entree
    elif id_bat == 116:
        Mat[y][x] = t.Exit_Pannel(x, y)
    elif id_bat == 0:
        Herb = h.Herb(x, y)
        Mat[y][x] = Herb
    elif id_bat== 70:
        Market = mar.Market(x, y)
        put_bat_mat(x, y, Market, Mat)



# globals()["Prefecture"+x+y] # truc interessant dont on se sert pas, à conserver pour plus tard

# ajoute un walker a une matrice donnnee en argument (on utilisera Mat_perso)
def add_perso_mat(Mat, perso, x, y):
    if Mat[y][x][0].name == "no Walker":
        Mat[y][x][0] = perso

    else:
        #print("test4")
        Mat[y][x].append(perso)


# cree un personnage de type specifié par un string
def add_perso(x, y, type_, Mat, Bat, Bat_cible, type_bouffe='ble', dest_x=-1, dest_y: object = -1, role=None) -> object:
    if type_ == 'Delivery Guy':
        DV = dv.Delivery_Guy(x, y, Bat, Bat_cible, type_bouffe)
        add_perso_mat(Mat, DV, x, y)
        Bat.Walk.append(DV)
        return DV
    elif type_ == "Food_Guy":
        FG = F_G.Food_Guy(x, y, Bat, role, Bat_cible)
        add_perso_mat(Mat, FG, x, y)
        Bat.Walk.append(FG)
        return FG
    elif type_ == "Engineer":
        EN = engineer.Engineer(x, y, Bat)
        add_perso_mat(Mat, EN, x, y)
        Bat.Walk.append(EN)
        return EN
    elif type_ == "Immigrant":
        IM = imm.Immigrant(x, y, Bat_cible)
        add_perso_mat(Mat_perso, IM, x, y)
        route_cible = SearchforRoad(Bat_cible.pos_x, Bat_cible.pos_y)
        (IM.dest_x, IM.dest_y) = route_cible
        Bat_cible.Walk.append(IM)
        return IM
    elif type_ == "Prefect":
        P = pref.Prefect(x, y, Bat)
        add_perso_mat(Mat, P, x, y)
        Bat.Walk.append(P)
        return P
    elif type_ == "Priest":
        Pr = pr.Priest(x, y, Bat)
        add_perso_mat(Mat, Pr, x, y)
        Bat.Walk.append(Pr)
        return Pr
    elif type_ == "Recruteur":
        #print("recruteur")
        Re = rec.Recruteur(x, y, Bat)
        add_perso_mat(Mat, Re, x, y)
        Bat.Walk.append(Re)
    else:
        print("unknown type, can't add perso :notlikethis:")


def invoke_walker(bat, type_, objectif=None):
    if bat.curEmployees >= 1 or type_ == "Recruteur":
        (x, y) = SearchforRoad(bat.pos_x, bat.pos_y, Mat_batiment)
        if x != -1:
            #print("test invoke:", x, y)
            #print("test batiment:", bat.pos_x, bat.pos_y)
            add_perso(x, y, type_, Mat_perso, bat, objectif)


def invoke_migrant(maison_cible):
    (x, y) = SearchforRoad(Panneau_entree.pos_x, Panneau_entree.pos_y, Mat_batiment)
    #print("coord:", x, y)
    if  x != 1 and y != -1 :
        global Population
        Population += 1 
        add_perso(x, y, "Immigrant", Mat_perso, Panneau_entree, maison_cible)


# charge la matrice de départ par défaut dans la matrice donnée en argument
def departureMatrice(Mat):
    map_depart = matrix
    for i in range(0, nb_cases_x):
        for j in range(0, nb_cases_y):
            if map_depart[j][i]:
                add_bat(j, i, map_depart[j][i], Mat)
    
    add_bat(20,0,name_id["Panneau Entree"])
    afficher_matrice_bat(Mat, nb_cases_x, nb_cases_y)


# teste si l'emplacement x,y d'une matrice correspond a un chemin
def isPath(x, y, Mat=Mat_batiment):
    return Mat[y][x].name == 'Path'


# SearchforRoad renvoie la position de la première route rencontrée autour (distance de 1) d'un batiment situé en x,y
def SearchforRoade(x, y, Mat=Mat_batiment):
    n = Mat[y][x].nbr_cases
    x1 = x
    y1 = y
    k = 0
    w = 0
    if x != 0:
        x1 = x - 1
        k = 1
    if y != 0:
        y1 = y - 1
        w = 1

    if x >= nb_cases_x - 1:
        k = -1

    if y >= nb_cases_y - 1:
        w = -1

    for i in range(n + k):
        if isPath(x1, y1, Mat):
            return x1, y1
        x1 = x1 + 1

    for j in range(n + w):
        if isPath(x1, y1, Mat):
            return x1, y1
        y1 = y1 + 1
    for i in range(0, n + k):
        if isPath(x1, y1, Mat):
            return x1, y1
        x1 = x1 - 1
    for j in range(n + w):
        if isPath(x1, y1, Mat):
            return x1, y1
        y1 = y1 - 1
    return -1, -1

def SearchforRoad(x, y, Mat=Mat_batiment):
    n = Mat_batiment[y][x].nbr_cases

    for xi in range( x-1 , x + n + 1) :
        for yi in range( y-1 , y + n + 1 ) :
            if  0 <= xi <= nb_cases_x -1 and 0 <= yi <= nb_cases_y -1  : 
                if xi in [x-1 , x+n ] or yi in [ y-1 , y+n ] :
                    if isPath(xi,yi) :
                        return xi,yi

    return -1 , -1

# cherche si une valeur est déjà presente dans un tableau
def InTable(x, tab):
    bool_ = 0
    for i in range(len(tab)):
        if x == tab[i]:
            bool_ = 1
    return bool_


def min_tab_tab_notnull(tab):  # take a tab of tab and return the tab in the tab of tab, with the smallest size
    n = len(tab)
    min_ = tab[0]
    for i in range(n):
        if len(min_) > len(tab[i]):
            min_ = tab[i]
    return min_


# fonction de pathfinding
def next_case(x, y, tab_path, dest_x, dest_y, Mat):
    assert (isPath(x, y, Mat)) 
    if x == dest_x and y == dest_y:
        return tab_path
    else:
        tab1 = []
        tab2 = []
        tab3 = []
        tab4 = []
        test = 0

        if x < nb_cases_x - 1:

            if isPath(x + 1, y, Mat) and not InTable((x + 1, y), tab_path):
                test = 1
                tab1 = copy(tab_path)
                tab1.append((x + 1, y))
                tab1 = next_case(x + 1, y, tab1, dest_x, dest_y, Mat)

        if 0 < x:
            if isPath(x - 1, y, Mat) and not InTable((x - 1, y), tab_path):
                test = 1
                tab3 = copy(tab_path)
                tab3.append((x - 1, y))
                tab3 = next_case(x - 1, y, tab3, dest_x, dest_y, Mat)

        if y < nb_cases_y - 1:

            if isPath(x, y + 1, Mat) and not InTable((x, y + 1), tab_path):
                test = 1
                tab2 = copy(tab_path)
                tab2.append((x, y + 1))
                tab2 = next_case(x, y + 1, tab2, dest_x, dest_y, Mat)

        if 0 < y:

            if isPath(x, y - 1, Mat) and not InTable((x, y - 1), tab_path):
                test = 1
                tab4 = copy(tab_path)
                tab4.append((x, y - 1))
                tab4 = next_case(x, y - 1, tab4, dest_x, dest_y, Mat)

        if test == 0:
            return []
        tab = []
        if tab1 != []:
            tab.append(tab1)
        if tab2 != []:
            tab.append(tab2)
        if tab3 != []:
            tab.append(tab3)
        if tab4 != []:
            tab.append(tab4)
        final_tab = []
        if tab != []:
            final_tab = min_tab_tab_notnull(tab)
        return final_tab


# supprime un batiment d'une matrice, à l'aide de ses coordonées
def suppr_Batiment(x, y, Mat):

    if Mat[y][x].name in ["Maison 1","Panneau","Maison 2","Maison 3"] :
        global Population
        Population -= Mat[y][x].curpop

    if not InTable(Mat[y][x].name, ["Herb",  "Rock", "Enter_Pannel", "Exit_Pannel", "Water"]):
        genocide(Mat[y][x])
        if Mat[y][x].name == "Path":
            for e in range(len(Mat_perso[y][x])):
                kill_walker(Mat_perso[y][x][0])
        # for i in range(0, Mat[y][x].nbr_cases):
        #     for j in range(0, Mat[y][x].nbr_cases):
        for i in range(Mat[y][x].nbr_cases -1 , -1, -1):
            for j in range(Mat[y][x].nbr_cases -1 , -1, -1):
                if y+j <= 39 and x+i <= 39 and Mat[y][x].name != "Herb":
                    Mat[Mat[y][x].pos_y + j][Mat[y][x].pos_x + i] = h.Herb(Mat[y][x].pos_x + i, Mat[y][x].pos_y + j)
                    Mat_fire[y + j][x + i] = 0

    restructure_water_map()


# deplacement normal: aller tout de droit puis faire demi tour apres une certaine distance
# doit prendre une direction au pif a un croisement
# renvoie le prochain x et le prochain y
def Deplacement_basique(x, y, Mat=Mat_perso, no_walker=0):
    #print(Mat_perso[y][x][no_walker].ttl, x, y)
    if Mat_perso[y][x][no_walker].ttl <= 0 and (
    Mat_perso[y][x][no_walker].dest_x, Mat_perso[y][x][no_walker].dest_y) == (-1, -1):
        kill_walker(Mat_perso[y][x][no_walker])
        return (666, 666)

    tab_possibles_chemins = []
    if x < nb_cases_x - 1:
        if Mat_route[y][x + 1] and (Mat_perso[y][x][no_walker].prev_x, Mat_perso[y][x][no_walker].prev_y) != (x + 1, y):
            tab_possibles_chemins.append((x + 1, y))
    if x > 0:
        if Mat_route[y][x - 1] and (Mat_perso[y][x][no_walker].prev_x, Mat_perso[y][x][no_walker].prev_y) != (x - 1, y):
            tab_possibles_chemins.append((x - 1, y))
    if y < nb_cases_y - 1:
        if Mat_route[y + 1][x] and (Mat_perso[y][x][no_walker].prev_x, Mat_perso[y][x][no_walker].prev_y) != (x, y + 1):
            tab_possibles_chemins.append((x, y + 1))
    if y > 0:
        if Mat_route[y - 1][x] and (Mat_perso[y][x][no_walker].prev_x, Mat_perso[y][x][no_walker].prev_y) != (x, y - 1):
            tab_possibles_chemins.append((x, y - 1))
    if len(tab_possibles_chemins) > 0:
        Mat_perso[y][x][no_walker].ttl -= 1
        return tab_possibles_chemins[random.randrange(0, len(tab_possibles_chemins))]  # Aléatoire
    else:
        Mat_perso[y][x][no_walker].ttl -= -1
        #print("demis tours : ", x,y ,Mat_perso[y][x][no_walker].prev_x, Mat_perso[y][x][no_walker].prev_y)
        return (Mat_perso[y][x][no_walker].prev_x, Mat_perso[y][x][no_walker].prev_y)


# verifie que la distance entre deux cases est de 1 (y compris en diagonale)
def dist(x1, y1, x2, y2):
    return ((x1 == x2 and (abs(y1 - y2) == 1)) or (y1 == y2 and (abs(x1 - x2) == 1)) or (
            (x2 - x1) ** 2 + (y2 - y1) ** 2 == 2))


# procede a un echange d'un walker de type delivery guy passé en parametre, ssi il se trouve a proximite de son batiment cible
def echange(DV):
    #print("echange")
    #print("dechargement:", DV.cargaison_nourriture)
    if DV.type_marchandise == 'ble':
        #print("ble")
        DV.bat_destination.get_delivery(DV.dechargement('ble'))
    elif DV.type_marchandise == 'fruits':
        DV.bat_destination.get_delivery(DV.dechargement('fruits'))
    elif DV.type_marchandise == 'viande':
        DV.bat_destination.get_delivery(DV.dechargement('viande'))
    elif DV.type_marchandise == 'olives':
        DV.bat_destination.get_delivery(DV.dechargement('olives'))
    elif DV.type_marchandise == 'argile':
        DV.bat_destination.get_delivery(DV.dechargement('argile'))
    #print("La quantité de blé est", DV.bat_destination.nourriture[0][1])

def collecte(fg: F_G.Food_Guy):
    fg.cargaison_nourriture[0][1] += fg.bat_destination.nourriture[0][1]
    fg.bat_destination.nourriture[0][1]=0
    fg.cargaison_nourriture[1][1] += fg.bat_destination.nourriture[1][1]
    fg.bat_destination.nourriture[1][1]=0
    fg.cargaison_nourriture[2][1] += fg.bat_destination.nourriture[2][1]
    fg.bat_destination.nourriture[2][1]=0

def livraison(fg: F_G.Food_Guy):
    fg.bat_destination.nourriture[0][1] += fg.cargaison_nourriture[0][1]
    fg.cargaison_nourriture[0][1] = 0
    fg.bat_destination.nourriture[0][1] += fg.cargaison_nourriture[1][1]
    fg.cargaison_nourriture[1][1] = 0
    fg.bat_destination.nourriture[0][1] += fg.cargaison_nourriture[2][1]
    fg.cargaison_nourriture[2][1] = 0

# deplace l'ensemble des walker
# possibilité de l'implémenter avec de la mise en parralèle
# si un walker arrive a destination procede a un echange
# pas terminé: il faut que on puisse echanger dès qu'on est a proximité et que le path soit remis a jours
# un walker arrive a destination doit soit mourir soit revenir a son batiment d'origine
# il faut implémenter des "missions" pour les walkers: definir le type de marchandise a acheminer, parce que echange marche juste avec ble pour l'instant
def deplacement_perso(Mat, tx=nb_cases, ty=nb_cases):
    for i in range(tx):
        for j in range(ty):
            if Mat[j][i][0].name != "no Walker":  # Pour toute cases, si on a un walker
                count = 0  # count correspond au nombre de walker sur la case
                for k in range(len(Mat[j][i])):
                    if Mat[j][i][count].has_moved == 1:
                        count = count + 1
                    else:
                        Mat[j][i][
                            count].has_moved = 1  # si le walker a déjà bougé, vaut 1 sinon 0 (chaque walker ne se déplace qu'une fois)
                        if Mat[j][i][count].dest_x != -1 and Mat[j][i][
                            count].dest_y != -1:  # si a un objectif, utilise un deplacement calcule, autrement, deplacement aleatoire
                            if Mat[j][i][count].tab_path == []:
                                new_path = next_case(i, j, [(i, j)], Mat[j][i][count].dest_x, Mat[j][i][count].dest_y,
                                                     Mat_batiment)
                                
                                if new_path == []:
                                    new_path.append((i, j))

                                Mat[j][i][count].tab_path = new_path
                            Mat[j][i][count].tab_path.pop(0)
                            if len(Mat[j][i][count].tab_path) != 0:
                                (nx, ny) = Mat[j][i][count].tab_path[0]
                                Mat[j][i][count].nx = nx
                                Mat[j][i][count].ny = ny
                            else:
                                # print(i, j, count)
                                nx = i
                                ny = j
                                if Mat_perso[j][i][count].name == "Immigrant":
                                    pass
                        else:
                            #print("cas basique", i, j)
                            #print(Mat[j][i][count].name)
                            (nx, ny) = Deplacement_basique(i, j, no_walker=count)
                            #print((nx, ny))
                            if nx == 666 and ny == 666:
                                count -= 1
                                nx = i
                                ny = j

                        if nx == i and ny == j:  # reste immobile
                            count = count + 1
                        else:  # change de case
                            if not isPath(nx, ny, Mat_batiment):
                                new_path = next_case(i, j, [(i, j)], Mat[j][i][count].dest_x, Mat[j][i][count].dest_y,
                                                     Mat_batiment)
                                Mat[j][i][count].tab_path = new_path
                                count = count + 1
                            else:
                                walk = Mat[j][i][count]
                                #print("test deplacement", walk.name)

                                Mat[j][i].pop(count)
                                if len(Mat[j][i]) == 0:
                                    Mat[j][i].append(w.NoWalker())
                                walk.x = nx
                                walk.y = ny
                                walk.prev_x = i
                                walk.prev_y = j
                                add_perso_mat(Mat, walk, nx, ny)
    for i in range(tx):
        for j in range(ty):
            if Mat[j][i][0].name != "no Walker":
                for k in range(len(Mat[j][i])):
                    Mat[j][i][k].has_moved = 0  # le walker est prêt a bouger au prochain appel de la fonction


def kill_walker(killed):  # gnéhéhé
    #print("gnehehehe")

    if killed.name != "no Walker":
        if killed.name == 'Recruteur':
            killed.batiment.hasRecruteur = 0
        for e in killed.batiment.Walk:
            if e == killed:
                killed.batiment.Walk.remove(e)
        if Mat_perso[killed.y][killed.x][0] == killed:
            if len(Mat_perso[killed.y][killed.x]) < 2:
                Mat_perso[killed.y][killed.x].pop()
                Mat_perso[killed.y][killed.x].append(w.NoWalker())
            else:
                Mat_perso[killed.y][killed.x].pop(0)
        else:
            n = 0
            for e in Mat_perso[killed.y][killed.x]:
                if e == killed:
                    Mat_perso[killed.y][killed.x].pop(n)
                n += 1


def get_Population() : 
    global Population
    return Population

def genocide(bat):  # plus efficace à la destruction d'un batiment + len
    for e in bat.Walk:
        if Mat_perso[e.y][e.x][0] == e:
            if len(Mat_perso[e.y][e.x]) < 2:
                Mat_perso[e.y][e.x].pop()
                Mat_perso[e.y][e.x].append(w.NoWalker())
        
            else:
                Mat_perso[e.y][e.x].pop(0)
        else:
            n = 0
            for h in Mat_perso[e.y][e.x]:
                if h == e:
                    Mat_perso[e.y][e.x].pop(n)
                n += 1


# place des ruines a l'emplacement couvert par le batiment
def destroy_Bat(Bat):
    genocide(Bat)
    if InTable(Bat, Liste_stock) and (Bat.name == "Granary" or Bat.name == "Warehouse"):
        Liste_stock.remove(Bat)
    #print("Destruction bat :",Bat.pos_x,Bat.pos_y)

    if Bat.name in ["Maison 1","Panneau","Maison 2","Maison 3"] :
        #print("Population descends destroy")
        global Population
        Population -= Bat.curpop
    for i in range(Bat.nbr_cases):
        for j in range(Bat.nbr_cases):
            
            Mat_batiment[j+Bat.pos_y][i+Bat.pos_x] = ruines.Ruin(i+Bat.pos_x, j+Bat.pos_y)
    restructure_water_map()

# la matrice de boolen considère qu'il y a du feu en (x,y)
def set_fire(x, y):
    Mat_fire[x][y] = 1


# place du feu sur l'ensemble d'un batiment (non terminé, il faut que le batiment cesse de fonctionner)
def fire_bat(Bat):
    if InTable(Bat, Liste_stock) and (Bat.name == "Granary" or Bat.name == "Warehouse"):
        Liste_stock.remove(Bat)
    #print("Une maison brule",Bat.pos_x,Bat.pos_y)
    for i in range(Bat.nbr_cases):
        for j in range(Bat.nbr_cases):  
            set_fire(Bat.pos_y, Bat.pos_x)
    genocide(Bat)


# verification de l'indice de feu, et d'effondrement
def check_fire_eff():
    n = 0
    for i in range(nb_cases):
        for j in range(nb_cases):
            if not InTable(Mat_batiment[j][i].name,
                           ["Herb", "Tree", "Rock", "Enter_Pannel", "Exit_Pannel", "Water", "Panneau"]) and \
                    Mat_batiment[j][i].hasCheck == 0:
                Mat_batiment[j][i].hasCheck = 1
                if (Mat_batiment[j][i].name != "Herb" and Mat_batiment[j][i].name != "Tree" and Mat_batiment[j][
                    i].name != "Path" and Mat_batiment[j][i].name != "Ruin"):
                    n = Mat_batiment[j][i].augm_att()
                    if n == -2:
                        destroy_Bat(Mat_batiment[j][i])
                    if n == -1:
                        fire_bat(Mat_batiment[j][i])
    for i in range(nb_cases):
        for j in range(nb_cases):
            Mat_batiment[j][i].hasCheck = 0


# renvoie un tableau avec les batiments proches d'une case dans un certain rayon, les terrains ne comptent pas et les chemins non plus
def get_bat_prox(x, y, r):
    tab = []
    for i in range(r):
        for j in range(r):

            if (y + j <= nb_cases_y - 1 and x + i <= nb_cases_x - 1 and not InTable(Mat_batiment[y + j][x + i].name,
                                                                                    ["Herb", "Tree", "Rock",
                                                                                     "Enter_Pannel", "Exit_Pannel",
                                                                                     "Water", "Path"]) and not InTable(
                Mat_batiment[y + j][x + i], tab)):
                tab.append(Mat_batiment[y + j][x + i])

            if (x + i <= nb_cases_x - 1 and y - j >= 0 and not InTable(Mat_batiment[y - j][x + i].name,
                                                                       ["Herb", "Tree", "Rock", "Enter_Pannel",
                                                                        "Exit_Pannel", "Water",
                                                                        "Path"]) and not InTable(
                Mat_batiment[y - j][x + i], tab)):
                tab.append(Mat_batiment[y - j][x + i])

            if (y - j >= 0 and x - i >= 0 and not InTable(Mat_batiment[y - j][x - i].name,
                                                          ["Herb", "Tree", "Rock", "Enter_Pannel", "Exit_Pannel",
                                                           "Water", "Path"]) and not InTable(Mat_batiment[y - j][x - i],
                                                                                             tab)):
                tab.append(Mat_batiment[y - j][x - i])

            if (y + j <= nb_cases_y - 1 and x - i >= 0 and not InTable(Mat_batiment[y + j][x - i].name,
                                                                       ["Herb", "Tree", "Rock", "Enter_Pannel",
                                                                        "Exit_Pannel", "Water",
                                                                        "Path"]) and not InTable(
                Mat_batiment[y + j][x - i], tab)):
                tab.append(Mat_batiment[y + j][x - i])
    return tab


def giveFood(fg: F_G.Food_Guy, house: mais.Maison):
    #print("HERE THE FOOD")
    #print(fg.cargaison_nourriture)
    if fg.cargaison_nourriture[0][1] > 0:
        chargement = ["ble", 10]
        fg.cargaison_nourriture[0][1] -= 10
        house.get_delivery(chargement)
        #print("bouffe de la maison:", house.nourriture)
    if fg.cargaison_nourriture[1][1] > 0:
        chargement = ["fruits", 10]
        fg.cargaison_nourriture[1][1] -= 10
        house.get_delivery(chargement)
    if fg.cargaison_nourriture[2][1] > 0:
        chargement = ["viande", 10]
        fg.cargaison_nourriture[2][1] -= 10
        house.get_delivery(chargement)
    #print("test billy")

def getFood(fg: F_G.Food_Guy, mar:mar.Market):
    fg.cargaison_nourriture[0][1]+=mar.nourriture[0][1]
    mar.nourriture[0][1] = 0
    fg.cargaison_nourriture[1][1]+=mar.nourriture[1][1]
    mar.nourriture[0][1] = 0
    fg.cargaison_nourriture[2][1]+=mar.nourriture[2][1]
    mar.nourriture[2][1] = 0



