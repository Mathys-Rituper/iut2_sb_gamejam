import pygame

#Initialisation de pygame
pygame.init()

#Initialisation de la fenêtre
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Game Jam 2021")


screen.blit(pygame.image.load("assets/default.jpg"), (0, 0))

pygame.display.flip()

ouvert = True

while ouvert:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ouvert = False

pygame.quit()
