import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )   #screen是一个surface对象，是屏幕的一部分，用于显示游戏元素
    pygame.display.set_caption("Alien Invasion")

    # 创建第一艘飞船
    ship = Ship(screen)

    # 设置背景色
    bg_color = (230,230,230)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        pygame.display.flip()

run_game()
