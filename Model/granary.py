import sys
sys.path.insert(0, '..')
from Model import batiment as b


class Granary(b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self, 3, 71, posx, posy, 100, -4, 1, 2, 2, 6,)
        self.max_space = 50
        self.occupied_space = 0
        self.name = "Granary"
        self.nourriture = [['ble', 0], ['fruits', 0], ['viande', 0]]
        self.produits = [['argile', 0], ['potterie', 0], ['huile', 0]]

    def get_delivery(self, chargement):
        print("chargement", chargement)
        if (chargement[0] == 'ble'):
            print("chargement de ble")
            self.nourriture[0][1] = self.nourriture[0][1] + chargement[1]
        if chargement[0] == 'fruits':
            self.nourriture[1][1] += chargement[1]
        if chargement[0] == 'viandes':
            self.nourriture[2][1] += chargement[1]
        if chargement[0] == 'olives':
            self.produits[2][1] += chargement[1]
        if chargement[0] == 'argile':
            self.produits[0][1] += chargement[1]

    def isFull(self):
        return self.max_space == self.occupied_space

    def hasFood(self):
        return self.nourriture[0][1] + self.nourriture[1][1] + self.nourriture[2][1] > 0
