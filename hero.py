import pygame


Remchik = pygame.image.load('image/Probnik.png')
rect_Remchik = pygame.Rect(100,100,200,100)

class Rem(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = rect_Remchik
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 450


