import pygame

# ПЕРЕМЕННЫЕ
Coin = pygame.image.load('image/coin.png')
Coin_list = []
Coin = pygame.transform.scale(Coin, (100, 100))
Coin_count = 10
Coin_speed = 10
points = 0