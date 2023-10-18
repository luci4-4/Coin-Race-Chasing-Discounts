import pygame, sys

def events(remchik):
    """Обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                remchik.mright = True
            elif event.key == pygame.K_a:
                remchik.mleft = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                remchik.mright = False
            elif event.key == pygame.K_a:
                remchik.mleft = False