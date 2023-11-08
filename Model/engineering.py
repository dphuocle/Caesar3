import sys
sys.path.insert(0, '..')
from Model import batiment as b


class EngineersPost(b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self, 1, 81, posx, posy, 30, 0, 1, 1, 1, 5)
        self.name = "EngineersPost"
