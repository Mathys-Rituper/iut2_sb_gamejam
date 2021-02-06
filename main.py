import pygame

pygame.init()
pygame.display.set_caption("Game Jam 2021")
screen = pygame.display.set_mode((1024, 768))
screen.blit(pygame.image.load("assets/default.jpg"), (0, 0))

ouvert = True

while ouvert:
    for event in pygame.event.get():
        if event.type == pygame.quit():
            ouvert = False

pygame.quit()
