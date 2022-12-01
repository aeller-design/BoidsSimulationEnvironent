"""foodSource class"""
import pygame
import numpy as np
import random
from . import params
from . import assets


class FoodSource(pygame.sprite.Sprite):
    """A food source to provide sustenance to boids and replenish their hunger meter."""

    images_list = ('corn_60157.png', 'plant1_6060.png',
                   'plant2_10050.png', 'purple_flower_6080.png')

    def __init__(self, pos=None):
        super().__init__()
        self.image, self.rect = assets.image_with_rect(self.getImage())
        self.pos = pos if pos is not None else np.zeros(2)
        self.rect = self.image.get_rect(center=self.pos)
        self.health = 10

    def getImage(self):
        item = random.choices(self.images_list, k=1)[0]
        return item

    def display(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.health <= 0:
            self.kill()
        return True
