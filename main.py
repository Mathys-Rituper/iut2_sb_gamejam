from game import Game
from tile_map import Tile_map
from setting import *
from sprite import *
import pytmx
# Initialisation de pygame
pygame.init()

# Initialisation de la fenêtre
screen = pygame.display.set_mode((1080,768)) #1080, 768
pygame.display.set_caption("Game Jam 2021")
background = pygame.image.load("assets/default.jpg")



main_running = True
is_a_menu_open = False

tile = Tile_map()
map_image = tile.make_map()

game = Game(map_image)
menu_cropfield = game.get_menu_cropfield()
menu_cropfield.disable()

pygame.display.flip()
#Definitioon d'une clock
clock = pygame.time.Clock()
FPS = 60

wall = []
for tile_object in tile.tmx.objects:
    if tile_object.name.startswith('obstacle'):
       wall.append(Obstacle(tile, tile_object.x, tile_object.y, tile_object.width, tile_object.height))

game.getWall(wall)

while main_running:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            main_running = False

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

    if not is_a_menu_open:

        screen.blit(map_image, (0, 0), game.camera)
        screen.blit(game.player.image, ( (1080-game.player.rect.w)/2 , (768-game.player.rect.h)/2) )
        for projectile in game.player.all_projectiles:
            projectile.move()

        #  map_image.blit(projectile.image, (projectile.rect.x, projectile.rect.y))


      #  game.player.all_projectiles.draw(map_image)

        if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x <= WIDTH_TILE*NB_TILE_X - game.player.rect.w:

            game.player.move_right()
        if game.pressed.get(pygame.K_LEFT) and game.player.rect.x >= 0 :
                game.player.move_left()
        if game.pressed.get(pygame.K_UP) and game.player.rect.y > 0 :
                game.player.move_up()
        if game.pressed.get(pygame.K_DOWN) and game.player.rect.y < HEIGHT_TILE * NB_TILE_Y - game.player.rect.h :
                game.player.move_down()
        if game.pressed.get(pygame.K_SPACE):
            game.player.launch_projectile()
        elif game.pressed.get(pygame.K_a):
            menu_cropfield.enable()
            is_a_menu_open = True


    elif menu_cropfield.is_enabled():  # Si le menu du champ est ouvert
        menu_cropfield.render()
        menu_cropfield.update(events)
        menu_cropfield.draw(screen)
        if game.pressed.get(pygame.K_ESCAPE):
            menu_cropfield.disable()
            is_a_menu_open = False
    else:
        is_a_menu_open = False  # Si tous les menus sont fermés, alors on est plus dans un menu


    pygame.display.flip()



    clock.tick(FPS)
pygame.quit()
