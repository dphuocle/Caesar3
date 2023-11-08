import sys

sys.path.insert(0, '..')
from Model import Walker as W


class Delivery_Guy(W.Walker):
    def __init__(self, x, y, bat, bat_cible, type_marchandise='ble'):
        W.Walker.__init__(self, x, y, bat)
        self.name = 'Delivery_Guy'
        self.cargaison_nourriture = [['ble', 0], ['fruits', 0], ['viande', 0]]
        self.cargaison_produits = [['argile', 0], ['potterie', 0], ['huile', 0], ['', 0], ['', 0]]
        self.bat_destination = bat_cible
        self.type_marchandise = type_marchandise

    # ajoute une marchandise a la cargaison
    def ajout_marchandise(self, nb):
        if self.type_marchandise == 'ble': self.cargaison_nourriture[0][1] = self.cargaison_nourriture[0][1] + nb
        if self.type_marchandise == 'fruits': self.cargaison_nourriture[1][1] = self.cargaison_nourriture[1][1] + nb
        if self.type_marchandise == 'viande': self.cargaison_nourriture[2][1] = self.cargaison_nourriture[2][1] + nb
        if self.type_marchandise == 'olives': self.cargaison_produits[2][1] = self.cargaison_produits[2][1] + nb
        if self.type_marchandise == 'argile': self.cargaison_produits[0][1] = self.cargaison_produits[0][1] + nb

    # decharge une marchandise
    def dechargement(self, type_transport):
        if type_transport == 'ble':
            res = ["ble", self.cargaison_nourriture[0][1]]
            self.cargaison_nourriture[0][1] = 0
            return res
        if type_transport == 'fruits':
            res = ["fruits", self.cargaison_nourriture[1][1]]
            self.cargaison_nourriture[1][1] = 0
            return res
        if type_transport == 'viande':
            res = ["viande", self.cargaison_nourriture[2][1]]
            self.cargaison_nourriture[2][1] = 0
            return res
        if type_transport == 'olives':
            res = ["olives", self.cargaison_produits[2][1]]
            self.cargaison_produits[2][1] = 0
            return res
        if type_transport == 'argile':
            res = ["argile", self.cargaison_produits[0][1]]
            self.cargaison_produits[0][1] = 0
            return res

    def HasSomething(self):
        return any(self.cargaison_nourriture[i][1] > 0 or self.cargaison_produits[i][1] > 0 for i in range(3))
