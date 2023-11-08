import sys

sys.path.insert(0, '..')


class NoWalker:
    def __init__(self):
        self.name = 'no Walker'


class Walker(NoWalker):
    def __init__(self, x, y, bat):
        super().__init__()
        self.x = x
        self.y = y
        self.name = 'unknown'
        self.ttl = 20
        self.tab_path = []
        self.batiment = bat
        self.dest_x = -1
        self.dest_y = -1
        self.has_moved = 0
        self.prev_x = x # Necessaire pour le déplacement
        self.prev_y = y # Laisser ces valeur pour deplacment_basique()
        self.nx = x
        self.ny = y
