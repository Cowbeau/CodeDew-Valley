import pygame 
from settings import *   # noqa: F403
from player import Player # noqa: F403

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()
        
        self.setup()# noqa: E999

    def setup(self):
        self.player = Player((640,360), self.all_sprites)  # noqa: F405

    def run(self,dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)