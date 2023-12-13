import pygame

from hero import Remchik, player_speed, player_y, player_x
from controls import running_left, running_right, player_anim_count
from coin import points, Coin_count, Coin_list, Coin_speed, Coin
from random import randint as ri


# ПЕРЕМЕННЫЕ
clock = pygame.time.Clock()
bg_x = 0
jump_count = 10
is_jump = False
running = True

# НАСТРОЙКА МИКШЕРА
pygame.mixer.pre_init(44100, -16, 1, 512)

# ИНИЦИАЛИЗАЦИЯ
pygame.init()
pygame.font.init()

#ФОННОВАЯ МУЗЫКА
pygame.mixer.music.load("Audio/79bpm.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

#ЗВУКИ
CoinS = pygame.mixer.Sound("Audio/brosok-odnoy-monetki-v-obschuyu-kuchu.mp3")
FinalS = pygame.mixer.Sound("Audio/zvuk-pobedyi-v-sportivnoy-igre-22991.mp3")
FinalS.set_volume(0.3)

# ШРИФТ
labal_font = pygame.font.Font('font/SuperMario256.ttf', 40)

# ЭКРАН
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Coin Race: Chasing Discounts")
back_ground = pygame.image.load('image/Background.jpg').convert_alpha()
pygame.display.set_icon(pygame.image.load('image/Remchik_icon.ico'))

# ОСНОВНОЙ ЦИКЛ
while running:
    # ТЕКСТ
    labal_points = labal_font.render(str(points) + '(10)', False, (0, 100, 0))
    labal_win = labal_font.render('Well done!', False, (0, 100, 0))

    # ВЫВОД НА ЭКРАН
    screen.blit(back_ground, (bg_x, 0))
    screen.blit(back_ground, (bg_x + 1000, 0))
    screen.blit(back_ground, (bg_x - 1000, 0))
    screen.blit(labal_points, (850, 30))

    # СПРАЙТЫ
    player_rect = Remchik.get_rect(topleft=(player_x, player_y))

    # РАБОТА КЛАВИШ И ПРОВЕРКА ИХ НАЖАТИЙ

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
        bg_x += player_speed - 2
        if bg_x == 1000:
            bg_x = 0
    elif keys[pygame.K_RIGHT] and player_x < 900:
        player_x += player_speed
        bg_x -= player_speed - 2
        if bg_x == -1000:
            bg_x = 0
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

    # АНИМАЦИЯ РЕМЧИКА
    if player_anim_count == 1:
        player_anim_count = 0
    else:
        player_anim_count += 1

    # РАНДОМАЙЗЕР МОНЕТ
    check_coin = ri(10, 900)
    check_time = ri(0, 100)
    if Coin_count > 0:
        if check_time == 5:
            Coin_list.append(Coin.get_rect(topleft=(check_coin, 0)))
            Coin_count -= 1
    if Coin_list:
        for (i, Coin_idx) in enumerate(Coin_list):
            screen.blit(Coin, Coin_idx)
            if Coin_idx.y <= 430:
                Coin_idx.y += Coin_speed
            if Coin_idx.colliderect(player_rect):
                Coin_list.pop(i)
                points += 1
                CoinS.play()
    if points == 10:
        screen.blit(labal_win, (250, 350))
        FinalS.play()




    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()





    clock.tick(45)


