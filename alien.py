1  #!/usr/bin/env python
2  # -*- coding: utf-8 -*-
3  # @File  : alien.py
4  # @Author: JO_KAAN
5  # @Date  : 2019/6/15
6  # @Desc  :

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    """表示单个外星人的类"""
    def __init__(self,ai_settings,screen):
        """初始化外星人并设置其起始位置"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 储存外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定的位置绘制外星人"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x


    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True






