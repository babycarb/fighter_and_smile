1  #!/usr/bin/env python
2  # -*- coding: utf-8 -*-
3  # @File  : ship.py
4  # @Author: JO_KAAN
5  # @Date  : 2019/6/15
6  # @Desc  :
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self,ai_settings,screen):
        """初始化飞船，并设置其起始位置"""
        super(Ship,self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每一个新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船中的属性center中储存最小数值
        self.center = float(self.rect.centerx)
        self.botto = float(self.rect.bottom)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def updata(self):
        # 根据移动标志来调整飞船的位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left >0:
            self.center -=self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top >0:
            self.botto -=self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.botto +=self.ai_settings.ship_speed_factor

        # 根据self.centerx更新rect对象
        self.rect.centerx = self.center
        self.rect.bottom = self.botto

    def blitime(self):

        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
        self.botto = self.screen_rect.bottom
