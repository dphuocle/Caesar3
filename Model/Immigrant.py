import sys

sys.path.insert(0, '..')
from Model import Walker as W


class Immigrant(W.Walker):
    def __init__(self, x, y, bat):
        W.Walker.__init__(self, x, y, bat)
        self.name = 'Immigrant'
