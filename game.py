import pygame
import player
from field import cropfield
import pygame_menu

from tile_map import *
import copy
from Monstre import *
import  random


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player = player.Player(self)
        self.camera = pygame.Rect(self.player.rect.x + (self.player.rect.w / 2) - 1024 / 2,
                                  self.player.rect.y + (self.player.rect.h / 2) - 768 / 2, 1024, 768)
        self.field = cropfield.Cropfield(9, self)
        self.pressed = {}
        self.wall = []
        self.menu_cropfield = self.get_menu_cropfield()
        self.menu_npc = self.get_npc_menu()
        self.tab_monstre = pygame.sprite.Group()
        self.menu_shop = self.get_shop_menu()
        self.menu_principal = self.get_menu_principal()
        self.menu_credits = self.get_menu_credits
        self.get_menu_regles()
        self.spawn = []
        self.projectiles = pygame.sprite.Group()

        #font
        self.font = pygame.font.SysFont('Comix Sans MS', 30)
        self.miniF = pygame.image.load('assets/Monstre/monstre1.png')
        self.miniPs = pygame.image.load('assets/Monstre/monstre2.png')
        self.miniC = pygame.image.load('assets/Monstre/monstre3.png')
        self.miniPa = pygame.image.load('assets/Monstre/monstre4.png')

        self.miniF = pygame.transform.scale(self.miniF,(30,30))
        self.miniPs = pygame.transform.scale(self.miniPs, (30, 30))
        self.miniC = pygame.transform.scale(self.miniC, (30, 30))
        self.miniPa = pygame.transform.scale(self.miniPa, (30, 30))


    def get_menu_cropfield(self):
        return self.field.field_interaction_menu()

    def update_menu(self, events):
        self.field.field_interaction_menu().update(events)

    def collision(self, player, group):
        return pygame.sprite.spritecollide(player, group, False)
       # return pygame.sprite.spritecollideany(player, group)

    def bouger_camera(self, x, y):
        self.camera.x += x
        self.camera.y += y

    def collision_monstre(self, monstre, group):
        return pygame.sprite.spritecollide(monstre, group, False)

    def essai_deplacement(self, sprite, x, y, group):
        c = copy.copy(sprite)
        c.rect = copy.deepcopy(sprite.rect)
        c.rect.x = c.rect.x + x
        c.rect.y = c.rect.y + y
        return self.collision(c, group)

    def get_wall(self, groups):
        self.wall = groups

    def update_menu_cropfield(self):
        self.menu_cropfield = self.get_menu_cropfield()

    def get_npc_menu(self):
        npc_menu = pygame_menu.Menu(400, 1024, "Shop", columns=2, rows=6, theme=pygame_menu.themes.THEME_DARK)
        head1 = npc_menu.add_label("Improve your stats !")
        # COL 1
        speed = npc_menu.add_button(
            "Increase speed (cost : 3 carrots, current speed :" + '%.2f' % (self.player.velocity) + ")",
            self.upgrade_speed)
        if self.player.veg_inv["C"]["amount"] < 3:
            speed.is_selectable = False
        speed.set_background_color((75, 75, 75))
        speed.update_font({"color": (255, 255, 255)})
        speed.set_padding(8)
        speed.set_max_width(450)

        max_health = npc_menu.add_button(
            "Increase max HP (cost : 3 potatos, current max HP :" + str(self.player.max_health) + ")",
            self.upgrade_hp)
        if self.player.veg_inv["P"]["amount"] < 3:
            max_health.is_selectable = False
        max_health.set_background_color((75, 75, 75), )
        max_health.update_font({"color": (255, 255, 255)})
        max_health.set_padding(8)
        max_health.set_max_width(450)

        damage = npc_menu.add_button(
            "Increase damage (cost : 3 strawberries, current damage :" + '%.2f' % (self.player.attack_strength) + ")",
            self.upgrade_damage)
        if self.player.veg_inv["S"]["amount"] < 3:
            damage.is_selectable = False
        damage.set_background_color((75, 75, 75), )
        damage.update_font({"color": (255, 255, 255)})
        damage.set_padding(8)
        damage.set_max_width(450)

        attack_speed = npc_menu.add_button(
            "Increase attack speed (cost : 3 watermelons, current attack speed :" + '%.2f' % (
                self.player.attack_speed) + ")",
            self.upgrade_atk_speed)
        if self.player.veg_inv["W"]["amount"] < 3:
            attack_speed.is_selectable = False
        attack_speed.set_background_color((75, 75, 75), )
        attack_speed.update_font({"color": (255, 255, 255)})
        attack_speed.set_padding(8)
        attack_speed.set_max_width(450)

        npc_menu.add_button("RETURN", self.disable_menu_npc)

        # COL 2
        head2 = npc_menu.add_label("Invest your veggies to become stronger.")
        label1 = npc_menu.add_label("Carrots in inventory : " + str(self.player.veg_inv["C"]["amount"]))
        label1.set_padding(8.8)
        label2 = npc_menu.add_label("Potatoes in inventory : " + str(self.player.veg_inv["P"]["amount"]))
        label2.set_padding(8.8)
        label3 = npc_menu.add_label("Strawberries in inventory : " + str(self.player.veg_inv["S"]["amount"]))
        label3.set_padding(8.8)
        label4 = npc_menu.add_label("Watermelons in inventory : " + str(self.player.veg_inv["W"]["amount"]))
        label4.set_padding(8.8)
        npc_menu.add_label("")

        for widget in npc_menu.get_widgets():
            widget.update_font({"size": widget.get_font_info()["size"] * 0.66})

        head1.update_font({"size": head1.get_font_info()["size"] * 1.25})
        head2.update_font({"size": head2.get_font_info()["size"] * 1.25})

        return npc_menu

    def update_menu_npc(self):
        self.menu_npc = self.get_npc_menu()

    def upgrade_speed(self):
        if self.player.veg_inv["C"]["amount"] > 2:
            self.player.velocity *= 1.1
            self.player.veg_inv["C"]["amount"] -= 3
        self.update_menu_npc()
        self.menu_npc.enable()

    def upgrade_hp(self):
        if self.player.veg_inv["P"]["amount"] > 2:
            self.player.max_health += 20
            self.player.veg_inv["P"]["amount"] -= 3
        self.update_menu_npc()
        self.menu_npc.enable()

    def upgrade_atk_speed(self):
        if self.player.veg_inv["W"]["amount"] > 2:
            self.player.attack_speed += 0.2
            self.player.veg_inv["W"]["amount"] -= 3
        self.update_menu_npc()
        self.menu_npc.enable()

    def upgrade_damage(self):
        if self.player.veg_inv["S"]["amount"] > 2:
            self.player.attack_strength *= 1.3
            self.player.veg_inv["S"]["amount"] -= 3
        self.update_menu_npc()
        self.menu_npc.enable()

    def disable_menu_npc(self):
        self.update_menu_npc()
        self.menu_npc.disable()

    def add_monstre(self):

        m = Monstre(self)
        self.tab_monstre.add(m)

    def get_shop_menu(self):
        menu_shop = pygame_menu.Menu(300, 1024, "Weapons", rows=4, columns=2, theme=pygame_menu.themes.THEME_DARK)

        # COL 1

        # header
        head1 = menu_shop.add_label("Buy and switch weapons !")
        head1.update_font({"size": head1.get_font_info()["size"] * 1.25})

        # pistol
        button_pistol = menu_shop.add_button("Pistol (owned)", self.change_player_weapon, "pistol")
        button_pistol.set_background_color((75, 75, 75), )
        button_pistol.update_font({"color": (255, 255, 255)})
        button_pistol.set_padding(8)
        button_pistol.set_max_width(450)

        # Pompe
        if self.player.weapons["shotgun"]["owned"]:
            button_pompe = menu_shop.add_button("Shotgun (owned)", self.change_player_weapon, "shotgun")
        else:
            button_pompe = menu_shop.add_button("Shotgun (10 strawberries, 10 watermelons)", self.buy_weapon, "shotgun",
                                                0, 0, 10, 10)
            if self.player.veg_inv["S"]["amount"] < 10 and self.player.veg_inv["W"]["amount"] < 10:
                button_pompe.is_selectable = False
        button_pompe.set_background_color((75, 75, 75), )
        button_pompe.update_font({"color": (255, 255, 255)})
        button_pompe.set_padding(8)
        button_pompe.set_max_width(450)

        # Return
        button_return = menu_shop.add_button("Return", self.disable_menu_shop)
        button_return.set_background_color((75, 75, 75), )
        button_return.update_font({"color": (255, 255, 255)})
        button_return.set_padding(8)
        button_return.set_max_width(450)

        # COL 2

        # head
        head2 = menu_shop.add_label("Current inventory :")
        head2.update_font({"size": head2.get_font_info()["size"] * 1.25})

        # strawberries
        label_strawberries = menu_shop.add_label("Strawberries : " + str(self.player.veg_inv['S']["amount"]))
        label_strawberries.set_padding(8.8)

        # waterlemons
        label_watermelons = menu_shop.add_label("Watermelons : " + str(self.player.veg_inv['S']["amount"]))
        label_watermelons.set_padding(8.8)

        # empty to finish grid
        menu_shop.add_label("")

        return menu_shop

    def update_menu_shop(self):
        self.menu_shop = self.get_shop_menu()

    def change_player_weapon(self, nom_weapon):
        self.player.switch_weapon(nom_weapon)
        self.disable_menu_shop()

    def disable_menu_shop(self):
        self.update_menu_shop()
        self.menu_shop.disable()

    def buy_weapon(self, nom_weapon, carrot, potato, strawberry, watermelon):
        if self.player.veg_inv["C"]["amount"] >= carrot and self.player.veg_inv["P"]["amount"] >= potato and \
                self.player.veg_inv["S"]["amount"] >= strawberry and self.player.veg_inv["W"]["amount"] >= watermelon:
            self.player.veg_inv["P"]["amount"] -= potato
            self.player.veg_inv["S"]["amount"] -= strawberry
            self.player.veg_inv["W"]["amount"] -= watermelon
            self.player.add_weapon(nom_weapon)
            self.player.switch_weapon(nom_weapon)
        self.disable_menu_shop()

    def get_menu_principal(self):
        menu = pygame_menu.Menu(768, 1024, "Potager assiégé", pygame_menu.themes.THEME_DARK)
        menu.add_label("Main menu", "label-top")
        label_top = menu.get_widget("label-top")
        label_top.update_font({"size":label_top.get_font_info()["size"]*1.3})
        menu.add_button("Play", self.jouer)
        menu.add_button("Rules", self.get_menu_regles())
        menu.add_button("Credits", self.get_menu_credits())

        menu.disable()
        return menu


    def jouer(self):
        self.menu_principal.disable()

    def get_menu_regles(self):
        regles_menu = pygame_menu.Menu(768, 1000, "Rules", pygame_menu.themes.THEME_DARK)
        regles_menu.add_label("How to play", "label-top")
        label_top = regles_menu.get_widget("label-top")
        label_top.update_font({"size": label_top.get_font_info()["size"] * 0.66})
        label_regles = "Defend your village and your cultures against the evil vegetable-monsters during the night. The aim of the game is to go through the 10 night phases with as many remaining vegetables as possible in your inventory. You can improve your stats and weapons, as well as get better yield using the field"
        label_touches = "Keys : Move around with the arrow keys, shoot with space, interact with the field and shops with Shift"


        regles_menu.add_label(label_regles, max_char=-1, font_size=15)
        regles_menu.add_label(label_touches, max_char=-1, font_size=15)
        regles_menu.add_button("RETURN", pygame_menu.events.BACK)


        return regles_menu



    def get_menu_credits(self):
        credits_menu = pygame_menu.Menu(768, 1000, "Credits", pygame_menu.themes.THEME_DARK)
        credits_menu.add_label("Credits", "label-top")
        label_top = credits_menu.get_widget("label-top")
        label_top.update_font({"size": label_top.get_font_info()["size"] * 0.66})
        label_credit_developpers = "Game Developpers : Lucas Arsicaud, Jonathan Charlassier, Mathys Rituper, Mael Veyrat"
        label_credit_crops = "Fruits and vegetable crops : [LPC] Crops by bluecarrot16, Daniel Eddeland (daneeklu), Joshua Taylor, Richard Kettering (Jetrel)."
        label_credit_fruits = "Fruits and Vegetables : [Pixel Art Food] by AnarchisedLUTE"
        label_credit_decor = "Decor : [LPC] Decorations Medieval by Lanea Zimmerman, Tuomo Untinen, Xenodora, Sharm, Johann C, Johannes Sjölund, Casper Nilsson, Daniel Cook, Rayane Félix, Wolthera van Hövell tot Westerflier,  Zachariah Husiar  & Clint Bellanger"
        label_credit_sound = "Music by Lucas Arsicaud, SFX by Jonathan Charlassier and Mael Veyrat"

        credits_menu.add_label(label_credit_developpers,max_char=-1,font_size=15)
        credits_menu.add_label(label_credit_crops,max_char=-1,font_size=15)
        credits_menu.add_label(label_credit_fruits,max_char=-1,font_size=15)
        credits_menu.add_label(label_credit_decor,max_char=-1,font_size=15)
        credits_menu.add_label(label_credit_sound,max_char=-1,font_size=15)
        credits_menu.add_button("RETURN", pygame_menu.events.BACK)
        return credits_menu


    def jour(self):
        pygame.mixer.music.load('assets/sounds/Arpeggios_Chill_100BPM.mp3')
        pygame.mixer.music.play(-1)
        # musique jour
        # apparence jour
        # disponibilité pnj
        # relier timer




    def nuit(self):
        pass
        # musique nuit
        # apparence nuit
        # disponibilité monstre
        # déclencher jour quand tous les monstres sont tués

    #def textMonstre(self):

    def Affichage_Nb_Jours(self):

        nb_jour = self.font.render(" jours : 1 / 10", True, (0, 0, 0))
        return  nb_jour

    def Affichage_Text_Nuit_Monstre(self):
        text_nb_monstreTT = self.font.render(str(len(self.tab_monstre)) + "  Monstres vivants", True, (0, 0, 0))
        return text_nb_monstreTT

    def affichageInventaire(self):

        imageFraise = pygame.image.load("assets/Monstre/monstre1.png").convert()
        imageFraise = pygame.transform.scale(imageFraise,(20,20))
        txt = self.font.render('mon cul', True,(0,0,0))
        imageFraise
        sF = self.miniF + txt
        return sF

    def AfficheFraiseTxt(self):
        txt = self.font.render(str(self.player.veg_inv['S']["amount"]), True, (0, 0, 0))
        return txt

    def AffichePastequeTxt(self):
        txt = self.font.render(str(self.player.veg_inv['W']["amount"]), True, (0, 0, 0))
        return txt

    def AfficheCarotteTxt(self):
        txt = self.font.render(str(self.player.veg_inv['C']["amount"]), True, (0, 0, 0))
        return txt


    def AffichePommeTTxt(self):
        txt = self.font.render(str(self.player.veg_inv['P']["amount"]), True, (0, 0, 0))
        return txt


