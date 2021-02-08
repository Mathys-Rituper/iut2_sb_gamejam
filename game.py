import pygame
import player
from field import cropfield

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.player = player.Player()
        self.field = cropfield.Cropfield(3,self)
        self.pressed = {}

    def show_menu_cropfield(self):
        self.field.field_interaction_menu().draw(self.screen)