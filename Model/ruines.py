import sys

sys.path.insert(0, '..')
from Model import batiment as b

#id ruine: 555
class Ruin(b.Batiment):
    def __init__(self, x, y):
        b.Batiment.__init__(self, 1, 555, x, y,  0, 0, 0, 0, 0, 0)
        self.name = "Ruin"
        self.ind_fire = -1
        self.ind_eff = -1