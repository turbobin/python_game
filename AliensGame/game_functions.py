import sys
import pygame
import json
from AliensGame.bullet import Bullet
from AliensGame.alien import Alien
from time import sleep


def check_event(stats, ai_set, screen, play_button, ship, bullets, aliens, sb):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 退出前保存最高得分，以便下次打开时加载
            save_high_score(stats)
            sys.exit()
        # 点击Play按钮时
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, ai_set, aliens, bullets,
                              screen, ship, play_button, mouse_x, mouse_y, sb)

        elif event.type == pygame.KEYDOWN:
            # ~ 设置退出键
            if event.key == pygame.K_q:
                # 退出前保存最高得分，以便下次打开时加载
                save_high_score(stats)
                sys.exit()

            if event.key == pygame.K_RIGHT:
                """向右移动飞船"""
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                """向左移动飞船"""
                ship.moving_left = True
            elif event.key == pygame.K_a:
                # 创建一颗子弹，并将其加入到编组
                new_bullet = Bullet(ai_set, screen, ship)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                """向右移动飞船"""
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                """向左移动飞船"""
                ship.moving_left = False


def save_high_score(stats):
    """将最高得分保存到文件中"""
    with open("high_score.json", 'w') as f_obj:
        json.dump(stats.high_score, f_obj)


def check_play_button(stats, ai_set, aliens, bullets, screen, ship,
                      play_button, mouse_x, mouse_y, sb):
    """单击Play按钮开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if (button_clicked and not stats.game_active):
        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 重置游戏
        stats.reset_stats()
        stats.game_active = True

        # 重置记分牌图像
        sb.prep_score()
        sb.prep_level()
        sb.prep_ships()

        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        creat_fleet(ai_set, screen, aliens)
        ship.center_ship()

        ai_set.init_set()


def creat_fleet(ai_set, screen, aliens):
    """创建外星人群"""
    alien = Alien(ai_set, screen)  # 创建一个外星人
    alien_width = alien.rect.width  # 外星人宽度

    # 计算一行可容纳多少个外星人，外星人间距为外星人宽度
    availablea_space_x = ai_set.screen_width - 2 * alien_width
    num_aliens_x = int(availablea_space_x / (2 * alien_width))

    # 创建一群外星人(4行)
    for row in range(4):
        creat_alien(ai_set, screen, aliens, row, num_aliens_x, alien_width)


def creat_alien(ai_set, screen, aliens, row, num_aliens_x, alien_width):
    """创建一行外星人"""
    for alien_num in range(num_aliens_x):
        # 创建一个外星人并将其加入到当前行
        alien = Alien(ai_set, screen)
        alien.x = alien_width + 2 * alien_width * alien_num

        alien.rect.x = alien.x

        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row
        aliens.add(alien)


def update_aliens(ai_set, aliens, bullets, screen, ship, stats, sb):
    check_fleet_edges(ai_set, aliens)
    # 更新所有外星人的位置
    aliens.update()  # 对编组调用update()，将会自动使每个外星人调用update()

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_set, aliens, bullets, screen, ship, stats, sb)

    # 检查是否有外星人到达底端
    check_aliens_bottom(ai_set, aliens, bullets, screen, ship, stats, sb)


def check_fleet_edges(ai_set, aliens):
    """有外星人触碰边缘时，将外星人下移，并改变移动方向"""
    for alien in aliens.sprites():
        if alien.check_edges():
            for alien in aliens.sprites():
                alien.rect.y += ai_set.fleet_speed
            ai_set.fleet_direction *= -1
            break;


def ship_hit(ai_set, aliens, bullets, screen, ship, stats, sb):
    # ~ print ("Ship hit !!")
    if stats.ships_left > 0:
        # 剩余飞船数-1
        stats.ships_left -= 1

        sb.prep_ships()
        # ~ print (stats.ships_left)

        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        creat_fleet(ai_set, screen, aliens)
        ship.center_ship()

        # 暂停
        sleep(1)
    else:
        stats.game_active = False
        # 显示光标
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_set, aliens, bullets, screen, ship, stats, sb):
    """检查是否有外星人到达了底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_set, aliens, bullets, screen, ship, stats, sb)
            break


def update_screen(ai_set, screen, ship, aliens, bullets,
                  stats, play_button, sb):
    """更新屏幕图像，并切换到新屏幕"""
    # 每次循环时都重汇屏幕
    screen.fill(ai_set.bg_color)

    # 显示得分
    sb.show_score()

    # 如果游戏处于非活跃状态，就显示Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    # ~ alien.blitme()
    aliens.draw(screen)

    # ~ 让最近绘制的屏幕可见
    pygame.display.flip()
