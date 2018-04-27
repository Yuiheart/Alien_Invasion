
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )   #screen是一个surface对象，是屏幕的一部分，用于显示游戏元素
    pygame.display.set_caption("Alien Invasion")

    # 创建第一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个编组来存储子弹
    bullets = Group()

    # 创建外星人
    aliens = Group()

    gf.create_fleet(ai_settings, screen, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
