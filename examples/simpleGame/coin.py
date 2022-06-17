import pygame
import random

class Coin(pygame.sprite.Sprite):

    # Create Coin at random position
    def __init__(self, screen_width, screen_height):
        self.image = pygame.image.load("coin.png")

        # Scale coin to 16x16 image
        self.image = pygame.transform.scale(self.image, (16, 16))
        
        self.rect = self.image.get_rect()
    
        # Local variable of screen space
        self.s_width  = screen_width - self.rect.width
        self.s_height = screen_height - self.rect.height

        # Randomize Position
        self.hit()
        
    def hit(self):
        # Move to random position
        self.rect.x = random.randint(0, self.s_width)
        self.rect.y  = random.randint(0, self.s_height)
        
    def render(self, screen):
        # Render Image to screen
        screen.blit(self.image, self.rect)
        
        
