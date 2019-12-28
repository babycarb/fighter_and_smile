1  #!/usr/bin/env python
2  # -*- coding: utf-8 -*-
3  # @File  : ship.py
4  # @Author: JO_KAAN
5  # @Date  : 2019/6/15
6  # @Desc  :

import sys
import pygame
from settings import Settings
from ship import *
import game_functions as gf
from pygame.sprite import Group
from alien import *
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # 初始化游戏对象
    pygame.init()
    ai_settings = Settings()

    # 设置屏幕大小
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasiion")

    play_button = Button(ai_settings,screen,"play")

    # 创建一艘飞船
    ship = Ship(ai_settings,screen)

    # 创建一个用于储存子弹的编组
    bullets = Group()

    # 创建一个外星人编组
    aliens = Group()

    gf.creat_fleet(ai_settings,screen,ship,aliens)

    # 创建一个用于储存游戏统计信息的实例,并创建积分板
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)

    # 开始游戏的主要循环
    while True:
        # 监听键盘以及鼠标的事件
        gf.check_events(ai_settings,screen,ship,bullets,stats,play_button,aliens,sb)

        if stats.game_active:
            # 飞船移动
            ship.updata()

            # 子弹移动
            gf.update_bullets(bullets,aliens,screen,ship,ai_settings,sb,stats)

            # 外星人移动
            gf.update_aliens(ai_settings, aliens, ship, stats, screen, bullets,sb)

        # 屏幕重绘
        gf.updata_screen(ai_settings,screen,ship,bullets,aliens,play_button,stats,sb)


run_game()