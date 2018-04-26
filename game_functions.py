import sys
import pygame

def check_events(ship):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
                ship.moving_left = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
                ship.moving_right = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    pygame.display.flip()

