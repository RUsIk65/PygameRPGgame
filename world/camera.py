import pygame
from random import randint
from pytmx.util_pygame import load_pygame

maps = None
def load_map():
    global maps
    maps = load_pygame('world/2.tmx')

screen = pygame.display.set_mode((1500, 800))


class Camera_group(pygame.sprite.Group):
    def __init__(self, screen):
        super().__init__()
        self.display_surface = screen

        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

        self.camera_bordes = {'left' : 200, 'right' : 200, 'top' : 100, 'bottom' : 100}
        l = 200
        r = 200
        b = 100
        t = 100
        w = self.display_surface.get_size()[0] - (l + r) 
        h = self.display_surface.get_size()[1] - (t + b)
        self.camera_box = pygame.Rect(l, t, w, h)

    def center_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def box_camera(self, target):

        if target.rect.left < self.camera_box.left:
            self.camera_box.left = target.rect.left  

        if target.rect.right > self.camera_box.right:
            self.camera_box.right = target.rect.right
        if target.rect.top < self.camera_box.top:
            self.camera_box.top = target.rect.top
        if target.rect.bottom > self.camera_box.bottom:
            self.camera_box.bottom = target.rect.bottom

        self.offset.x = self.camera_box.left - self.camera_bordes['left']
        self.offset.y = self.camera_box.top - self.camera_bordes['top']


    def kaif_draw(self, target):
        
        self.center_camera(target)

        for layer in maps.visible_layers:
            for x, y, surf in layer.tiles():
                pos = (16 * x, 16 * y)
                ground_offset = pos - self.offset
                self.display_surface.blit(surf, ground_offset)
      
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            sprite_offset = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, sprite_offset)



camera_group = Camera_group(screen)

