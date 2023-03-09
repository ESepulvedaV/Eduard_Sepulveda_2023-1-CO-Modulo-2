import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import HAMMER

class Shoot (Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.image = HAMMER
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.speed_hammer = 5

    def update(self, power_ups, game_speed):
        self.rect.x += self.speed_hammer
        self.rect.x += game_speed
        
        if self.rect.x > self.rect.width:
            power_ups.pop()
             





