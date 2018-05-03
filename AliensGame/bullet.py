import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""在飞船的位置创建一个子弹的类"""
	
	def __init__(self,ai_set,screen,ship):
		"""在飞船所处的位置创建一个对象"""
		super().__init__() #初始化父类的属性
		self.screen = screen
		
		#在(0,0)处创建一个子弹的矩形，再设置正确的位置
		self.rect = pygame.Rect(0,0,ai_set.bullet_width,
								ai_set.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		#存储用小数表示的子弹位置
		self.y = float(self.rect.y)
		
		self.color = ai_set.bullet_color
		self.speed = ai_set.bullet_speed

	def update(self,ai_set,bullets,aliens,stats,sb):
		"""向上移动子弹"""
		#更新表示子弹位置的小数值
		self.y -= self.speed
		#更新表示子弹的rect的位置
		self.rect.y = self.y
		
		# 删除已消失的子弹
		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
		# ~ print(len(bullets))
				
		#检查是否有子弹击中了外星人,True表示删除碰撞的对应元素
		collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
		
		#子弹击中外星人时，累计得分
		if collisions:
			for aliens_list in collisions.values():
# 				print(ali)
				
				stats.score += ai_set.alien_points * len(aliens_list)
				sb.prep_score()
			
			# 检查是否诞生了最高得分
			if stats.score > stats.high_score:
				stats.high_score = stats.score
				sb.prep_high_score()
		
	def draw_bullet(self):
		"""在屏幕上绘制子弹"""
		pygame.draw.rect(self.screen,self.color,self.rect)
