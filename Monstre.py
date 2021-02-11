import pygame
import random
import threading
class Monstre(pygame.sprite.Sprite ):
    def __init__(self, game ):
        super().__init__()
        self.hp = 10
        self.dmg = 10
        self.cd = 1
        self.last_attack = pygame.time.get_ticks()
        self.vitessex = 4
        self.vitessey = 4
        self.game = game
        self.num = str(random.randint(1,4))
        self.ModifStat()
        self.image = pygame.image.load('assets/Monstre/monstre'+self.num+'.png')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.damage_animation_timer = -1
        self.rect = pygame.Rect(self.image.get_rect().x, self.image.get_rect().y, 30,30)#self.image.get_rect()


        self.defineSpawn()
        self.check = 0;
        self.col = False
        self.subpos = 0

        #stat qui bouger
        #PommeT tanky
        #carrote speed
        #Fraise normal
        #Pasteque ?




    def mouvement(self, posx, posy , group ):

        dx = posx - self.rect.x
        dy = posy - self.rect.y
        # for all item in groupe teste collision
        dir = self.max(dx, dy)

        if dir ==1 and dx >= 0:
            self.animation = True
            if not self.game.essai_deplacement(self, self.vitessex, 0 , group):
                if not self.game.essai_deplacement(self, self.vitessex, 0, self.game.wall)  :
                    self.rect.x += self.vitessex
                    self.col = False
                else:
                    if not self.col:
                        i = random.randint(1,2)
                        self.col = True

                        if i  == 1:#dy > 0:
                            self.subpos = -self.vitessey
                        else:
                             #self.rect.y -= self.vitessey
                             self.subpos = self.vitessey
                    self.rect.y += self.subpos

        if dir ==1 and dx < 0:
            if not self.game.essai_deplacement(self, -self.vitessex, 0, group):
                if not self.game.essai_deplacement(self, -self.vitessex, 0, self.game.wall):
                    self.rect.x -= self.vitessex
                    self.col = False
                else :
                    if not self.col:
                        i = random.randint(1, 2)
                        self.col = True
                        if i == 1:  # dy > 0:
                            self.subpos = -self.vitessey
                        else:
                            self.subpos = self.vitessey

                    self.rect.y += self.subpos

        if dir ==2 and dy >= 0:
            if not self.game.essai_deplacement(self, 0, self.vitessex, group):
                if not self.game.essai_deplacement(self, 0, self.vitessex, self.game.wall)  :
                    self.rect.y += self.vitessex
                    self.col = False
                else :
                    if not self.col:
                        i = random.randint(1, 2)
                        self.col = True
                        if i == 1:  # dy > 0:
                            self.subpos = self.vitessex
                        else:
                            self.subpos = self.vitessey

                    self.rect.x += self.subpos

        if dir ==2 and dy <= 0:
            if not self.game.essai_deplacement(self, 0, -self.vitessex, group):
                if not self.game.essai_deplacement(self, 0, -self.vitessex, self.game.wall) :
                    self.rect.y -= self.vitessex
                    self.col  = False
                else :
                    if not self.col:
                        i = random.randint(1, 2)
                        self.col = True
                        if i == 1:  # dy > 0:
                            self.subpos = -self.vitessey
                        else:
                            self.subpos = self.vitessey

                    self.rect.x += self.subpos
        if self.rect.colliderect(self.game.player.rect)& ((pygame.time.get_ticks() - self.last_attack) / 1000>self.cd):
            self.game.player.take_damage(self.dmg)
            self.last_attack = pygame.time.get_ticks()


    def max(self, a , b):
        if abs(a) > abs(b):
            return 1 # deplacement horizontal
        else:
            return  2 #deplacement vertical

    def collisionMonstre2(self, rect):

       if self.rect.x + 5 > rect.x + rect.w:
            return True
       elif self.rect.x + self.rect.w - 5 < rect.x:
           return  True
       elif self.rect.y + self.rect.h  + 5 < rect.y:
           return True
       elif self.rect.y  - 5 > rect.y + rect.h:
           return  True
       else:
           return False

    def stop(self):
        self.vitessex = 0;
        self.vitessey = 0

    def battu(self):
        if self.num == "1":
            crop="S"
        elif self.num == "2":
            crop="W"
        elif self.num == "3":
            crop="C"
        elif self.num == "4":
            crop="P"
        nb=random.randint(0,3)
        for i in range (0,nb,1):
           self.game.player.inc_veg(crop)

    def prendre_degat(self, dmg):
        self.hp-=dmg
        self.damage_animation_timer=0
        if self.hp<=0:
            self.battu()
            self.kill()

    def update_anim_degats(self):
        colorImage = pygame.Surface(self.image.get_size()).convert_alpha()

        if self.damage_animation_timer >= 6:
            colorImage.fill("white")
            self.image.blit(colorImage, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            self.damage_animation_timer = -1

        elif self.damage_animation_timer!=-1:
            colorImage.fill("red")
            self.image.blit(colorImage, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            self.damage_animation_timer+=1

    def defineSpawn(self):
        spawn = random.randint(0,3)
        if spawn % 2 ==0 :
            self.rect.x = self.game.spawn[spawn].x + (50 * random.randint(-2,2))
            self.rect.y = self.game.spawn[spawn].y
        else:
            self.rect.x = self.game.spawn[spawn].x
            self.rect.y = self.game.spawn[spawn].y + (50 * random.randint(-2, 2))

    def ModifStat(self):
        if self.num == '3':
            self.vitessex = self.game.player.velocity - 1
            self.vitessey = self.game.player.velocity - 1
            self.subpos = 6
        elif self.num == '4':
            self.hp = 15


