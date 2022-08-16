import sys, pygame
import pygame.gfxdraw
from entity import *
from player import *
from asteroid import *
# Initialize the pygame framework
pygame.init()

# ScreenSize as 640x480
size = width, height = 640, 480

# Custom Color Black Declaration
black = 0, 0, 0

# Initialize pygame with size of 640x480
# and name of "Simple Window"
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Simple Window")

clock = pygame.time.Clock()
dt = 0
clock.tick(60)

#for i in range(100):
#    Player((i%20)*20, 100 + int(i/20)*30, 0)#math.pi*2*((i%20)/20))
Player(100, 100, 0)
Asteroid(200, 200)
while True:
    # Handle all events
    for event in pygame.event.get():
        # If window closed exit program
        if event.type == pygame.QUIT:
            sys.exit(0);
            

    # Update Calls are called here

    Entity.update_all(dt)
    
            
    screen.fill(black)
    # Drawing calls are called here
    Entity.render_all(screen)
    # Draw the current Screen buffer
    pygame.display.flip()

    Entity.gc()
    
    dt = clock.tick(60)/1000
    

