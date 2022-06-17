import pygame


# Class functions declarations first variable must always be 'self'
# Class Variables have to be used with self.VARIABLE_NAME

class Player:

    # eg. variable = Player(0, 0, 1)
    def __init__(self, x, y, speed):

        # Set Position
        self.x = x
        self.y = y

        # Set Movement Speed
        self.speed = speed

        # Load Graphics
        self.image = pygame.image.load("pygame.png")
        self.rect = self.image.get_rect()

    # Pass keyboard state to check inputs and update position
    def update(self, keyboardState):

        if keyboardState[pygame.K_LEFT]:
            # Move -speed on x axis (Left)
            self.x -= self.speed
        if keyboardState[pygame.K_RIGHT]:
            # Move speed on x axis (RIGHT)
            self.x += self.speed
                
        if keyboardState[pygame.K_UP]:
            # Move -speed on y axis (UP)
            self.y -= self.speed
        if keyboardState[pygame.K_DOWN]:
            # Move speed on y axis (DOWN)
            self.y += self.speed

    # Render Graphics to Screen
    def render(self, screen):

        # Update Position of Graphics
        self.rect.x = self.x
        self.rect.y  = self.y

        # Render Graphics to Screen Buffer
        screen.blit(self.image, self.rect)
        
