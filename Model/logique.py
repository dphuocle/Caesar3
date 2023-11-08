import pygame as pg
import pickle
import sys
import random
sys.path.insert(0, '..')

from Model import matrice as m


#walker nx ny, batiment detruire plusieurs cases, maisons construires plusieurs cases
# Definition des Userevents


Nume_maison = pg.USEREVENT
Nume_eau = pg.USEREVENT +1
Nume_route = pg.USEREVENT +2
Nume_theatre = pg.USEREVENT +3
Nume_nourriture = pg.USEREVENT+4
Nume_sante = pg.USEREVENT +5
Nume_prefecure = pg.USEREVENT+6
Nume_ingenieur = pg.USEREVENT +7
Nume_administratif = pg.USEREVENT+8
Nume_pelle = pg.USEREVENT +9
Nume_increase_speed = pg.USEREVENT +10
Nume_decrease_speed = pg.USEREVENT +11
Nume_pause_speed = pg.USEREVENT +12
Nume_well = pg.USEREVENT +13
Nume_overlay = pg.USEREVENT +14
Nume_fountain = pg.USEREVENT +15
Nume_save = pg.USEREVENT +16 
Nume_load = pg.USEREVENT +17

Unalterable = [0,1,2,3,4,5,6,666,116,115 , 91 ]

# En jeu (dans le main), on n'utilisera que les fonctions de logique.py, celles prÃ©sente dans les autres fichiers servent de briques pour celles prÃ©sentes ici


# pour les variables globales: il nous faut la liste des greniers et des entrepots, et faire une methode qui dit s'ils sont plein ou pas
# pour eviter de devoir faire un scan sur toute la matrice a chaque fois qu'on a besoin de faire une livraison

# cree un walker pour effectuer une livraison
# prend en parametre le batiment qui invoque la livraison, le type de marchandise, la quantité
def Delivery(Bat_depart, type_march, quant):
    (x, y) = m.SearchforRoad(Bat_depart.pos_x, Bat_depart.pos_y, m.Mat_batiment)
    # print("Heres the delivery")
    if x != -1:
        cible = m.SearchforSpace(type_march)
        if cible == None:
            return -1
        # print("MUDA MUDA")
        dg = m.add_perso(x, y, 'Delivery Guy', m.Mat_perso, Bat_depart, cible, type_march)
        dg.ajout_marchandise(quant)
        # Bat dest devra être calculé : grenier, entrepot, marché
        (cx, cy) = cible.ret_coord()
        #print("cible", cx, cy)
        (dx, dy) = m.SearchforRoad(cx, cy, m.Mat_batiment)
        dg.dest_x = dx
        dg.dest_y = dy
        # print(dx, dy)

def findFood(Bat_depart):
    (x, y) = m.SearchforRoad(Bat_depart.pos_x, Bat_depart.pos_y, m.Mat_batiment)
    if x != -1:
        cible = m.SearchforFood()
        if cible == None:
            return -1
        fg=m.add_perso(x, y, "Food_Guy", m.Mat_perso,Bat_depart, cible,role="collecteur")
        (cx, cy)=cible.ret_coord()
        # print("cible", cx, cy)
        (dx, dy) = m.SearchforRoad(cx, cy, m.Mat_batiment)
        fg.dest_x = dx
        fg.dest_y = dy
        # print(dx,dy)


# renvoie l'ID d'un batiment placé sur une case de la matrice des batiments, dont les coordonées sont données en argument
# Pour un batiment de plusieurs cases, ne donne l'id que si la case est celle en haut, autrement renvoie 666
def getID(i, j):
    if m.Mat_batiment[j][i].pos_x + m.Mat_batiment[j][i].nbr_cases - 1 == i and m.Mat_batiment[j][i].pos_y + \
            m.Mat_batiment[j][i].nbr_cases - 1 == j:
        return m.Mat_batiment[j][i].id
    else:
        return 666


def getID_base_matrix( i , j ) :
    return m.matrix[j][i]

# initialise les matrices de jeux
# incomplet: reste à implémenter les load
def init_game():
    m.departureMatrice(m.Mat_batiment)


