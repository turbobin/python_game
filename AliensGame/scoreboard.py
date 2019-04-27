import pygame
from pygame.sprite import Group
from AliensGame.ship import Ship


class ScoreBoard():
    """显示得分信息的类"""

    def __init__(self, ai_set, screen, stats):
        """初始化变量属性"""
        self.ai_set = ai_set
        self.screen = screen
        self.stats = stats
        self.screen_rect = screen.get_rect()

        # 显示得分信息使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始得分图像
        self.prep_score()
        self.prep_level()
        self.prep_high_score()
        self.prep_ships()

    def prep_level(self):
        """将等级转换为渲染的图像"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
                                            self.text_color, self.ai_set.bg_color)

        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_score(self):
        """将得分转换为一副渲染的图像"""
        score = round(self.stats.score, -1)  # -1：将数圆整到10的整数倍；-2：圆整到100的整数倍...
        score_str = "{:,}".format(score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.ai_set.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """将最高得分转换为渲染的图像"""
        high_score = round(self.stats.high_score, -1)  # -1：将数圆整到10的整数倍；
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, self.ai_set.bg_color)

        # 将得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 10

    def prep_ships(self):
        """显示还余下多少飞船"""
        self.ships = Group()
        # 飞船数大于3时显示3条飞船
        if self.stats.ships_left > 3:
            num = 3
        else:
            num = self.stats.ships_left

        for ship_num in range(num):
            ship = Ship(self.ai_set, self.screen)
            ship.rect.x = 10 + (8 + ship.rect.width) * ship_num
            ship.rect.y = 5
            self.ships.add(ship)

    def show_score(self):
        """在屏幕上显示得分，等级"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.ships.draw(self.screen)
