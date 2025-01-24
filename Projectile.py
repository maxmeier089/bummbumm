import pygame
from pygame.math import *
from Config import *

class Projectile(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.r = 10
        self.pos = pos
        

    def update(self):
        self.pos.x += 5
        if self.pos.x - self.r > WIDTH:
            self.kill()

    def draw(self, displaysurface):
        pygame.draw.circle(displaysurface, (255,255,55), self.pos, self.r) 