# ajoute un batiment si l'espace sur la carte est libre
def Add_bat_game(x, y, id_bat):
    for i in range(m.id_size[id_bat]):
        for j in range(m.id_size[id_bat]):
            if i+x > 39 or y+j > 39 or m.Mat_batiment[y + j][x + i].name != "Herb":
                return -1
    m.add_bat(x, y, id_bat, m.Mat_batiment)
    return 0

def get_speed_game() : return Speed_game

def get_fire_level(x,y):
    if m.Mat_batiment[y][x].id not in Unalterable:
        return m.Mat_batiment[y][x].ind_fire
    return -1

def get_eff_level(x,y):
    if m.Mat_batiment[y][x].id not in Unalterable:
        return m.Mat_batiment[y][x].ind_eff
    return -1

class State:
    def __init__(self):
        self.Matrice_bat = m.Mat_batiment
        self.Matrice_perso = m.Mat_perso
        # self.Variable_Globale = [] # will be used later, now there's nothing to put in there

    def mise_a_jour(self):
        self.Matrice_bat = m.Mat_batiment
        self.Matrice_perso = m.Mat_perso
        # self.Variable_Globale = []

    def uploadFromSave(self):
        m.Mat_batiment = self.Matrice_bat
        m.Mat_perso = self.Matrice_perso


# creer un fichier de sauvegarde, à partir de l'état actuel du jeu

data_set = [m.Mat_batiment , m.Mat_perso , m.Mat_route , m.Mat_fire , m.Mat_water ]

def sauvegarde(nom):
    sauv = State()
    with open(nom, "wb") as f:
        pickle.dump(sauv, f)


def savefile(filename) : 

    if ".pkl" not in filename :
        filename += ".pkl"

    with open( f"Terminus_saves/{filename}" , "wb") as f :
        pickle.dump(m.Mat_batiment,f)
        pickle.dump(m.Mat_perso,f)
        pickle.dump(m.Mat_route,f)
        pickle.dump(m.Mat_fire,f)
        pickle.dump(m.Mat_water,f)

def loadfile(filename) :

    if ".pkl" not in filename :
        filename += ".pkl"

    with open( f"Terminus_saves/{filename}" , "rb" ) as f:
        m.Mat_batiment = pickle.load(f)
        m.Mat_perso = pickle.load(f)
        m.Mat_route = pickle.load(f)
        m.Mat_fire = pickle.load(f)
        m.Mat_water = pickle.load(f)
            

# charge un fichier de sauvegarde et met a jour le jeu
def load(nom):
    sauv = State()
    with open(nom, "rb") as f:
        sauv = pickle.load(f)
    sauv.uploadFromSave()


def getWalker(i, j):
        return m.Mat_perso[j][i][0]

def getDesirability(bat):
    proxy = m.get_bat_prox(bat.pos_x,bat.pos_y,5)
    somme = 0
    for batis in proxy:
        somme += batis.initDesirability
    return somme
def check_water():
    for i in range(m.nb_cases):
        for j in range(m.nb_cases):
            if m.InTable(m.Mat_batiment[j][i].name, ["Panneau", "Maison 1", "Maison 2", "Maison 3"]) and m.Mat_water[i][j]:
                m.Mat_batiment[j][i].acces_eau = 1
            if m.InTable(m.Mat_batiment[j][i].name, ["Panneau", "Maison 1", "Maison 2", "Maison 3"]) and not m.Mat_water[i][j]:
                m.Mat_batiment[j][i].acces_eau = 0


def evolve(bat):
    # print("is Evolving")
    x = bat.pos_x
    y = bat.pos_y
    if bat.name == 'Maison 1':
        m.add_bat(x, y, 11, m.Mat_batiment)
    elif bat.name == 'Maison 2':
        m.add_bat(x, y, 12, m.Mat_batiment)
    batiment = m.Mat_batiment[y][x]
    batiment.nourriture = bat.nourriture
    batiment.produits = bat.produits
    batiment.curpop = bat.curpop
    batiment.employed = bat.employed
    batiment.faith = bat.faith
    batiment.acces_eau = bat.acces_eau
    batiment.Walk = bat.Walk
    for p in bat.Walk:
        p.batiment = batiment

