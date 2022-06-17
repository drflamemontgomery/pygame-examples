import sys, pygame
from player import *

# Initialize the pygame framework
pygame.init()

# ScreenSize as 640x480
size = width, height = 640, 480

# Custom Color Black Declaration
black = 0, 0, 0

# Initialize pygame with size of 640x480
# and name of "Classes 01"
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Classes 01")


player = Player(20, 20, 0.3)

while True:
    # Handle all events
    for event in pygame.event.get():
        # If window closed exit program
        if event.type == pygame.QUIT:
            sys.exit(0);


    # Update Callbacks are called Here
            
    keyboardState = pygame.key.get_pressed()
    player.update(keyboardState)
    
    screen.fill(black)
    # Drawing calls are called here 

    player.render(screen)
    

    # Draw the current Screen buffer
    pygame.display.flip()
    
