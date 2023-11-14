import pygame, controls

from hero import Remchik
from controls import running_left, running_right, player_anim_count

# ПЕРЕМЕННЫЕ
clock = pygame.time.Clock()
bg_x = 0
player_speed = 10
player_x = 0
player_y = 450

is_jump = False
jump_count = 10




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
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
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

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()



    clock.tick(40)


