import pygame
import animation
import weapons.weapons
from weapons import weapons


class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("player")

        # STATISTIQUES INGAME
        self.velocity = 6.5
        self.health = 100
        self.max_health = 100
        self.attack_speed = 1  # coefficient multiplicateur vitesse attaque
        self.attack_strength = 1  # coefficient mulitiplicateur degats
        self.last_attack = pygame.time.get_ticks()  # date de la dernière attaque
        self.resistance = 0  # pourcentage de degats reduits
        self.elapse = 0
        self.game = game
        self.weapon = weapons.Pistolet(self)
        self.damage_animation_timer =-1

        # INVENTORY
        self.veg_inv = {"P": {"name": "Potato", "amount": 1},
                        "W": {"name": "Watermelon", "amount": 10},
                        "C": {"name": "carrot", "amount": 5},
                        "S": {"name": "Strawberry", "amount": 10},
                        "N": {"name": "No Crop", "amount": 0}}
        self.weapons = {"pistol": {"owned": True, "item": weapons.Pistolet(self)},
                        "shotgun": {"owned": False, "item": weapons.Pompe(self)},"smg":{"owned":False,"item":weapons.Mitrailleuse(self)},"sniper":{"owned":False,"item":weapons.Snipe(self)}}  # Rajouter chaque nouvelle arme ici

        # SPRITE
        self.rect = self.image.get_rect()
        self.rect.x = 2341
        self.rect.y = 1902

    def attack(self):
        self.weapon.fire()

    def cd(self):
        return ((pygame.time.get_ticks() - self.last_attack) / 1000)


    def reset_cd(self):
        self.last_attack = pygame.time.get_ticks()

    def move_right(self):
        self.current_orientation = "right"
        if not self.game.essai_deplacement(self, 5, 0, self.game.wall):
            self.rect.x += self.velocity
            self.game.bouger_camera(self.velocity, 0)
        self.update()

    def move_left(self):
        self.current_orientation = "left"
        if not self.game.essai_deplacement(self, -5, 0, self.game.wall):
            self.rect.x -= self.velocity
            self.game.bouger_camera(-self.velocity, 0)
        self.update()

    def move_up(self):
        self.current_orientation = "up"
        if not self.game.essai_deplacement(self, 0, -5, self.game.wall):
            self.rect.y -= self.velocity
            self.game.bouger_camera(0, -self.velocity)
        self.update()

    def move_down(self):
        self.current_orientation = "down"
        if not self.game.essai_deplacement(self, 0, 5, self.game.wall):
            self.rect.y += self.velocity
            self.game.bouger_camera(0, self.velocity)
        self.update()

    def has_no_vegs(self):
        isempty = True
        for key in self.veg_inv.keys():
            if self.veg_inv[key]["amount"] != 0:
                isempty = False
        return isempty

    def dec_veg(self, crop):
        self.veg_inv[crop]["amount"] -= 1

    def inc_veg(self, crop):
        self.veg_inv[crop]["amount"] += 1

    def update(self):

        if pygame.time.get_ticks() - self.elapse > 100:
            self.animate()
            self.elapse = pygame.time.get_ticks()

    def reset_position(self):
        self.rect.x = 2341
        self.rect.y = 1902
        self.game.camera.x=self.rect.x + (self.rect.w / 2) - 1024 / 2
        self.game.camera.y=self.rect.y + (self.rect.h / 2) - 768 / 2



    def take_damage(self, dmg):
        self.health-=dmg
        self.damage_animation_timer = 0

    def add_weapon(self, nom_weapon):
        self.weapons[nom_weapon]["owned"] = True

    def switch_weapon(self, nom_weapon):
        if self.weapons[nom_weapon]["owned"]:
            self.weapon = self.weapons[nom_weapon]["item"]

    def update_anim_degats(self):
        colorImage = pygame.Surface(self.image.get_size()).convert_alpha()

        if 0<=self.damage_animation_timer<2:
            colorImage.fill("black")
            self.image.blit(colorImage, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            self.damage_animation_timer+=1

        elif self.damage_animation_timer >= 10:
            colorImage.fill("white")
            self.image.blit(colorImage, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            self.damage_animation_timer=-1
        elif self.damage_animation_timer != -1:
            colorImage.fill("red")
            self.image.blit(colorImage, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            self.damage_animation_timer+=1