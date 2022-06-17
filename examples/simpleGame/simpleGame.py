import sys, pygame
from player import Player
from coin import Coin

# Initialize the pygame framework
pygame.init()
# Initialize fonts
pygame.font.init()

# ScreenSize as 640x480
size = width, height = 640, 480

# Custom Color Black Declaration
black = 0, 0, 0

# Initialize pygame with size of 640x480
# and name of "Simple Game"
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Simple Game")

# Create Player
player = Player(10, 10, 0.5)

# Intialize 10 Coins
coins = [Coin(640,480) for i in range(10)]

# Load Font
font = pygame.font.SysFont('Comic Sans MS', 30)

    
while True:
    # Handle all events
    for event in pygame.event.get():
        # If window closed exit program
        if event.type == pygame.QUIT:
            sys.exit(0);
            

    keyboardState = pygame.key.get_pressed()
            
    # Update Player Callbacks
    player.update(keyboardState, coins)
    
            
    screen.fill(black)
    # Drawing calls are called here

    # Render Coins
    for coin in coins:
        coin.render(screen)
    # Render Player
    player.render(screen)

    # Update Score Image Then Render
    cur_score = font.render(str(player.get_score()), False, 0xFFFFFF)
    screen.blit(cur_score, (0, 0))
    
    # Draw the current Screen buffer
    pygame.display.flip()
    
