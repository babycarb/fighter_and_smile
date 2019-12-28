1  #!/usr/bin/env python
2  # -*- coding: utf-8 -*-
3  # @File  : game_functions.py
4  # @Author: JO_KAAN
5  # @Date  : 2019/6/15
6  # @Desc  :

import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_events(ai_settings,screen,ship,bullets,stats,play_button,aliens,sb):
    """响应按键以及鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 处理键盘按键按下去事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)

        # 处理键盘按键松开事件
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(stats,play_button,mouse_x,mouse_y,ai_settings,screen,ship,aliens,bullets,sb)


def updata_screen(ai_settings,screen,ship,bullets,aliens,play_button,stats,sb):
    # 每次循环都会重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitime()
    aliens.draw(screen)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 显示得分
    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应按下按键"""
    if event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_w:
        ship.moving_up = True
    elif event.key == pygame.K_s:
        ship.moving_down = True
    elif event.key == pygame.K_j:
        fire_buttle(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup_events(event,ship):
    """响应放开按钮"""
    if event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_a:
        ship.moving_left = False
    elif event.key == pygame.K_w:
        ship.moving_up = False
    elif event.key == pygame.K_s:
        ship.moving_down = False

def update_bullets(bullets,aliens,screen,ship,ai_settings,sb,stats):
    bullets.update()
    # 删除屏幕外面的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 检察是否有子弹击中外星人
    # 如果是这样，就删除对应的子弹以及外星人
    check_bullet_alien_collisions(bullets,aliens,screen,ship,ai_settings,sb,stats)

def fire_buttle(ai_settings,screen,ship,bullets):
    """如果还没有到达限制，就打一炮"""
    # 创建新的子弹，并将其加入到编组bullets里面
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def creat_fleet(ai_settings,screen,ship,aliens):
    """创建一个外星人群"""
    # 创建一个外星人，并计算一行可以容纳多少外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    # 创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            creat_alien(ai_settings, screen, aliens, alien_number,row_number)

def get_number_aliens_x(ai_settings,alien_width):
    """计算每行可以容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (1.9 * alien_width))
    return number_aliens_x

def creat_alien(ai_settings,screen,aliens,alien_number,row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(ai_settings,ship_height,alien_height):
    """计算屏幕可以放多少行外星人"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height)-ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings,aliens,ship,stats,screen,bullets,sb):
    """检查是否有外星人到达屏幕最边缘，然后更新所有的外星人的位置"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,sb)

    # 检测外星人与飞船之间的碰触
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb)


def check_bullet_alien_collisions(bullets,aliens,screen,ship,ai_settings,sb,stats):
    """响应子弹和外星人的碰撞"""
    # 删除发生碰撞的子弹以及外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.ailen_points * len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)

    if len(aliens) == 0:
        # 删除现有的子弹，加快游戏节奏，以及创建一群新的外星人
        bullets.empty()
        ai_settings.increase_speed()

        # 提高等级
        stats.level += 1
        sb.prep_level()

        creat_fleet(ai_settings,screen,ship,aliens)


def ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        # 将ships_left减1
        stats.ships_left -= 1

        # 更新记分牌
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.6)
    else:
        # 游戏停止
        stats.game_active = False
        # 显示鼠标的光标
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,sb):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船与外星人碰触一样进行处理
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb)
            break


def check_play_button(stats,play_button,mouse_x,mouse_y,ai_settings,screen,ship,aliens,bullets,sb):
    """在玩家单击play的时候开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:

        # 隐藏光标
        pygame.mouse.set_visible((False))

        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()

        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        sb.prep_score()
        sb.prep_level()
        sb.prep_high_score()
        sb.prep_ships()

        # 清空外星人列表
        aliens.empty()
        bullets.empty()

        # 创建一群新外星人，并让飞船居中
        creat_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

def check_high_score(stats,sb):
    """检查是否诞生了新的最高分数"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

