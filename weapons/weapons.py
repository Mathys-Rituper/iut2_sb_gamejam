import pygame
import random
from projectile import Projectile


class Pistolet(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.cooldown = 0.3
        self.vitesse_projectile = 6
        self.damage = 3
        self.ttl = 45

    def fire(self):
        if (self.player.cd()/self.player.attack_speed) > self.cooldown:
            direction = self.player.current_orientation
            if direction == "right":
                x = self.player.rect.center[0]
                y = self.player.rect.center[1]
                dx = self.vitesse_projectile + random.randint(1, 3)
                dy = ((random.random() - 0.5) * 2)
            elif direction == "left":
                x = self.player.rect.center[0]
                y = self.player.rect.center[1]
                dx = -self.vitesse_projectile + random.randint(-3, -1)
                dy = ((random.random() - 0.5) * 2)
            elif direction == "up":
                x = self.player.rect.center[0]
                y = self.player.rect.center[1]
                dy = -self.vitesse_projectile + random.randint(-3, -1)
                dx = ((random.random() - 0.5) * 2)
            else:
                x = self.player.rect.center[0]
                y = self.player.rect.center[1]
                dy = self.vitesse_projectile + random.randint(1, 3)
                dx = ((random.random() - 0.5) * 2)
            self.player.game.projectiles.add(Projectile(self.player.game, x, y, dx, dy, self.damage*self.player.attack_strength, self.ttl, 30))
            self.player.reset_cd()

class Mitrailleuse(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.cooldown = 0.1
        self.vitesse_projectile = 7
        self.damage = 2
        self.ttl = 45

    def fire(self):
        if (self.player.cd()/self.player.attack_speed) > self.cooldown:
            direction = self.player.current_orientation
            if direction == "right":
                x = self.player.rect.center[0]
                y = self.player.rect.center[1]
                dx = self.vitesse_projectile + random.randint(1, 3)
                dy = ((random.random() - 0.5) * 2)
            elif direction == "left":
                x = self.player.rect.center[0]
                y = self.player.rect.center[1]
                dx = -self.vitesse_projectile + random.randint(-3, -1)
                dy = ((random.random() - 0.5) * 2)
            elif direction == "up":
                x = self.player.rect.center[0]
                y = self.player.rect.center[1]
                dy = -self.vitesse_projectile + random.randint(-3, -1)
                dx = ((random.random() - 0.5) * 2)
            else:
                x = self.player.rect.center[0]
                y = self.player.rect.center[1]
                dy = self.vitesse_projectile + random.randint(1, 3)
                dx = ((random.random() - 0.5) * 2)
            self.player.game.projectiles.add(Projectile(self.player.game, x, y, dx, dy, self.damage*self.player.attack_strength, self.ttl, 0))
            self.player.reset_cd()
class Snipe(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.cooldown = 1
        self.vitesse_projectile = 20
        self.damage = 10
        self.ttl = 100


    def fire(self):
        if (self.player.cd()/self.player.attack_speed) > self.cooldown:
            direction = self.player.current_orientation
            if direction == "right":
                x = self.player.rect.center[0]
                y = self.player.rect.center[1]
                dx = self.vitesse_projectile
                dy = 0
            elif direction == "left":
                x = self.player.rect.center[0]
                y = self.player.rect.center[1]
                dx = -self.vitesse_projectile
                dy = 0
            elif direction == "up":
                x = self.player.rect.center[0]
                y = self.player.rect.center[1]
                dy = -self.vitesse_projectile
                dx = 0
            else:
                x = self.player.rect.center[0]
                y = self.player.rect.center[1]
                dy = self.vitesse_projectile
                dx = 0
            self.player.game.projectiles.add(Projectile(self.player.game, x, y, dx, dy, self.damage*self.player.attack_strength, self.ttl, 1000))
            self.player.reset_cd()

class Pompe(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.cooldown = 0.3
        self.vitesse_projectile = 12
        self.damage = 2
        self.spread_factor = .25
        self.ttl = 18

    def fire(self):
        if (self.player.cd()/self.player.attack_speed) > self.cooldown:
            direction = self.player.current_orientation
            if direction == "right":
                centre = [self.player.rect.center[0] ,
                          self.player.rect.center[1]]  # centre de la ligne sur laquelle les balles sont ajoutées
                for i in range(-3, 4, 1):
                    if i != 0:
                        x = centre[0]
                        y = centre[1] + ((i + random.randint(-3, 3)) * 3)
                        dx = self.vitesse_projectile + random.randint(3, 5)
                        dy = (i + random.randint(-3, 3)) * self.spread_factor
                        self.player.game.projectiles.add(Projectile(self.player.game, x, y, dx, dy, self.damage*self.player.attack_strength, self.ttl, 1))

            elif direction == "left":
                centre = [self.player.rect.center[0] ,
                          self.player.rect.center[1]]  # centre de la ligne sur laquelle les balles sont ajoutées
                for i in range(-3, 4, 1):
                    if i != 0:
                        x = centre[0]
                        y = centre[1] + ((i + random.randint(-3, 3)) * 3)
                        dx = -self.vitesse_projectile + random.randint(-5,-3)
                        dy = (i + random.randint(-3, 3)) * self.spread_factor
                        self.player.game.projectiles.add(Projectile(self.player.game, x, y, dx, dy, self.damage*self.player.attack_strength, self.ttl, 1))

            elif direction == "up":

                centre = [self.player.rect.center[0],
                          self.player.rect.center[1] ]  # centre de la ligne sur laquelle les balles sont ajoutées
                for i in range(-3, 4, 1):
                    if i != 0:
                        x = centre[0] + ((i + random.randint(-3, 3)) * 3)
                        y = centre[1]
                        dy = - self.vitesse_projectile + random.randint(-5, -3)
                        dx = (i + random.randint(-3, 3)) * self.spread_factor

                        self.player.game.projectiles.add(Projectile(self.player.game, x, y, dx, dy, self.damage*self.player.attack_strength, self.ttl, 1))

            else:

                centre = [self.player.rect.center[0],
                          self.player.rect.center[1] ]  # centre de la ligne sur laquelle les balles sont ajoutées
                for i in range(-3, 4, 1):
                    if i != 0:
                        x = centre[0] + ((i + random.randint(-3, 3)) * 3)
                        y = centre[1]
                        dy = self.vitesse_projectile + random.randint(3, 5)
                        dx = (i + random.randint(-3, 3)) * self.spread_factor

                        self.player.game.projectiles.add(Projectile(self.player.game, x, y, dx, dy, self.damage*self.player.attack_strength, self.ttl, 1))

            self.player.reset_cd()
