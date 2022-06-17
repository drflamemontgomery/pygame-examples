import sys, pygame

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

while True:
    # Handle all events
    for event in pygame.event.get():
        # If window closed exit program
        if event.type == pygame.QUIT:
            sys.exit(0);
            

    # Update Calls are called here

    
            
    screen.fill(black)
    # Drawing calls are called here 

    # Draw the current Screen buffer
    pygame.display.flip()
    
