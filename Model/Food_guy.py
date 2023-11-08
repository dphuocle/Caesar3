import sys

sys.path.insert(0, '..')
from Model import Walker as W
from Model import delivery_guy as DG


# food_guy a essentiellement le même fonctionnement que delivery guy,
# faut juste le faire heriter et rajouter les conditions appropriées:
# doit uniquement être appelable d'un marchÃ©
# les déplacement vont soit du marché aux greniers, soit du marche au random

class Food_Guy(DG.Delivery_Guy):
    def __init__(self, x, y, bat, role, bat_dest):
        DG.Delivery_Guy.__init__(self, x, y, bat, bat_dest)
        self.name = 'Food_Guy'
        self.role = role
        self.bat_destination = bat_dest