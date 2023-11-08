import sys
sys.path.insert(0, '..')
from Model import batiment as b


class Temple(b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self, 1, 60, posx, posy, 50,4,2,-1,6,2)
        self.name = "Temple"