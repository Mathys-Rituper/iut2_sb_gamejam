import pygame
import game
#Initialisation de pygame
pygame.init()

#Initialisation de la fenêtre
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Game Jam 2021")


game = game.Game(screen)

ouvert = True

while ouvert:
    screen.blit(pygame.image.load("assets/default.jpg"), (0, 0))
    game.show_menu_cropfield()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ouvert = False

pygame.quit()
