class Terrain:
    def __init__(self, x, y, id_t):
        self.nbr_cases = 1
        self.pos_x = x  # position x sur la map
        self.pos_y = y  # position y sur la map
        self.name = 'Terrain vide'
        self.id = id_t  # id du terrain:wq



class Water(Terrain):
    def __init__(self, posx, posy):
        Terrain.__init__(self, posx, posy, 1)
        self.name = "Water"


class Rock(Terrain):
    def __init__(self, posx, posy):
        Terrain.__init__(self, posx, posy, 2)
        self.name = "Rock"


class Enter_Pannel(Terrain):
    def __init__(self, posx, posy):
        Terrain.__init__(self, posx, posy, 115)
        self.name = "Enter_Pannel"


class Exit_Pannel(Terrain):
    def __init__(self, posx, posy):
        Terrain.__init__(self, posx, posy, 116)
        self.name = "Exit_Pannel"
