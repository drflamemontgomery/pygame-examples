import pygame.gfxdraw
import entity
import math
from line import Point

class Bullet(entity.Entity):

    speed = 256
    
    def __init__(self, x, y, rotation):
        entity.Entity.__init__(self)
        self.x = x
        self.y = y
        self.rotation = rotation
        self.length = 10
        self.id = "Bullet"

    def update_collider(self):
        self.points = [Point(self.x, self.y), Point(self.x + math.cos(self.rotation)*self.length, self.y + math.sin(self.rotation)*self.length)]
        
    def onCollide(self, e):
        if e.id == "Asteroid":
            e.hit()
            self.dispose()
        
    def update(self, dt):

        self.x += math.cos(self.rotation)*Bullet.speed*dt
        self.y += math.sin(self.rotation)*Bullet.speed*dt

        if self.x > 672 or self.x < -32 or self.y > 512 or self.y < -32:
            self.dispose()
            
    def render(self, screen):
        pygame.gfxdraw.line(screen, int(self.x), int(self.y),
                            int(self.x + math.cos(self.rotation)*self.length),
                            int(self.y + math.sin(self.rotation)*self.length),
                            (255, 255, 255))
    
