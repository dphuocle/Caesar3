from os import getcwd


TILE_SIZE = 29
path_to_sprites = f"{getcwd()}/View/Sprites/Used_sprites/"
path_to_Nature = path_to_sprites + "Nature"
path_to_House = path_to_sprites + "Home_builds"
path_to_Utilities = path_to_sprites + "Utilities"
path_to_Walkers = path_to_sprites + "Walkers"

overlay = ""

TILE_SIZE_MINI_MAP = 1.6

# Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)
MINI_MAP_COLOR = (102, 0, 51)

sizedbuildings_2 = {"market"}
sizedbuildings_3 = {"reservoir_empty", "reservoir_full", "warehouse", "granary", "farm"}