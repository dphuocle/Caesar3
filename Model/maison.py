import sys

sys.path.insert(0, '..')
from Model import batiment as b


# classe de maison servant a définir les méthodes communes a toutes les maisons
class Maison(b.Batiment):
    def __init__(self, nbr_cases, id_bat, posx, posy, cst, des, stp, sze, rge, emp):
        super().__init__(nbr_cases, id_bat, posx, posy, cst, des, stp, sze, rge, emp)
        self.name = 'Maison'
        self.nourriture = [['ble', 0 ], ['fruits', 0], ['viande', 0]]
        self.produits = [['argile',0], ['potterie',0], ['huile',0]]
        self.popLim = 1
        self.curpop = 0
        self.employed = 0
        self.faith = 0
        self.acces_eau = 0

        
    def get_delivery(self, chargement):
        print("chargement",chargement)
        if(chargement[0] == 'ble'):
            self.nourriture[0][1] = self.nourriture[0][1] + chargement[1]
        if chargement[0] == 'fruits':
            self.nourriture[1][1] += chargement[1]
        if chargement[0] == 'viandes':
            self.nourriture[2][1] += chargement[1]
        if chargement[0] == 'olives':
            self.produits[2][1] += chargement[1]
        if chargement[0] == 'argile':
            self.produits[0][1] += chargement[1]

    def inccpop(self):
        if self.popLim > self.curpop :
            self.curpop += 1
        else :
            self.curpop = self.popLim

    def hasEnoughFood(self):
        print("test enough food")
        return (self.nourriture[0][1]+self.nourriture[1][1]+self.nourriture[2][1]) > 10
 
class Panneau(Maison):
    def __init__(self, x, y):
        Maison.__init__(self, 1, 7, x, y, 10, -3, 1, 1, 3, 0)
        self.ind_fire = -1 
        self.name = "Panneau"



class Maison_1(Maison):
    def __init__(self, x, y):
        Maison.__init__(self, 1, 10, x, y, 10, -3, 1, 1, 3, 0)
        self.name = 'Maison 1'
        self.des_prev = -99  # cf https://gamefaqs.gamespot.com/pc/63635-caesar-iii/faqs/14466
        self.des_next = -10
        # self.entNeeded = 0
        self.watNeeded = 0
        self.godNeeded = 0
        # self.eduNeeded = 0
        self.marketNeeded = 0
        # self.barberNeeded = 0
        # self.bathNeeded = 0
        # self.medNeeded = 0
        self.foodNeeded = 0
        # self.potNeeded = 0
        # self.oilNeeded = 0
        # self.furNeeded = 0
        # self.wineNeeded = 0
        self.crimeIncrement = 3
        self.crimeBase = 25
        self.prospCap = 5
        self.popLim = 5
        self.taxMultiplier = 1


class Maison_2(Maison):
    def __init__(self, x, y):
        b.Batiment.__init__(self, 1, 11, x, y, 0, -3, 1, 1, 3, 0)
        self.name = 'Maison 2'
        self.acces_eau = 0
        self.des_prev = -12  # cf https://gamefaqs.gamespot.com/pc/63635-caesar-iii/faqs/14466
        self.des_next = -5
        # self.entNeeded = 0
        self.watNeeded = 1
        self.godNeeded = 0
        # self.eduNeeded = 0
        self.marketNeeded = 0
        # self.barberNeeded = 0
        # self.bathNeeded = 0
        # self.medNeeded = 0
        self.foodNeeded = 0
        # self.potNeeded = 0
        # self.oilNeeded = 0
        # self.furNeeded = 0
        # self.wineNeeded = 0
        self.crimeIncrement = 3
        self.crimeBase = 25
        self.prospCap = 10
        self.popLim = 7
        self.taxMultiplier = 1


class Maison_3(Maison):
    def __init__(self, x, y):
        b.Batiment.__init__(self, 1, 12, x, y, 0, -2, 1, 1, 2, 0)
        self.name = 'Maison 3'
        
        self.acces_eau = 0
        self.des_prev = -7  # cf https://gamefaqs.gamespot.com/pc/63635-caesar-iii/faqs/14466
        self.des_next = 0
        # self.entNeeded = 0
        self.watNeeded = 1
        self.godNeeded = 0
        # self.eduNeeded = 0
        self.marketNeeded = 1
        # self.barberNeeded = 0
        # self.bathNeeded = 0
        # self.medNeeded = 0
        self.foodNeeded = 1
        # self.potNeeded = 0
        # self.oilNeeded = 0
        # self.furNeeded = 0
        # self.wineNeeded = 0
        self.crimeIncrement = 3
        self.crimeBase = 25
        self.prospCap = 15
        self.popLim = 9
        self.taxMultiplier = 1


class Maison_4(Maison):
    def __init__(self, x, y):
        b.Batiment.__init__(self, 1, 13, x, y, 0, -2, 1, 1, 2, 0)
        self.name = 'Maison 4'
        
        self.acces_eau = 0
        self.des_prev = -2  # cf https://gamefaqs.gamespot.com/pc/63635-caesar-iii/faqs/14466
        self.des_next = 4
        # self.entNeeded = 0
        self.watNeeded = 1
        self.godNeeded = 1
        # self.eduNeeded = 0
        self.marketNeeded = 1
        # self.barberNeeded = 0
        # self.bathNeeded = 0
        # self.medNeeded = 0
        self.foodNeeded = 1
        # self.potNeeded = 0
        # self.oilNeeded = 0
        # self.furNeeded = 0
        # self.wineNeeded = 0
        self.crimeIncrement = 3
        self.crimeBase = 25
        self.prospCap = 20
        self.popLim = 11
        self.taxMultiplier = 1
