import pygame

class Projectile(pygame.sprite.Sprite):

    def __init__(self,game,x ,y ,dx,dy,damage, ttl):
        super().__init__()
        self.velocity = 2
        self.game=game
        self.image = pygame.image.load('assets/bullet.png')
        self.image = pygame.transform.scale(self.image, (8, 8))
        self.dx = dx
        self.dy = dy
        self.ttl = ttl
        self.tl = 0


        self.rect = self.image.get_rect()
        self.rect.x = x-(self.rect.width/2)
        self.rect.y = y


    def remove(self):
        self.game.projectiles.remove(self)

    def move(self):
        self.rect.x+=self.dx
        self.rect.y+=self.dy
        if self.tl==self.ttl:
            self.remove()
        else:
            self.tl+=1

