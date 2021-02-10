import pygame
import pygame_menu
import player
import copy
from field import cropfield
from tile_map import *
import copy
from Monstre import Monstre
class Game():
    def __init__(self, screen):
        self.screen = screen
        self.player = player.Player(self)
        self.camera = pygame.Rect(self.player.rect.x + (self.player.rect.w/2) - 1080/2, self.player.rect.y + (self.player.rect.h/2) - 768/2,  1080,  768)
        self.field = cropfield.Cropfield(9,self)
        self.pressed = {}
        self.wall = []
        self.menu_cropfield = self.get_menu_cropfield()
        self.menu_npc = self.get_npc_menu()
        self.tab_monstre= pygame.sprite.Group()

        #self.monste = Monstre(self)


    def get_menu_cropfield(self):
        return self.field.field_interaction_menu()

        self.field.field_interaction_menu().draw(self.screen)
    def update_menu(self,events):
        self.field.field_interaction_menu().update(events)

    #def collision(self, player, group):
     #   return pygame.sprite.spritecollide(player, group, False)

    def collision(self, player, group):
        return pygame.sprite.spritecollide(player, group, False)

    def bougerCamera(self, x, y ):
        self.camera.x += x
        self.camera.y += y

    def collisionMonstre(self, monstre , group):
        return pygame.sprite.spritecollide(monstre, group, False)




    def essaieDeplacement(self, sprite , x, y, group):
        c = copy.copy(sprite)
        c.rect = copy.deepcopy(sprite.rect)
        c.rect.x = c.rect.x + x
        c.rect.y = c.rect.y + y
        return self.collision(c, group)

    def getWall(self, groups):
        self.wall = groups

    def update_menu_cropfield(self):
        self.menu_cropfield = self.get_menu_cropfield()



    def get_npc_menu(self):
        npc_menu = pygame_menu.Menu(400,1024,"Shop",columns=2,rows=6)
        head1 = npc_menu.add_label("Improve your stats !")
        #COL 1
        speed = npc_menu.add_button("Increase speed (cost : 3 carrots, current speed :" +'%.2f'%(self.player.velocity)+")",self.upgrade_speed)
        if (self.player.veg_inv["C"]["amount"]<1):
            speed.is_selectable=False
        speed.set_background_color((75,75,75))
        speed.update_font({"color":(255,255,255)})
        speed.set_padding(8)
        speed.set_max_width(450)


        max_health = npc_menu.add_button(
            "Increase max HP (cost : 3 potatos, current max HP :" + str(self.player.max_health) + ")",
            self.upgrade_hp)
        if (self.player.veg_inv["P"]["amount"] < 1):
            max_health.is_selectable = False
        max_health.set_background_color((75, 75, 75),)
        max_health.update_font({"color": (255, 255, 255)})
        max_health.set_padding(8)
        max_health.set_max_width(450)

        damage = npc_menu.add_button(
            "Increase damage (cost : 3 strawberries, current damage :" + '%.2f'%(self.player.attack_strength) + ")",
            self.upgrade_damage)
        if (self.player.veg_inv["S"]["amount"] < 1):
            damage.is_selectable = False
        damage.set_background_color((75, 75, 75), )
        damage.update_font({"color": (255, 255, 255)})
        damage.set_padding(8)
        damage.set_max_width(450)

        attack_speed = npc_menu.add_button(
            "Increase attack speed (cost : 3 watermelons, current attack speed :" + '%.2f'%(self.player.attack_speed) + ")",
            self.upgrade_atk_speed)
        if (self.player.veg_inv["W"]["amount"] < 1):
            attack_speed.is_selectable = False
        attack_speed.set_background_color((75, 75, 75), )
        attack_speed.update_font({"color": (255, 255, 255)})
        attack_speed.set_padding(8)
        attack_speed.set_max_width(450)

        npc_menu.add_button("RETURN", self.disable_menu)

        #COL 2
        head2 = npc_menu.add_label("Invest your veggies to become stronger.")
        label1 = npc_menu.add_label("Carrots in inventory : "+str(self.player.veg_inv["C"]["amount"]))
        label1.set_padding(8.8)
        label2 = npc_menu.add_label("Potatoes in inventory : " + str(self.player.veg_inv["P"]["amount"]))
        label2.set_padding(8.8)
        label3 = npc_menu.add_label("Strawberries in inventory : " + str(self.player.veg_inv["S"]["amount"]))
        label3.set_padding(8.8)
        label4 =npc_menu.add_label("Watermelons in inventory : " + str(self.player.veg_inv["W"]["amount"]))
        label4.set_padding(8.8)
        npc_menu.add_label("")

        for widget in npc_menu.get_widgets():
            widget.update_font({"size":widget.get_font_info()["size"]*0.66})

        head1.update_font({"size":widget.get_font_info()["size"]*1.25})
        head2.update_font({"size":widget.get_font_info()["size"]*1.25})


        return npc_menu

    def update_menu_npc(self):
        self.menu_npc = self.get_npc_menu()

    def upgrade_speed(self):
        if self.player.veg_inv["C"]["amount"] >0:
            self.player.velocity*=1.1
            self.player.veg_inv["C"]["amount"]-=1
        self.update_menu_npc()
        self.menu_npc.enable()

    def upgrade_hp(self):
        if self.player.veg_inv["P"]["amount"] >0:
            self.player.max_health+=20
            self.player.veg_inv["P"]["amount"]-=1
        self.update_menu_npc()
        self.menu_npc.enable()

    def upgrade_atk_speed(self):
        if self.player.veg_inv["W"]["amount"] >0:
            self.player.attack_speed+=0.1
            self.player.veg_inv["W"]["amount"]-=1
        self.update_menu_npc()
        self.menu_npc.enable()

    def upgrade_damage(self):
        if self.player.veg_inv["S"]["amount"] >0:
            self.player.attack_strength*=1.1
            self.player.veg_inv["S"]["amount"]-=1
        self.update_menu_npc()
        self.menu_npc.enable()

    def disable_menu(self):
        self.update_menu_npc()
        self.menu_npc.disable()
    def addMonstre(self):

        m = Monstre(self)

        self.tab_monstre.add(m)
