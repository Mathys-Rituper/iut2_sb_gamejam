import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, game, x, y, dx, dy, damage, ttl, pen):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('assets/bullet.png')
        self.image = pygame.transform.scale(self.image, (8, 8))

        self.dmg = damage
        self.velocity = 2
        self.dx = dx
        self.dy = dy
        self.penetration = pen # en pixels
        self.penned = 0

        self.ttl = ttl
        self.tl = 0

        self.rect = self.image.get_rect()
        self.rect.x = x - (self.rect.width / 2)
        self.rect.y = y

    def remove(self):
        self.game.projectiles.remove(self)

    def move(self):

        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.tl == self.ttl:
            self.remove()
        else:
            self.tl += 1

        for ob in self.game.tab_monstre:
            if ob.rect.contains(self.rect):

                ob.prendre_degat(self.dmg)
                self.penned += 1

                if self.penned >= self.penetration:
                    self.kill()
        for ob in self.game.wall:
            if ob.rect.contains(self.rect):
                    self.kill()