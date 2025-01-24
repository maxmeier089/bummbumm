import pygame
from pygame.math import *
from Projectile import *

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.r = 50
        self.pos = Vector2(100, 500)
        self.cooldown = 0
        

    def update(self, game): 
        pressedKeys = pygame.key.get_pressed()

        if pressedKeys[pygame.K_UP]:
            self.pos.y -= 4
        if pressedKeys[pygame.K_DOWN]:
            self.pos.y += 4
            
        if self.cooldown == 0 and pressedKeys[pygame.K_SPACE]:
            game.projectiles.add(Projectile(self.pos.copy()))
            game.score -= 1
            self.cooldown = 12
        elif self.cooldown > 0:
            self.cooldown -= 1

    def draw(self, displaysurface):
        pygame.draw.circle(displaysurface, (55,225,5), self.pos, self.r)
