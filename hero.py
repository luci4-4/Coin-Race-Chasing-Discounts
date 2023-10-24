import pygame
jumpCount = 10
class Remchik():

    def __init__(self, screen):

        """Инициализация Ремчика"""

        self.screen = screen
        self.image = pygame.image.load('image/Remchik.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = (self.screen_rect.left) + 10
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False
        self.mjump = False



    def output(self):
        """ Рисует Ремчика"""
        self.screen.blit(self.image, self.rect)


    def update_remchik(self):
        """ОБНОВЛЕНИЕ ПОЗИЦИ РЕМЧИКА"""
        global mjump, jumpCount
        if self.mright and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        elif self.mleft and self.rect.left > 0:
            self.rect.centerx -= 1
        elif self.mjump and self.rect.y >= self.screen_rect.y:
            if jumpCount >= -10:
                self.rect.centery -= jumpCount / 500
                self.rect.centery -= 1
                jumpCount -= 10
            else:
                jumpCount = 10
                mjump = False








