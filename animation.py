import pygame

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load('assets/'+sprite_name+'.png')
        self.image = pygame.transform.scale(self.image, (50,50))


        self.current_image = 0

        self.orientation = "right"
        self.current_orientation = self.orientation

        self.listeAnimations = {
            'right': load_animation_images(sprite_name, "right"),
            'left': load_animation_images(sprite_name, "left"),
            'up' : load_animation_images(sprite_name, "up"),
            'down' : load_animation_images(sprite_name, "down")
        }
        self.images = self.listeAnimations.get('right')




    def animate(self):
        if(self.orientation!=self.current_orientation):
            self.images = self.listeAnimations.get(self.current_orientation)
            self.current_image=0
            self.orientation=self.current_orientation

        # passer à l'image suivante
        self.current_image += 1

        # verifier si on a atteint la fin de l'animation
        if self.current_image >= len(self.images):
            self.current_image = 0

        #modifier l'image precedente par la suivante
        self.image = self.images[self.current_image]
        self.image = pygame.transform.scale(self.image, (50,50))



# definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name, direction):
    # charger les images de ce sprite dans le dossier correspondant
    images = []

    path = f"assets/{sprite_name}/{sprite_name}{direction}"

    for num in range(1,4):
        image_path = path + str(num) +'.png'
        images.append(pygame.image.load(image_path))

    return images

# definir un dictionnaire qui va contenir les images chargées de chaque sprite

