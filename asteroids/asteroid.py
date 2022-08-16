import pygame.gfxdraw
import entity
import random
import math
from line import Point
from angles import *

class Asteroid(entity.Entity):

    def __init__(self, x, y):
        entity.Entity.__init__(self)
        self.x = x
        self.y = y
        self.lengths = [(int(random.random()*3)*5 + 20) for i in range(random.randrange(4, 10))]
        self.rotation = 0
        self.sides = len(self.lengths)
        self.dr = random.random()*math.pi + math.pi
        self.id = "Asteroid"


    def onCollide(self, e):
        if e.id == "Player":
            e.hit()
        
    def update(self, dt):
        self.rotation += self.dr*dt

    def update_collider(self):
        self.points = [Point((self.x + math.cos(self.rotation + i*M_2PI/self.sides)*self.lengths[i]),
                             (self.y + math.sin(self.rotation + i*M_2PI/self.sides)*self.lengths[i])) for i in range(self.sides)]
        
    def render(self, screen):

        points = [(int(point.x), int(point.y)) for point in self.points]
        sides = len(self.lengths)
        pygame.gfxdraw.polygon(screen, points, (255, 255, 255))
        
