import pygame

class Projectile(pygame.sprite.Sprite):

    def __init__(self,player):
        super().__init__()
        self.velocity = 1
        self.player = player
        self.image = pygame.image.load('assets/bullet.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.current_orientation = self.player.current_orientation


        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 30
        self.rect.y = player.rect.y + 20


    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        if self.current_orientation == "right":
            self.rect.x += self.velocity

        elif self.current_orientation =="left":
            self.rect.x -= self.velocity

        elif self.current_orientation == "down":
            self.rect.y += self.velocity

        elif self.current_orientation == "up":
            self.rect.y -= self.velocity

        if self.rect.x > 1024 or self.rect.x <0 or self.rect.y > 768 or self.rect.y<0:
            self.remove()




