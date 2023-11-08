import sys

sys.path.insert(0, '..')
from Model import batiment as b


class Well(b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self, 1, 92, posx, posy, 5, -1, 1, 2, 1, 1)
        self.name = "Well"


class Reservoir(b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self, 3, 90, posx, posy, 80, -6, 1, 2, 3, 0)
        self.water_flow = None
        self.name = "Reservoir"

    def change_id(self):
        if self.water_flow == 0:
            self.id = 90
        if self.water_flow == 1:
            self.id = 9000


class Aquaduct(b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self, 1, 8, posx, posy, 8, -2, 1, 1, 2, 0)
        self.water_flow = 0
        self.path = 0
        self.name = "Aquaduct"


class Fountain(b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self, 1, 91, posx, posy, 15, 0, 0, 0, 0, 4)
        self.water_flow = 0
        self.name = "Fountain"
