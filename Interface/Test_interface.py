import pygame

# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
window_size = (600, 400)

# Créer la fenêtre
screen = pygame.display.set_mode(window_size)

# Définir les coordonnées et les dimensions de la zone à éclaircir
x, y = 100, 100
width, height = 200, 200

# Créer la surface de la zone à éclaircir
area_surface = pygame.Surface((width, height))

# Remplir la surface avec une couleur
area_surface.fill((255, 0, 0))

# Réduire la transparence de la surface (alpha = 50)
area_surface.set_alpha(50)

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        # Si l'utilisateur quitte, arrêter la boucle
        if event.type == pygame.QUIT:
            running = False

    # Récupérer la position de la souris
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Détecter si la souris est dans la zone
    if (x <= mouse_x <= x + width) and (y <= mouse_y <= y + height):
        # Dessiner la surface de la zone avec une transparence réduite
        screen.blit(area_surface, (x, y))
    else:
        # Dessiner la surface de la zone avec une transparence normale
        screen.blit(area_surface, (x, y))

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
