import sys

sys.path.insert(0, '..')
from Model import batiment as b


class Herb(b.Batiment):
    def __init__(self, x, y):
        b.Batiment.__init__(self, x, y, 0, 0, 0, 0, 0, 0, 0, 0)
        self.ind_fire = -1
        self.ind_eff = -1
        self.name = "Herb"
