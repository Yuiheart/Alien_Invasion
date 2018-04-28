
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )   #screen是一个surface对象，是屏幕的一部分，用于显示游戏元素
    pygame.display.set_caption("Alien Invasion")

    # 创建开始按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建第一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个编组来存储子弹
    bullets = Group()

    # 创建外星人编组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen,  ship, aliens)

    # 创建游戏状态对象
    stats = GameStats(ai_settings)

    # 创建记分板对象
    sb = Scoreboard(ai_settings, screen, stats)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
