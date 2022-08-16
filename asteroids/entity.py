import pygame
from line import intersect

class Entity(pygame.sprite.Sprite):

    ALL = []
    GC = []
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.disposed = False
        self.x = 0
        self.y = 0
        self.dx = 0 # Velocities
        self.dy = 0 # Velocities
        self.vx = 0 # Visual Offset
        self.vy = 0 # Visual Offset
        self.id = "PLACEHOLDER"
        
        self.points = []
        
        Entity.ALL += [self]

    def hit(self):
        self.dispose()
        
    def onCollide(self, e):
        pass
        
    def collide(self, e):
        for v in range(len(self.points)):
            for ev in range(len(e.points)):
                if intersect(self.points[v], self.points[(v+1)%len(self.points)],
                             e.points[ev], e.points[(ev+1)%len(e.points)]):
                    self.onCollide(e)
                    return

    def update_collider(self):
        pass
                
    def update_all(dt):
        for e in Entity.ALL:
            if not e.disposed:
                e.update(dt)
                e.update_collider()

        for e in Entity.ALL:
            if not e.disposed:
                for e2 in Entity.ALL:
                    if not e2.disposed and e2 != e:
                        e.collide(e2)

    def render_all(screen):
        for e in Entity.ALL:
            e.render(screen)
            
    def dispose(self):
        self.disposed = True
        Entity.GC += [self]

    def gc(): 
        for e in Entity.GC:
            if e in Entity.ALL:
                Entity.ALL.remove(e)
            Entity.GC.remove(e)
            
    def update(self, dt):
        pass

    def render(self, screen):
        pass
