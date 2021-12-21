import pygame
import random
#똥피하기 게임

def dong():
    pygame.init()
    # 화면크기설정
    screen_width = 480
    screen_height = 640
    screen = pygame.display.set_mode((screen_width, screen_height))
    # 화면 타이틀 설정
    pygame.display.set_caption("kang game")

    clock = pygame.time.Clock()

    # 배경이미지 불러오기
    background = pygame.image.load(r"C:\Users\kangsan\Desktop\pppython\images/background.png")
    character = pygame.image.load(r"C:\Users\kangsan\Desktop\pppython\images/dongdonggy.png")
    character_size = character.get_rect().size
    character_width = character_size[0]
    character_height = character_size[1]
    character_x_pos = (screen_width - character_width) / 2
    character_y_pos = screen_height - character_height

    to_x = 0
    character_speed = 0.6

    # 적
    enemy = pygame.image.load(r"C:\Users\kangsan\Desktop\pppython\images/dong.png")
    enemy_size = enemy.get_rect().size
    enemy_width = enemy_size[0]
    enemy_height = enemy_size[1]
    enemy_x_pos = random.randint(0, screen_width - enemy_width)
    enemy_y_pos = 0
    enemy_speed = 0.9

    # pont
    game_font = pygame.font.Font(None, 40)

    total_time = 10
    start_ticks = pygame.time.get_ticks()
    # 이벤트루프
    running = True
    while running:
        dt = clock.tick(60)
        print("fps : " + str(clock.get_fps()))
        for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_x -= character_speed
                elif event.key == pygame.K_RIGHT:
                    to_x += character_speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0
        character_x_pos += to_x * dt

        if character_x_pos < 0:
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width

        enemy_y_pos += enemy_speed * dt
        if enemy_y_pos > screen_height:
            enemy_y_pos = 0
            enemy_x_pos = random.randint(0, screen_width - enemy_width)

        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos

        enemy_rect = enemy.get_rect()
        enemy_rect.left = enemy_x_pos
        enemy_rect.top = enemy_y_pos

        if character_rect.colliderect(enemy_rect):
            print("충돌했어요")
            running = False

        screen.blit(background, (0, 0))
        screen.blit(character, (character_x_pos, character_y_pos))
        screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

        elapse_time = (pygame.time.get_ticks() - start_ticks) / 1000

        timer = game_font.render(str(int(total_time - elapse_time)), True, (255, 255, 255))
        screen.blit(timer, (10, 10))

        if total_time - elapse_time <= 0:
            print("타임아웃")
            running = False

        pygame.display.update()

