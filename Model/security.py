import sys
sys.path.insert(0, '..')
from Model import batiment as b


class Prefecture(b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self, 1, 55, posx, posy, 30, -2, 1, 1, 2, 6)
        self.name = "Prefecture"