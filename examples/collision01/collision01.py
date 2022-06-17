import sys, pygame
from collidable_rect import *

# Initialize the pygame framework
pygame.init()

# ScreenSize as 640x480
size = width, height = 640, 480

# Custom Color Black Declaration
black = 0, 0, 0
green = 0, 0xFF, 0
red   = 0xFF, 0, 0

# Initialize pygame with size of 640x480
# and name of "Collision 01"
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Collision 01")


# Create a collidable Rectangle that turns green on collision
# Position = (10, 10)
# Size = 40x40
rect1 = CollidableRect(10, 10, 40, 40, green)

# Create a collidable Rectangle that turns red on collision
# Position = (100, 10)
# Size = 100x50
rect2 = CollidableRect(100, 10, 100, 50, 0xFF0000)

while True:
    # Handle all events
    for event in pygame.event.get():
        # If window closed exit program
        if event.type == pygame.QUIT:
            sys.exit(0);
            
    keyboardState = pygame.key.get_pressed()
            
    # Update Calls are called here

    rect1.update(keyboardState)
            
    screen.fill(black)
    # Drawing calls are called here 

    rect2.render(screen, rect1)
    rect1.render(screen, rect2)
    
    # Draw the current Screen buffer
    pygame.display.flip()
    
