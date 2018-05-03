import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""创建一个外星人的类"""
	
	def __init__(self,ai_set,screen):
		"""初始化外星人并设置其初始位置"""
		super().__init__()
		self.screen = screen
		self.ai_set = ai_set
		
		#加载外星人图像
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		
		#设置外星人最初的位置--屏幕左上角
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#储存外星人的准确位置
		self.x = float(self.rect.x)
		
	def check_edges(self):
		"""如果外星人位于屏幕边缘，返回True"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
		
	def update(self):
		"""向左或向右移动外星人"""
		self.x += (self.ai_set.alien_speed * 
						self.ai_set.fleet_direction)
		# ~ print (self.x)
		self.rect.x = self.x 
	
	def blitme(self):
		"""在指定位置绘制外星人"""
		self.screen.blit(self.image,self.rect)
	