def devolve(bat):
    # print("is Devolving")
    x = bat.pos_x
    y = bat.pos_y
    if bat.name == 'Maison 3':
        m.add_bat(x, y, 11, m.Mat_batiment)
    elif bat.name == 'Maison 2':
        m.add_bat(x, y, 10, m.Mat_batiment)
    batiment = m.Mat_batiment[y][x]
    batiment.nourriture = bat.nourriture
    batiment.produits = bat.produits
    batiment.curpop = bat.curpop
    print("curpop : " , batiment.curpop ," New popLim  :" , batiment.popLim )
    if bat.curpop >= batiment.popLim:
        m.Population -= bat.curpop - batiment.popLim 
        batiment.curpop = batiment.popLim

    else: batiment.curpop = bat.curpop
    batiment.employed = bat.employed
    batiment.faith = bat.faith
    batiment.Walk = bat.Walk
    for p in bat.Walk:
        p.batiment = batiment

# fonction qui a realiser des opérations entre walkers et batiments:
# si c'est un pompier, il va diminuer les indices de feu des batiments autour de lui, et si il y a un feu, doit aller l'eteindre
# si c'est un ingenieur, il va diminuer les indices d'effondrement des batiments autour de lui
# si c'est un Delivery_Guy, et qu'il est a destination, il va proceder a un echange (il faut enlever cette partie du deplacement pour la mettre içi)
# si c'est pretre, il va augmenter l'indice de foi des maisons autour de lui
# si c'est un Food_Guy, et que sa mission est de distribuer des biens/bouffe aux habitants, il va donner une certaine quantité de ce qu'il a aux maisons autour de lui
def test_walker_logique():
    for i in range(m.nb_cases):
        for j in range(m.nb_cases):
            if m.Mat_perso[j][i][0].name != "no Walker":
                count = 0
                for k in range(len(m.Mat_perso[j][i])):
                    perso = m.Mat_perso[j][i][count]
                    count +=1
                    if perso.name == "Prefect":
                        proxy = m.get_bat_prox(i, j, 5)
                        # #print("proxy", proxy)
                        for bat in proxy:
                            bat.ind_fire = 0
                        for w in range(5):
                            for s in range(5):
                                if(s+perso.y <= 39 and w+perso.x <= 39):
                                    m.Mat_fire[w+perso.x][s+perso.y] = 0
                                if (s + perso.y <= 39 and -w + perso.x >= 0):
                                    m.Mat_fire[-w+perso.x][perso.y+s] = 0
                                if(-s+perso.y >= 0 and w + perso.x <= 39):
                                    m.Mat_fire[w + perso.x][-s + perso.y] = 0
                                if (-s + perso.y >= 0 and -w + perso.x >= 0):
                                    m.Mat_fire[-w + perso.x][perso.y - s] = 0


                    elif perso.name == "Engineer":
                        proxy = m.get_bat_prox(i, j, 5)
                        #print("proxy", proxy)
                        for bat in proxy:
                            bat.ind_eff = 0
                    elif perso.name == "Priest":
                        proxy = m.get_bat_prox(i, j, 4)
                        #print("proxy", proxy)
                        for bat in proxy:
                            if m.InTable(bat.name, ["Maison 1", "Maison 2", "Maison 3", "Maison 4"]):
                                bat.faith = bat.faith + 40
                    elif perso.name == "Recruteur":
                        perso.nb_a_recruter = perso.batiment.neededEmployees - perso.batiment.curEmployees
                        proxy = m.get_bat_prox(i, j, 4)
                        #print("proxy recruteur", proxy)
                        for bat in proxy:
                            if m.InTable(bat.name, ["Maison 1", "Maison 2", "Maison 3", "Maison 4"]):
                                recruit = perso.nb_a_recruter
                                #print("goal recruit:", recruit)
                                if bat.employed < bat.curpop and recruit > 0:
                                    if (bat.curpop - bat.employed) >= recruit:
                                        bat.employed += recruit
                                        perso.nb_a_recruter = 0
                                        perso.batiment.curEmployees += recruit
                                    else:
                                        recruted = (bat.curpop - bat.employed)
                                        perso.nb_a_recruter -= recruted
                                        bat.employed = bat.curpop
                                        perso.batiment.curEmployees += recruted
                                #print("Le nombre d'employés de", perso.batiment,  "est ", perso.batiment.curEmployees)

                        if perso.nb_a_recruter == 0:
                            perso.batiment.hasRecruteur = 0
                            m.kill_walker(perso)
                            count -= 1
                            #print("recruteur tué")

                    elif perso.name == "Delivery_Guy" and perso.HasSomething():
                        proxy = m.get_bat_prox(i, j, 4)
                        #print("test delivery guy")
                        if m.InTable(perso.bat_destination, proxy):
                            #print("tentative echange")
                            m.echange(perso)
                            m.kill_walker(perso)
                            count -= 1
                    elif perso.name == "Food_Guy":
                        if perso.role == 'collecteur':
                            proxy = m.get_bat_prox(i, j, 2)
                            #print("test collecteur")
                            if m.InTable(perso.bat_destination, proxy):
                                #print("tentative collecte")
                                m.collecte(perso)
                                #print(perso.cargaison_nourriture)
                                perso.role = "livreur"
                                perso.bat_destination = perso.batiment
                                (dx,dy) = m.SearchforRoad(perso.batiment.pos_x,perso.batiment.pos_y,m.Mat_batiment)
                                if dx != -1:
                                    perso.dest_y = dy
                                    perso.dest_x = dx
                        if perso.role == "livreur":
                            #print("ici")
                            proxy = m.get_bat_prox(i, j, 2)
                            if m.InTable(perso.bat_destination, proxy):
                                #print("test livreur")
                                m.livraison(perso)
                                m.kill_walker(perso)
                                count -= 1
                        elif perso.role == 'distributeur':
                            proxy = m.get_bat_prox(i, j, 4)
                            #print("there is a ditributeur")
                            if perso.dest_x == -1:
                                #print("distribution en cours...")
                                for bat in proxy:
                                    if not perso.HasSomething():
                                        m.kill_walker(perso)
                                        count -= 1
                                    if m.InTable(bat.name, ["Maison 1", "Maison 2", "Maison 3", "Maison 4"]) and not bat.hasEnoughFood():
                                        m.giveFood(perso, bat)
                            if not perso.HasSomething():
                                m.kill_walker(perso)
                                count -= 1
                        else:
                            continue
                    elif perso.name == "Immigrant":
                        #print(perso.dest_x, perso.dest_y, "test destination")
                        if perso.x == perso.dest_x and perso.y == perso.dest_y:
                            if perso.batiment.name == "Panneau":
                                #print("debug")
                                x = perso.batiment.pos_x
                                y = perso.batiment.pos_y
                                m.add_bat(x,y,10, m.Mat_batiment)
                                perso.batiment.Walk.remove(perso)
                                perso.batiment = m.Mat_batiment[y][x]
                                perso.batiment.Walk.append(perso)
                            perso.batiment.inccpop()
                            m.kill_walker(perso)
                            count -= 1


