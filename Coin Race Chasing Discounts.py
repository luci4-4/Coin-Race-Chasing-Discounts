import pygame, controls

import jump
from hero import Remchik

def run():

    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('Монетная гонка: погоня за скидками')
    background_image = pygame.image.load("image/pixil-gif-drawing (4).gif")
    bg_color = (0, 0, 0)
    remchik = Remchik(screen)


    while True:
        controls.events(remchik)
        remchik.update_remchik()
        screen.fill(bg_color)
        screen.blit(background_image, (0, 0))
        remchik.output()
        pygame.display.flip()
        jump.jump()




run()