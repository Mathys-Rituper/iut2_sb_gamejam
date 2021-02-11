from game import Game
from sprite import *
import pygame_menu
import pygame
import copy

# Initialisation de pygame
pygame.init()
main_running = True

# Initialisation de la fenêtre
screen = pygame.display.set_mode((1024, 768))  # 1080, 768
pygame.display.set_caption("Game Jam 2021")
world_image = pygame.Surface((WIDTH_TILE * NB_TILE_X, HEIGHT_TILE * NB_TILE_Y))

# Gestion de la map
tile = TileMap()
map_image = tile.make_map()
game = Game(map_image)
spots = []
wall = []



for tile_object in tile.tmx.objects:
    if tile_object.name.startswith('obstacle'):
        wall.append(Obstacle(tile, tile_object.x, tile_object.y, tile_object.width, tile_object.height))
    if tile_object.name.startswith('spot'):
        spots.append(tile_object)
    if tile_object.name.startswith('spawn'):
        game.spawn.append(tile_object)
game.get_wall(wall)
groupM = []

# Gestion des menus
game.menu_cropfield.disable()
game.menu_npc.disable()
game.menu_shop.disable()

# premier affichage
pygame.display.flip()

# Definitioon d'une clock
clock = pygame.time.Clock()
FPS = 60


def menus():
    game.menu_principal.enable()
    menus_open = True
    while menus_open:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                menus_open = False
                pygame.quit()
        game.menu_principal.update(events)
        if game.menu_principal.is_enabled():
            game.menu_principal.draw(screen)
        else:
            menus_open = False
        pygame.display.flip()


def main_game(running):
    is_a_menu_open = False
    while running:

        world_image = pygame.Surface((WIDTH_TILE * NB_TILE_X, HEIGHT_TILE * NB_TILE_Y))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP and event.key == pygame.K_e:
                game.field.croissance()
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True

                if event.key == pygame.K_w:
                    game.add_monstre()

                    copyT = copy.copy(game.tab_monstre)

            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
            if event.type == pygame_menu.events.BACK or event.type == pygame_menu.events.CLOSE:
                game.update_menu_cropfield()

        if not is_a_menu_open:

            # screen.blit(game.monste.image,game.monste.rect)
            # game.tab_monstre.draw(screen)

            # mouvement monstre
            # for m in game.tab_monstre:
            # m.mouvement(game.player.rect.x, game.player.rect.y)
            for m in game.tab_monstre:
                for k in game.tab_monstre:
                    if k != m:
                        groupM.append(k)
                m.mouvement(game.player.rect.x, game.player.rect.y, groupM)

                for k in game.tab_monstre:
                    if k != m:
                        groupM.remove(k)

            world_image.blit(map_image, (0, 0))

            # Affichage des crops sur le champ
            assert len(game.field.spots) == len(spots)
            for i in range(len(game.field.spots)):
                world_image.blit(game.field.spots[i].image, (spots[i].x, spots[i].y))

            for projectile in game.projectiles:
                projectile.move()
                world_image.blit(projectile.image, (projectile.rect.x, projectile.rect.y))
                pygame.display.flip()

            for monster in game.tab_monstre:
                # gestion monstres

                world_image.blit(monster.image, monster.rect)

            screen.blit(world_image, (0, 0), game.camera)
            game.player.update_anim_degats()
            screen.blit(game.player.image, ((1024 - game.player.rect.w) / 2, (768 - game.player.rect.h) / 2))

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
                game.update_menu_cropfield()
                game.menu_cropfield.enable()
                is_a_menu_open = True
            elif game.pressed.get(pygame.K_e):
                game.update_menu_npc()
                game.menu_npc.enable()
                is_a_menu_open = True
                game.pressed[pygame.K_e] = False
            elif game.pressed.get(pygame.K_r):
                game.update_menu_shop()
                game.menu_shop.enable()
                is_a_menu_open = True
                game.pressed[pygame.K_r] = False

        elif game.menu_cropfield.is_enabled():  # Si le menu du champ est ouvert
            game.menu_cropfield.update(events)
            if game.menu_cropfield.is_enabled():  # car le dernier event peut avoir désactivé le menu, il ne serait alors
                # plus dessinable
                game.menu_cropfield.draw(screen)
            if game.pressed.get(pygame.K_ESCAPE):
                game.menu_cropfield.disable()
                is_a_menu_open = False

        elif game.menu_npc.is_enabled():  # Si le menu du NPC Shop est ouvert
            game.menu_npc.update(events)
            if game.menu_npc.is_enabled():
                game.menu_npc.draw(screen)
            if game.pressed.get(pygame.K_ESCAPE):
                game.menu_npc.disable()
                is_a_menu_open = False
        elif game.menu_shop.is_enabled():
            game.menu_shop.update(events)
            if game.menu_shop.is_enabled():
                game.menu_shop.draw(screen)
            if game.pressed.get(pygame.K_ESCAPE):
                game.menu_shop.disable()
                is_a_menu_open = False
        else:
            is_a_menu_open = False  # Si tous les menus sont fermés, alors on est plus dans un menu

        pygame.display.flip()

        clock.tick(FPS)
    pygame.quit()


menus()  # Commence par ouvrir les menus
main_running = True  # Ouvrir le jeu en lançant le menu principal
main_game(main_running)
