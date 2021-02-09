import pygame
import player
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

    def essaieDeplacement(self, sprite , derection, vitesse, group):
        copy = sprite
        print("position sprite" ,sprite.y)
        if derection == 1:
            copy.x = sprite.x - vitesse
        else:
            #copy.rect.y = sprite.rect.y + vitesse
            copy.rect.h = sprite.rect.h + vitesse
           # copy.rect.y = copy.y
            print("postion copye " ,copy.rect.y)
            print("??", copy.y)
        return self.collision(copy, group)

    def getWall(self, groups):
        self.wall = groups

