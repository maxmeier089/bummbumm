import pygame, random
from Config import *
from Player import *
from Enemy import *

class Game:

    def __init__(self):
        pygame.init()
        self.score = 0
        self.font = pygame.font.SysFont(None, 82)
        self.player = Player()
        self.enemies = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()


    def update(self):

        # update player
        self.player.update(self)

        # update enemies
        for e in self.enemies:
            e.update(self)

        # update projectiles
        for p in self.projectiles:
            p.update()

        # check player hit
        for e in self.enemies:
            if self.player.pos.distance_to(e.pos) < self.player.r + e.r:
                self.score -= 10

        # check enemy hits
        for e in self.enemies:
            for p in self.projectiles:
                if e.pos.distance_to(p.pos) < e.r + p.r:
                    e.kill()
                    p.kill()
                    self.score += 3

        # randomly spawn enemies
        if random.randint(0, 22) == 0:
            self.enemies.add(Enemy())


    def draw(self, displaysurface):

        # draw background
        displaysurface.fill((55,55,255))

        # draw player
        self.player.draw(displaysurface)

        # draw enemies
        for e in self.enemies:
            e.draw(displaysurface)

        # draw projectiles
        for p in self.projectiles:
            p.draw(displaysurface)

        # draw score
        scoreImg = self.font.render(str(self.score), True, (255, 255, 255))
        displaysurface.blit(scoreImg, (50, 50))

        # update display
        pygame.display.update()


    

