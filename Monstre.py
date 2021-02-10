from select import select

import pygame
import random
import threading
class Monstre(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.vitessex = 2
        self.vitessey = 2
        self.num = str(random.randint(1,4))
        #self.path = str('assets/Monstre/monstre'+self.num+'.png')
        self.image = pygame.image.load('assets/Monstre/monstre'+self.num+'.png')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.game = game
        self.i = random.randint(1,3)
        self.rect.x = 2143
        self.rect.y = 1020
        self.check = 0;
        self.animation = True
        self.col = False
        self.subpos = 0




    def mouvement(self, posx, posy , group ):

        dx = posx - self.rect.x
        dy = posy - self.rect.y
        # for all item in groupe teste collision
        dir = self.max(dx, dy)
        #self.animationG()

        if dir ==1 and dx >= 0:
            self.animation = True
            if not self.game.essaieDeplacement(self, self.vitessex, 0 ,group):
                if not self.game.essaieDeplacement(self, self.vitessex, 0, self.game.wall)  :
                    self.rect.x += self.vitessex
                    self.col = False
                else:
                    if not self.col:
                        i = random.randint(1,2)
                        print("i 1er", i)
                        self.col = True
                        self.vitessex = 2
                        self.vitessey = 2
                        if i  == 1:#dy > 0:
                            self.subpos = -2
                        else:
                             #self.rect.y -= self.vitessey
                             self.subpos = 2
                    self.rect.y += self.subpos

        if dir ==1 and dx < 0:
            self.animation = False
            if not self.game.essaieDeplacement(self, -self.vitessex, 0, group):
                if not self.game.essaieDeplacement(self, -self.vitessex, 0, self.game.wall):
                    self.rect.x -= self.vitessex
                    self.col = False
                else :
                    if not self.col:
                        i = random.randint(1, 2)
                        self.col = True
                        print("i 2em" , i)
                        if i == 1:  # dy > 0:
                            self.subpos = -2
                        else:
                            self.subpos = 2

                    self.rect.y += self.subpos

        if dir ==2 and dy >= 0:
            if not self.game.essaieDeplacement(self, 0,self.vitessex, group):
                if not self.game.essaieDeplacement(self, 0, self.vitessex, self.game.wall)  :
                    self.rect.y += self.vitessex
                    self.col = False
                else :
                    if not self.col:
                        i = random.randint(1, 2)
                        self.col = True
                        print("i 2em", i)
                        if i == 1:  # dy > 0:
                            self.subpos = -2
                        else:
                            self.subpos = 2

                    self.rect.x += self.subpos

        if dir ==2 and dy <= 0:
            if not self.game.essaieDeplacement(self, 0, -self.vitessex, group):
                if not self.game.essaieDeplacement(self, 0, -self.vitessex, self.game.wall) :
                    self.rect.y -= self.vitessex
                    self.col  = False
                else :
                    if not self.col:
                        i = random.randint(1, 2)
                        self.col = True
                        print("i 2em", i)
                        if i == 1:  # dy > 0:
                            self.subpos = -2
                        else:
                            self.subpos = 2

                    self.rect.x += self.subpos



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




