import pygame
coin_img = pygame.image.load("image/coin.png")
coin_img = pygame.transform.scale(coin_img, (100,100))

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y






