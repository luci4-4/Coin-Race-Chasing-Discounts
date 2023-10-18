import pygame, controls
from hero import Remchik

def run():

    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Монетная гонка: погоня за скидками')
    # background_image = pygame.image.load()
    bg_color = (0, 0, 0)
    remchik = Remchik(screen)

    while True:
        controls.events(remchik)
        remchik.update_remchik()
        screen.fill(bg_color)
        remchik.output()
        pygame.display.flip()


run()