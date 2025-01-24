import pygame, random
from Config import *

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.r = 40
        self.pos = pygame.Vector2(WIDTH + self.r, random.randint(self.r, HEIGHT - self.r))
        

    def update(self, game):
        self.pos.x -= 3
        if self.pos.x + self.r < 0:
            self.kill()
            game.score -= 5

    def draw(self, displaysurface):
        pygame.draw.circle(displaysurface, (255,255,255), self.pos, self.r) 