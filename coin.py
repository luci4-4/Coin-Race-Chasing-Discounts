import pygame

# ПЕРЕМЕННЫЕ
Coin = pygame.image.load('image/coin.png')
Coin_list = []
Coin = pygame.transform.scale(Coin, (100, 100))
Coin_count = 15
Coin_speed = 6
points = 0