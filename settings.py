1  #!/usr/bin/env python
2  # -*- coding: utf-8 -*-
3  # @File  : settings.py
4  # @Author: JO_KAAN
5  # @Date  : 2019/6/14
6  # @Desc  :

class Settings():
    """存储《打飞机》的所有的设置的类"""
    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置

        self.screen_width = 1360
        self.screen_height = 768
        self.bg_color = (147,112,219)

        # 飞船设置
        self.ship_speed_factor = 1.6
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 0.9
        self.bullet_width = 6
        self.bullet_height = 100
        self.bullet_color = 255,20,147
        self.bullet_allowed = 30

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1

        # 外星人点数提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction为1表示向右，为-1表示向左
        self.fleet_direction = 1

        # 记分
        self.ailen_points = 50



    def increase_speed(self):
        # 提高速度设置以及外星人点数
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.ailen_points = int(self.ailen_points * self.score_scale)

