from game import Game
from sprite import *
import pygame_menu
import pygame
import copy

# Initialisation de pygame
pygame.init()
#Gestoin font
pygame.font.init()

main_running = True

# Initialisation de la fenêtre
screen = pygame.display.set_mode((1024, 768))  # 1080, 768
pygame.display.set_caption("Game Jam 2021")
world_image = pygame.Surface((WIDTH_TILE * NB_TILE_X, HEIGHT_TILE * NB_TILE_Y))

# Gestion de la map
tile = TileMap()
map_image = tile.make_map()
image_npc1 = pygame.image.load("assets/npc-oldman1.png")
game = Game(map_image)

filterNight = pygame.Surface(world_image.get_size()).convert_alpha()
filterNight.fill("dark blue")
filterNight.set_alpha(150)
map_image_night = copy.copy(map_image)
map_image_night.blit(filterNight, (0, 0))

for tile_object in tile.tmx.objects:
    if tile_object.name.startswith('obstacle'):
        game.wall.append(Obstacle(tile, tile_object.x, tile_object.y, tile_object.width, tile_object.height))
    elif tile_object.name.startswith('spot'):
        game.spots.append(tile_object)
    elif tile_object.name.startswith('spawn'):
        game.spawn.append(tile_object)
    elif tile_object.name.startswith('pnj1'):
        game.pnj1.append(Place(tile, tile_object.x, tile_object.y, tile_object.width, tile_object.height))
    elif tile_object.name.startswith('pnj2'):
        game.pnj2.append(Place(tile, tile_object.x, tile_object.y, tile_object.width, tile_object.height))
    elif tile_object.name.startswith('champ'):
        game.champ.append(Place(tile, tile_object.x, tile_object.y, tile_object.width, tile_object.height))
game.get_wall(game.wall)

# Gestion des menus-
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

        game.next_phase()

        world_image = pygame.Surface((WIDTH_TILE * NB_TILE_X, HEIGHT_TILE * NB_TILE_Y))

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
            if event.type == pygame_menu.events.BACK or event.type == pygame_menu.events.CLOSE:
                game.update_menu_cropfield()

     #

        if game.phase == "nuit":
            world_image.blit(map_image_night, (0, 0))  # nouveau calque
        else:
            world_image.blit(map_image, (0, 0))  # nouveau calque

        # Affichage des crops sur le champ
        assert len(game.field.spots) == len(game.spots)
        for i in range(len(game.field.spots)):
            world_image.blit(game.field.spots[i].image, (game.spots[i].x, game.spots[i].y))

        # Affichage des PNJs
        if (game.phase == "jour"):
            world_image.blit(image_npc1, (80 * 32, 47 * 32))
            world_image.blit(image_npc1, (92 * 32, 54 * 32))

        elif game.phase == "nuit":

            game.monsters_move()

            for projectile in game.projectiles:  # logique des projectiles puis rendering
                projectile.move()
                world_image.blit(projectile.image, (projectile.rect.x, projectile.rect.y))
                pygame.display.flip()

            for monster in game.tab_monstre:  # rendering
                # gestion monstres
                monster.update_anim_degats()
                world_image.blit(monster.image, monster.rect)

        screen.blit(world_image, (0, 0), game.camera)
        game.player.update_anim_degats()
        # Habillage écran
        # Texte
        screen.blit(game.Affichage_Nb_Jours(), (0, 0))
        screen.blit(game.Affichage_Text_Nuit_Monstre(), (750, 0))
        # Inventaire Fraise
        screen.blit(game.miniF, (10, 100))
        screen.blit(game.AfficheFraiseTxt(), (50, 110))
        # Inventaire Pasteque
        screen.blit(game.miniPs, (10, 150))
        screen.blit(game.AffichePastequeTxt(), (50, 160))
        screen.blit(game.player.image, ((1024 - game.player.rect.w) / 2, (768 - game.player.rect.h) / 2))
        # Inventaire Carotte
        screen.blit(game.miniC, (10, 200))
        screen.blit(game.AfficheCarotteTxt(), (50, 210))
        # Inventaire patate
                # Inventaire Fraise
        screen.blit(game.miniPa, (10, 250))
        screen.blit(game.AffichePommeTTxt(), (50, 260))
        screen.blit(game.affiche_hp(), (520, 0))
        screen.blit(game.img_heart, ((490, 1)))

        game.phase_over()
        if not is_a_menu_open:
            if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x <= WIDTH_TILE * NB_TILE_X - game.player.rect.w:
                game.player.move_right()
            if game.pressed.get(pygame.K_LEFT) and game.player.rect.x >= 0:
                game.player.move_left()
            if game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
                game.player.move_up()
            if game.pressed.get(pygame.K_DOWN) and game.player.rect.y < HEIGHT_TILE * NB_TILE_Y - game.player.rect.h:
                game.player.move_down()
            if game.pressed.get(pygame.K_SPACE):
                if game.phase=="nuit":
                    game.player.attack()
            if game.pressed.get(pygame.K_RSHIFT):
                if game.collision(game.player,game.champ):
                    game.update_menu_cropfield()
                    game.menu_cropfield.enable()
                    is_a_menu_open = True
                elif game.collision(game.player,game.pnj1):
                    game.update_menu_npc()
                    game.menu_npc.enable()
                    is_a_menu_open = True
                elif game.collision(game.player, game.pnj2):
                    game.update_menu_shop()
                    game.menu_shop.enable()
                    is_a_menu_open = True
                    game.pressed[pygame.K_r] = False

        if game.menu_cropfield.is_enabled():  # Si le menu du champ est ouvert
            game.menu_cropfield.update(events)
            if game.menu_cropfield.is_enabled():  # car le dernier event peut avoir désactivé le menu, il ne serait
                # alors
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
game.phase = "jour"
main_running = True  # Ouvrir le jeu en lançant le menu principal
main_game(main_running)
