import pygame
import player
import copy
from field import cropfield

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.player = player.Player(self)
        self.camera = pygame.Rect(self.player.rect.x + (self.player.rect.w/2) - 1080/2, self.player.rect.y - (self.player.rect.h/2) + 768/2,  1080,  768)
        self.field = cropfield.Cropfield(9,self)
        self.pressed = {}
        self.wall = []


    def get_menu_cropfield(self):
        return self.field.field_interaction_menu()

        self.field.field_interaction_menu().draw(self.screen)
    def update_menu(self,events):
        self.field.field_interaction_menu().update(events)

    def collision(self, player, group):
        return pygame.sprite.spritecollide(player, group, False)

    def collision(self, player, group):
        return pygame.sprite.spritecollide(player, group, False)

    def bougerCamera(self, x, y ):
        self.camera.x += x
        self.camera.y += y




    def essaieDeplacement(self, sprite , x, y, group):
        c = copy.copy(sprite)
        c.rect = copy.deepcopy(sprite.rect)
        c.rect.x = c.rect.x + x
        c.rect.y = c.rect.y + y
        return self.collision(c, group)

    def getWall(self, groups):
        self.wall = groups

