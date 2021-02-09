import pygame
import player
import copy
from field import cropfield

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.player = player.Player(self)
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





    def essaieDeplacement(self, sprite , x, y, group):
        c = copy.copy(sprite)
        c.rect = copy.deepcopy(sprite.rect)
        c.rect.x = c.rect.x + x
        c.rect.y = c.rect.y + y
        print("origine x " ,sprite.rect.x)
        print("coy x ", c.rect.x)
        return self.collision(c, group)

    def getWall(self, groups):
        self.wall = groups

