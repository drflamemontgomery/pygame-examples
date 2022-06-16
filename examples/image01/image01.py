import sys, pygame

# Initialize the pygame framework
pygame.init()

# ScreenSize as 640x480
size = width, height = 640, 480

# Custom Color Black Declaration
black = 0, 0, 0

# Initialize pygame with size of 640x480
# and name of "Image01"
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Image01")

# Load PyGame Logo as image
logo = pygame.image.load("pygame.png")

# Get Dimensions of Image for rendering
# Default Image Position 0, 0
logorect = logo.get_rect()

while True:
    # Handle all events
    for event in pygame.event.get():
        # If window closed exit program
        if event.type == pygame.QUIT:
            sys.exit(0);

    screen.fill(black)
    # Drawing calls are called here 

    # Render Logo to Screen buffer
    screen.blit(logo, logorect)

    # Render the Screen buffer 
    pygame.display.flip()
    
