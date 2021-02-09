from pytmx import  load_pygame
import pytmx
import  pygame
from setting import  *


class Tile_map():
    def __init__(self):
        self.tmx = load_pygame('assets/Map.tmx', pixelalpha=True)
        self.ti = self.tmx.get_tile_image_by_gid
        self.wall = []
        #for tile_object in self.tmx.objects:
         #   self.wall.append(tile_object)

    def render(self, screen):
        for layer in self.tmx.visible_layers:
                if isinstance(layer, pytmx.TiledTileLayer):
                    for x, y, gid in layer:
                        t = self.ti(gid)
                        if t:
                            screen.blit(t, (x * 32, y * 32))

    def make_map(self):
        map = pygame.Surface((WIDTH_TILE*NB_TILE_X, HEIGHT_TILE*NB_TILE_Y))
        self.render(map)
        return map

