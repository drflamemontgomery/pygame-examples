import sys, pygame

# Initialize the pygame framework
pygame.init()

# ScreenSize as 640x480
size = width, height = 640, 480

# Custom Color Black Declaration
black = 0, 0, 0

# Initialize pygame with size of 640x480
# and name of "Image02"
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Image02")

# Load PyGame Logo as image
logo = pygame.image.load("pygame.png")

# Get Dimensions of Image for rendering
# Default Image Position 0, 0
logorect = logo.get_rect()

# Movement speed per frame
speed = 1.0

while True:
    # Handle all events
    for event in pygame.event.get():
        # If window closed exit program
        if event.type == pygame.QUIT:
            sys.exit(0);

    keyboardstate = pygame.key.get_pressed()


    # Screen axis
    #        -
    #        | Y
    #    X   |
    # -  --------- +
    #        |
    #        |
    #        +

    # Check if Arrow Keys are pressed
    
    if keyboardstate[pygame.K_LEFT]:
        # Move -speed on x axis (Left)
        logorect = logorect.move([-speed, 0])
    if keyboardstate[pygame.K_RIGHT]:
        # Move speed on x axis (RIGHT)
        logorect = logorect.move([speed, 0])
        
    if keyboardstate[pygame.K_UP]:
        # Move -speed on y axis (UP)
        logorect = logorect.move([0, -speed])
    if keyboardstate[pygame.K_DOWN]:
        # Move speed on y axis (DOWN)
        logorect = logorect.move([0, speed])
                
    screen.fill(black)
    # Drawing calls are called here 

    # Render Logo to Screen buffer
    screen.blit(logo, logorect)

    # Draw the current Screen buffer
    pygame.display.flip()
    
