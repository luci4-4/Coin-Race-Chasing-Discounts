import pygame, controls

from hero import Remchik
from controls import running_left, running_right, player_anim_count

clock = pygame.time.Clock()
bg_x = 0

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Coin Race: Chasing Discounts")
back_ground = pygame.image.load('image/Background(1).jpg')
pygame.display.set_icon(pygame.image.load('image/Remchikicon.ico'))

running = True
while running:



    screen.blit(back_ground, (bg_x, 0))
    screen.blit(back_ground, (bg_x + 1000, 0))
    screen.blit(running_right[player_anim_count], (0, 450))

    if player_anim_count == 2:
        player_anim_count = 0
    else:
        player_anim_count += 1

    bg_x -= 10
    if bg_x == -1000:
        bg_x = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    while True:
        controls.events(remchik)
        remchik.update_remchik()
        screen.fill(bg_color)
        screen.blit(background_image, (0, 0))
        remchik.output()
        pygame.display.flip()



    clock.tick(8)
