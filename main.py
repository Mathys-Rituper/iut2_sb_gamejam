from game import Game
from tile_map import Tile_map
from setting import *
from sprite import *
import copy
import pytmx
import pygame_menu

# Initialisation de pygame
pygame.init()

# Initialisation de la fenêtre
screen = pygame.display.set_mode((1080, 768))  # 1080, 768
pygame.display.set_caption("Game Jam 2021")
background = pygame.image.load("assets/default.jpg")

main_running = True
is_a_menu_open = False

tile = Tile_map()
map_image = tile.make_map()

game = Game(map_image)
game.menu_cropfield.disable()

pygame.display.flip()
# Definitioon d'une clock
clock = pygame.time.Clock()
FPS = 60

spots = []
wall = []
for tile_object in tile.tmx.objects:
    if tile_object.name.startswith('obstacle'):
        wall.append(Obstacle(tile, tile_object.x, tile_object.y, tile_object.width, tile_object.height))
    if tile_object.name.startswith('spot'):
        spots.append(tile_object)


def render_field():
    assert len(game.field.spots) == len(spots)
    for i in range(len(game.field.spots)):
        world_image.blit(game.field.spots[i].image, (spots[i].x, spots[i].y))


game.getWall(wall)

while main_running:

    world_image = pygame.Surface((WIDTH_TILE * NB_TILE_X, HEIGHT_TILE * NB_TILE_Y))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            main_running = False
        elif event.type == pygame.KEYUP and event.key == pygame.K_e:
            game.field.croissance()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        if event.type == pygame_menu.events.BACK or event.type == pygame_menu.events.CLOSE:
            game.update_menu_cropfield()

    if not is_a_menu_open:
        world_image.blit(map_image, (0, 0))
        render_field()

        for projectile in game.projectiles:
            projectile.move()
            world_image.blit(projectile.image, (projectile.rect.x, projectile.rect.y))

        screen.blit(world_image, (0, 0), game.camera)

        screen.blit(game.player.image, ((1080 - game.player.rect.w) / 2, (768 - game.player.rect.h) / 2))
        pygame.display.flip()

        if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x <= WIDTH_TILE * NB_TILE_X - game.player.rect.w:
            game.player.move_right()
        if game.pressed.get(pygame.K_LEFT) and game.player.rect.x >= 0:
            game.player.move_left()
        if game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
            game.player.move_up()
        if game.pressed.get(pygame.K_DOWN) and game.player.rect.y < HEIGHT_TILE * NB_TILE_Y - game.player.rect.h:
            game.player.move_down()
        if game.pressed.get(pygame.K_SPACE):
            game.player.attack()
        elif game.pressed.get(pygame.K_a):
            print("nouveau rendu du menu, inventaire :", game.player.veg_inv)
            game.update_menu_cropfield()
            game.menu_cropfield.enable()
            is_a_menu_open = True


    elif game.menu_cropfield.is_enabled():  # Si le menu du champ est ouvert
        game.menu_cropfield.update(events)
        if game.menu_cropfield.is_enabled():
            game.menu_cropfield.draw(screen)
        if game.pressed.get(pygame.K_ESCAPE):
            game.menu_cropfield.disable()
            is_a_menu_open = False
    else:
        is_a_menu_open = False  # Si tous les menus sont fermés, alors on est plus dans un menu

  #  pygame.display.flip()

    clock.tick(FPS)
pygame.quit()
