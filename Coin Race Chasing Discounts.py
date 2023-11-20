import pygame, controls, random

from hero import Remchik
from controls import running_left, running_right, player_anim_count
import coin
from hero import Rem
# ПЕРЕМЕННЫЕ
clock = pygame.time.Clock()
bg_x = 0
player_speed = 10
player_x = 0
player_y = 450

is_jump = False
jump_count = 10

coins = pygame.sprite.Group()

score = 0

coin_x = []
coin_y = []
coin_num = []
coin1 = coin.Coin(100,450)
coin2 = coin.Coin(200, 450)
coins.add(coin1, coin2)
coin_x.append(coin1.rect.x)
coin_y.append(coin1.rect.y)
coin_x.append(coin2.rect.x)
coin_y.append(coin2.rect.y)

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Coin Race: Chasing Discounts")
back_ground = pygame.image.load('image/Background(1).jpg')
pygame.display.set_icon(pygame.image.load('image/Remchik_icon.ico'))
running = True
while running:



    screen.blit(back_ground, (bg_x, 0))
    # screen.blit(back_ground, (bg_x + 1000, 0))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
        if keys[pygame.K_LEFT]:
            screen.blit(running_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(running_right[player_anim_count], (player_x, player_y))
    else:
        screen.blit(Remchik, (player_x, player_y))

    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed

    elif keys[pygame.K_RIGHT] and player_x < 900:
        player_x += player_speed

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            if jump_count > 0:
                player_y -= (jump_count ** 2) // 2
            else:
                player_y += (jump_count ** 2) // 2
            jump_count -= 2
        else:
            is_jump = False
            jump_count = 10

    if player_anim_count == 2:
        player_anim_count = 0
    else:
        player_anim_count += 1

    # bg_x -= 5
    # if bg_x == -1000:
    #     bg_x = 0
    coins.draw(screen)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
#Тут потом переработаю, надо делать что-то либо со спрайтами, либо что-то другое думать
    for coinn in coins:
        for i, j in zip(coin_x, coin_y):
            if (abs(i - player_x) <= 10 and abs(j - player_y) <= 10):
                score += 1

    print(f"Счёт: {score} монеток")

    coins.update()

    clock.tick(42)


