import pygame


# Class declaration extends pygame.sprite.Sprite
class CollidableRect(pygame.sprite.Sprite):

    # Class initialization
    # eg. var rect = CollidableRect(0, 0, 10, 10, 0xFF0000)
    def __init__(self, x, y, width, height, colorOnHit):

        # extended class initialization
        pygame.sprite.Sprite.__init__(self)

        # Set Position 
        self.x = x
        self.y = y

        self.colorOnHit = colorOnHit
        
        self.speed = 0.3

        # Create image of size width and height
        self.image = pygame.Surface([width, height])

        # Fill image with white
        self.image.fill(0xFFFFFF)

        self.rect = self.image.get_rect()

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
    def render(self, screen, rectToTestCollision):
        # Update Position of Graphics
        self.rect.left = self.x
        self.rect.top = self.y

        # If hit turn a color
        # Else stay white
        if pygame.sprite.collide_rect(self, rectToTestCollision):
            self.image.fill(self.colorOnHit)
        else:
            self.image.fill(0xFFFFFF)
        
        # Render Graphics to Screen Buffer
        screen.blit(self.image, self.rect)