# fonction qui teste les condition des batiments:
# va tester le feu, l'effondrement
# si un batiment a produit quelque chose, appelle un livraison
# si un marché a besoin de produits, va en chercher
# si un marché a des produits, appelle une distribution (reste a implementer)
# si c'est une maison, va consommer de la nourriture, tester l'evolution / regression de la maison
def test_bat_logique():
    m.check_fire_eff()
    check_water()
    for i in range(m.nb_cases):
        for j in range(m.nb_cases):
            if not m.InTable(m.Mat_batiment[j][i].name, ["Herb", "Tree", "Rock", "Enter_Pannel", "Exit_Pannel", "Water"]):
                bat = m.Mat_batiment[j][i]
                if bat.curEmployees < bat.neededEmployees and not bat.hasRecruteur and (m.SearchforRoad(i, j, Mat=m.Mat_batiment) != (-1,-1)):
                    m.invoke_walker(bat, "Recruteur")
                    bat.hasRecruteur = 1
                elif bat.hasCheck == 0:
                    bat.hasCheck = 1
                    if bat.name == "Farm":
                        if bat.curEmployees>=1:
                            bat.growFood()
                            #print(bat.ind_Harv)
                            if bat.ind_Harv >= 6:
                                #print("time for delivery")
                                Delivery(bat, 'ble', bat.ind_Harv * 2)
                                bat.ind_Harv = 0
                    elif bat.name == "Prefecture":
                        if bat.Walk == []:
                            m.invoke_walker(bat, "Prefect")
                    elif bat.name == "EngineersPost":
                        if bat.Walk == []:
                            m.invoke_walker(bat, "Engineer")
                    elif bat.name == "Temple":
                        if bat.Walk == []:
                            m.invoke_walker(bat, "Priest")
                    elif bat.name == "Market":
                        if bat.occupied_space <= 15:
                            if not bat.hasEnoughFood() and bat.Walk == []:
                                findFood(bat)
                            elif bat.Walk == []:
                                (x, y) = m.SearchforRoad(bat.pos_x, bat.pos_y, m.Mat_batiment)
                                if x != -1:
                                    FG = m.add_perso(x,y,"Food_Guy",m.Mat_perso,bat,None, role= "distributeur")
                                    m.getFood(FG, bat)

                    elif m.InTable(bat.name,["Panneau", "Maison 1", "Maison 2", "Maison 3"]):
                        if(bat.name == "Maison 1" and bat.acces_eau == 1):
                            #print("will evolve soon")
                            evolve(bat)
                            #print("evolved")
                        elif (bat.name == "Maison 2" and bat.acces_eau == 1 and bat.nourriture[0][1]>5):
                            #print("will evolve soon into maison 3")
                            evolve(bat)
                            #print("evolved")
                        elif (bat.name == "Maison 3" or bat.name == "Maison 2") and not bat.acces_eau:
                            #print("you will devolve :ghost:")
                            devolve(bat)
                            # if bat.name =="Maison 2":
                            #     devolve(bat)
                            #print("devolved")
                        elif bat.name == "Maison 3" and bat.nourriture[0][1] == 0:
                            #print("you will devolve :ghost:")
                            devolve(bat)
                            #print("devolved")
                        if bat.curpop < bat.popLim and bat.Walk == []:
                            n = getDesirability(bat)
                            if n >= -99:
                                for i in range(bat.popLim-bat.curpop):
                                    m.invoke_migrant(bat)
                        if bat.nourriture[0][1]>0 and random.random()<0.3:
                            bat.nourriture[0][1]-=1

    for i in range(m.nb_cases):
        for j in range(m.nb_cases):
            m.Mat_batiment[j][i].hasCheck = 0


