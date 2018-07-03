# -*- coding: utf-8 -*-
class Settings():
	"""存储所有设置的类"""	
	
	def __init__(self):
		"""初始化游戏的设置"""
		#屏幕设置
		self.screen_width = 1000
		self.screen_heigth = 600
		self.screen_size = (1000,600)
		self.bg_color = (230,230,230)
		
		#飞船设置
		self.ship_speed = 1
		self.ship_limit = 5
		
		#子弹设置
		# ~ self.bullet_speed = 2
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		
		#外星人设置
		# ~ self.alien_speed = 0.5
		# ~ self.fleet_speed = 10
		
		self.fleet_direction = 1
		
		#重置变量
		self.init_set()

	def init_set(self):
		self.alien_points = 10	#每个外星人值多少分
		self.bullet_width = 3
		self.ship_speed = 1
		self.bullet_speed = 2
		self.alien_speed = 0.5
		self.fleet_speed = 10
	
	#提高难度等级
	def increase_speed(self):
		self.bullet_width *= 1.5
		self.ship_speed   *= 1.1
		self.bullet_speed *= 1.2
		self.alien_speed  += 0.1
		# ~ self.fleet_speed  += 2
		self.alien_points += 5
		self.alien_points = round(self.alien_points)
		print("每个外星人值多少分："+str(self.alien_points))
