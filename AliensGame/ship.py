import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_set, screen):
        """初始化飞船，并设置其初始位置"""
        super().__init__()
        self.screen = screen
        self.ai_set = ai_set

        # 加载飞船图像，并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 使每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """初始化飞船位置"""
        self.center = self.screen_rect.centerx

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_set.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_set.ship_speed

        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
