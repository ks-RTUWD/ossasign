import os
import pang
import miner
import dong
import random
import pygame
##############################################################
# 기본 초기화 (반드시 해야 하는 것들)

def assamble():
    pygame.init()
    ###############################################################
    curr_score =0
    screen_width = 900 # 가로 크기
    screen_height = 500 # 세로 크기
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("kangsan's game")

    clock = pygame.time.Clock()

    current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
    image_path = os.path.join(current_path, "images") # images 폴더 위치 반환


    background = pygame.image.load(os.path.join(image_path, "backinit.jpg"))
    name1 = pygame.image.load(os.path.join(image_path, "pang.png"))
    name2 = pygame.image.load(os.path.join(image_path, "miner.png"))

    name4 = pygame.image.load(os.path.join(image_path, "dongback.png"))
    character =pygame.image.load(os.path.join(image_path, "character.png"))

    character_size = character.get_rect().size
    character_width=character_size[0]
    character_height=character_size[1]
    character_x_pos = (screen_width-character_width)/2
    character_y_pos = screen_height-character_height

    name1_size = name1.get_rect().size
    name2_size = name2.get_rect().size

    name4_size = name4.get_rect().size

    name1_width=name1_size[0]
    name1_height=name1_size[1]
    name2_width=name2_size[0]
    name2_height=name2_size[1]

    name4_width=name4_size[0]
    name4_height=name4_size[1]

    name1_x_pos = 0
    name1_y_pos = 0

    name2_x_pos = name2_width*2 -40
    name2_y_pos = 0


    name4_x_pos = name2_width*3+50
    name4_y_pos = 0

    to_x = 0
    to_y = 0
    character_speed = 0.6

    running = True
    moretime = 0
    def setposinit():
        character_x_pos = (screen_width - character_width) / 2
        character_y_pos = screen_height - character_height
        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos

    while running:
        if moretime:
            assamble()
        dt = clock.tick(60)
        print("fps : " + str(clock.get_fps()))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                    to_x -= character_speed
                elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                    to_x += character_speed
                elif event.key == pygame.K_UP: # 캐릭터를 오른쪽으로
                    to_y -= character_speed
                elif event.key == pygame.K_DOWN: # 캐릭터를 오른쪽으로
                    to_y += character_speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    character_to_x = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    to_y = 0

        character_x_pos += to_x * dt
        character_y_pos += to_y * dt

        if character_x_pos <0:
            character_x_pos=0
        elif character_x_pos > screen_width-character_width:
            character_x_pos = screen_width-character_width
        if character_y_pos < 0:
            character_y_pos = 0
        elif character_y_pos > screen_height - character_height:
            character_y_pos = screen_height - character_height

        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos

        name1_rect = name1.get_rect()
        name1_rect.left = name1_x_pos
        name1_rect.top = name1_y_pos

        name2_rect = name2.get_rect()
        name2_rect.left = name2_x_pos
        name2_rect.top = name2_y_pos

        name4_rect = name4.get_rect()
        name4_rect.left = name4_x_pos
        name4_rect.top = name4_y_pos

        if character_rect.colliderect(name1_rect):
            setposinit()
            print("팡게임")
            pang.pang()
            moretime = 1
        if character_rect.colliderect(name2_rect):
            print("광산")
            miner.miner()
            moretime = 1
        if character_rect.colliderect(name4_rect):
            print("똥")
            dong.dong()
            moretime = 1


        screen.blit(background, (0, 0))
        screen.blit(character, (character_x_pos, character_y_pos))
        screen.blit(name1, (name1_x_pos, name1_y_pos))
        screen.blit(name2, (name2_x_pos, name2_y_pos))

        screen.blit(name4, (name4_x_pos, name4_y_pos))

        pygame.display.update()
    pygame.quit()

assamble()