def build_pannel_grid(x1, y1, x2, y2):
    for i in range(min(x1,x2), max(x1,x2)+1):
        for j in range(min(y1,y2), max(y1,y2)+1):
            Add_bat_game(i, j, m.name_id["Panneau"])

def build_grid(x1, y1, x2, y2 , id_bat):
    for i in range(min(x1,x2), max(x1,x2)+1):
        for j in range(min(y1,y2), max(y1,y2)+1):
            Add_bat_game(i, j,id_bat)

def destroy_grid(x1,y1,x2,y2):
    # print("grid")
    # print(x1,y1,x2,y2)
    for i in range(min(x1,x2), max(x1,x2)+1):
        for j in range(min(y1,y2), max(y1,y2)+1):
            m.suppr_Batiment(i,j,m.Mat_batiment)

def isHerb(x,y):
    return m.Mat_batiment[y][x].name == "Herb"


def Square_path(x1,y1,x2,y2):
    if all(isHerb(i,y1) for i in range(min(x1,x2),max(x1,x2)+1)) and all(isHerb(x2,j) for j in range(min(y1,y2), max(y1,y2)+1)):
        for i in range(min(x1,x2),max(x1,x2)+1):
            Add_bat_game(i,y1,m.name_id["Path"])
        for j in range(min(y1,y2), max(y1,y2)+1):
            Add_bat_game(x2,j,m.name_id["Path"])
    elif all(isHerb(x1,j) for j in range(min(y1,y2), max(y1,y2)+1)) and all(isHerb(i,y2) for i in range(min(x1,x2),max(x1,x2)+1)):
        for j in range(min(y1,y2), max(y1,y2)+1):
            Add_bat_game(x1,j,m.name_id["Path"])
        for i in range(min(x1, x2), max(x1, x2) + 1):
            Add_bat_game(i,y2,m.name_id["Path"])


