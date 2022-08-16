import pygame.gfxdraw
import entity
from bullet import Bullet
import math
from line import Point
from angles import *

class Player(entity.Entity):
    def __init__(self, x, y, rotation):
        entity.Entity.__init__(self)
        self.x = x
        self.y = y
        self.rotation = rotation
        self.length = 20
        self.k_pressed = False
        self.id = "Player"
        
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rotation -= 2.5*dt
        if keys[pygame.K_RIGHT]:
            self.rotation += 2.5*dt
        if keys[pygame.K_UP]:
            self.x += math.cos(self.rotation)*128*dt
            self.y += math.sin(self.rotation)*128*dt

        if keys[pygame.K_SPACE] and not self.k_pressed:
            self.k_pressed = True
            Bullet(self.x + math.cos(self.rotation)*(self.length+2),
                   self.y + math.sin(self.rotation)*(self.length+2),
                   self.rotation)
        elif not keys[pygame.K_SPACE] and self.k_pressed:
            self.k_pressed = False
            

    def onCollide(self, e):
        if e.id == "Asteroid":
            self.hit()
            
    def update_collider(self):
        self.points = [Point(self.x + self.length*math.cos(self.rotation + M_2_3PI*i),
                             self.y + self.length*math.sin(self.rotation + M_2_3PI*i)) for i in range(3)]
    def render(self, screen):
        pygame.gfxdraw.trigon(screen,
                              int(self.points[0].x), int(self.points[0].y),
                              int(self.points[1].x), int(self.points[1].y),
                              int(self.points[2].x), int(self.points[2].y),
                              (255, 255, 255))
                              
    
