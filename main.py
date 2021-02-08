import pygame
from game import Game

# Initialisation de pygame
pygame.init()

# Initialisation de la fenêtre
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Game Jam 2021")
background = pygame.image.load("assets/default.jpg")

game = Game(screen)
pygame.display.flip()

ouvert = True

while ouvert:

    screen.blit(background, (0, 0))

    screen.blit(game.player.image, game.player.rect)



    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT):
        game.player.move_left()
    elif game.pressed.get(pygame.K_UP):
        game.player.move_up()
    elif game.pressed.get(pygame.K_DOWN):
        game.player.move_down()

    if game.pressed.get(pygame.K_RIGHT) and game.pressed.get(pygame.K_UP):
        game.player.move_right()
        game.player.move_up()

    elif game.pressed.get(pygame.K_RIGHT) and game.pressed.get(pygame.K_DOWN):
        game.player.move_right()
        game.player.move_down()

    elif game.pressed.get(pygame.K_LEFT) and game.pressed.get(pygame.K_DOWN):
        game.player.move_left()
        game.player.move_down()

    elif game.pressed.get(pygame.K_LEFT) and game.pressed.get(pygame.K_UP):
        game.player.move_left()
        game.player.move_up()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ouvert = False

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

pygame.quit()