actual_position = 0 
Speed_game = 100
speed_level = 5
tab_speed = [10,20,30,50,70,100,150,200,300,400,500]


def increase_speed():
    global Speed_game, speed_level
    if speed_level < len(tab_speed) -1 :
        speed_level += 1 
        Speed_game = tab_speed[speed_level]

val_overlay = 0   

def decrease_speed():
    global Speed_game, speed_level
    if speed_level > 0 :
        speed_level -= 1 
        Speed_game = tab_speed[speed_level]

def pause_speed() :
    global Speed_game
    if Speed_game == 0 :
        Speed_game = tab_speed[speed_level]
    else : 
        Speed_game = 0 

def Tour_jeu() :
    global actual_position
    actual_position += Speed_game
    
    if actual_position >= 1000 :
        actual_position = 0 
        m.deplacement_perso(m.Mat_perso , m.nb_cases_x , m.nb_cases_y)
        m.check_fire_eff()
        test_bat_logique()
        test_walker_logique()

def get_overlay() :
    global val_overlay
    match val_overlay :
        case 1 : return "water"
        case 2 : return "bat"
        case 3 : return "fire"
        case _ : return ""

def get_water(x,y) : 
    return m.Mat_water[x][y]

def event_to_logic(nume, pos_init, pos_final, Name_game = "tmp.pkl"):
    if not pos_final :
        pos_final = pos_init

    if nume == Nume_maison:
        (x1, y1) = pos_init
        (x2, y2) = pos_final
        build_pannel_grid(x1,y1,x2,y2)

    elif nume == Nume_pelle:
        (x1, y1) = pos_init
        (x2, y2) = pos_final


        destroy_grid(x1,y1,x2,y2)
    elif nume == Nume_route:
        (x1, y1) = pos_init
        (x2, y2) = pos_final
        Square_path(x1,y1,x2,y2)


    elif nume == Nume_increase_speed :
        increase_speed()

    elif nume == Nume_decrease_speed :
        decrease_speed()

    elif nume == Nume_pause_speed :
        pause_speed()
    elif(nume == Nume_well):
       if(pos_init == pos_final):
           (x,y) = pos_init
           Add_bat_game(x,y,m.name_id["Well"])
    
    elif nume == Nume_nourriture : 
        if pos_init == pos_final :
             Add_bat_game(pos_init[0],pos_init[1],m.name_id["Farm"])

    elif nume == Nume_eau :
        build_grid(pos_init[0],pos_init[1],pos_final[0],pos_final[1] , m.name_id["Well"])

    elif nume == Nume_ingenieur :
        build_grid(pos_init[0],pos_init[1],pos_final[0],pos_final[1] , m.name_id["EngineersPost"])

    elif nume == Nume_prefecure :
        build_grid(pos_init[0],pos_init[1],pos_final[0],pos_final[1] , m.name_id["Prefecture"])

    elif nume == Nume_overlay :
        global val_overlay
        val_overlay = (val_overlay +1 )%4

    elif nume == Nume_fountain :
        build_grid(pos_init[0],pos_init[1],pos_final[0],pos_final[1] , m.name_id["Fountain"])

    elif nume == Nume_administratif : 
        build_grid(pos_init[0],pos_init[1],pos_final[0],pos_final[1] , m.name_id["Warehouse"])

    elif nume == Nume_sante : 
        build_grid(pos_init[0],pos_init[1],pos_final[0],pos_final[1] , m.name_id["Granary"])

    elif nume == Nume_theatre : 
        build_grid(pos_init[0],pos_init[1],pos_final[0],pos_final[1] , m.name_id["Market"])

    elif nume == Nume_save : 
        savefile(Name_game)

    elif nume == Nume_load : 
        loadfile(Name_game)
        

# a garder
init_game()