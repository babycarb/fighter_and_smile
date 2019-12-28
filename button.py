1  #!/usr/bin/env python
2  # -*- coding: utf-8 -*-
3  # @File  : button.py
4  # @Author: JO_KAAN
5  # @Date  : 2019/6/16
6  # @Desc  :

import pygame.font

class Button():

    def __init__(self,ai_settings,screen,msg):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸以及其它属性
        self.width,self.height = 200,50
        self.button_color = (218,165,32)
        self.text_color = (	178,34,34)
        self.font = pygame.font.SysFont(None,48)

        # 创建按钮的reck对象，并且使其居中
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        # 按钮的标签只需要创建一次
        self.prep_msg(msg)

    def prep_msg(self,msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 绘制一个用颜色填充的按钮，在绘制文本
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
