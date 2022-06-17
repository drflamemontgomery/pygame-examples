import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, speed):

        pygame.sprite.Sprite.__init__(self)
        
        self.x = x
        self.y = y
        self.speed = speed

        self.score = 0
        
        self.image = pygame.image.load("pygame.png")
        self.rect = self.image.get_rect()

    # Handle Keyboard Inputs
    def handle_input(self, keyboardState):
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

    # Return Current Game Score
    def get_score(self):
        return self.score

    # Check if Player Has Collided With A Coin
    def collided_with_coin(self, coin):
        return pygame.sprite.collide_rect(self, coin)

    def update(self, keyboardState, coins):
        # move player
        self.handle_input(keyboardState)

        # Check if Player collided with any coins
        for coin in coins:
            if self.collided_with_coin(coin):
                coin.hit()
                self.score += 1

    def render(self, screen):
        
        self.rect.x = self.x
        self.rect.y  = self.y

        # Render image to screen
        screen.blit(self.image, self.rect)
        
        
