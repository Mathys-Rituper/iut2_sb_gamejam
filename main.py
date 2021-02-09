import pygame
from game import Game
from tile_map import Tile_map
from setting import *
from sprite import *
import pytmx
# Initialisation de pygame
from player import Player
pygame.init()

# Initialisation de la fenêtre
screen = pygame.display.set_mode((WIDTH_TILE*NB_TILE_X, HEIGHT_TILE*NB_TILE_Y)) #1080, 768
pygame.display.set_caption("Game Jam 2021")
background = pygame.image.load("assets/default.jpg")

game = Game(screen)
pygame.display.flip()

ouvert = True

tile = Tile_map()
map_image = tile.make_map()

#Definitioon d'une clock
clock = pygame.time.Clock()
FPS = 60
wall = []
for tile_object in tile.tmx.objects:
    if tile_object.name == 'maison':
       wall.append(Obstacle(tile, tile_object.x, tile_object.y, tile_object.width, tile_object.height))
    if tile_object.name == 'rocher':
       wall.append(Obstacle(tile, tile_object.x, tile_object.y, tile_object.width, tile_object.height))

game.getWall(wall)

while ouvert:
    #screen.blit(background, (0, 0))
    screen.blit(map_image, (0, 0))
    screen.blit(game.player.image, game.player.rect)

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x <= WIDTH_TILE*NB_TILE_X - game.player.rect.w:

        game.player.move_right()
    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x >= 0 :
            game.player.move_left()
    if game.pressed.get(pygame.K_UP) and game.player.rect.y > 0 :

            game.player.move_up()
    if game.pressed.get(pygame.K_DOWN) and game.player.rect.y < HEIGHT_TILE * NB_TILE_Y - game.player.rect.h :

            game.player.move_down()

    """" if game.pressed.get(pygame.K_RIGHT) and game.pressed.get(pygame.K_UP):
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
         game.player.move_up()"""

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ouvert = False

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

    clock.tick(FPS)
pygame.quit()
