import sys

sys.path.insert(0, '..')
from Model import batiment as b


class tree(b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self, 1, 3, posx, posy, 0, 0, 0, 0, 0, 0)
        self.name = "Tree"
