# -*- coding: utf-8 -*-
import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard

# ~ from alien import Alien

def run_game():
	# ~ 初始化游戏并创建一个屏幕对象
	pygame.init()
	
	ai_set = Settings()
	screen = pygame.display.set_mode(ai_set.screen_size)
	# ~ pygame.display.set_caption("Alien Invasion")
	pygame.display.set_caption("飞机大战")
	
	#创建Play按钮
	play_button = Button(ai_set,screen,"Play")
	
	#创建一个用于统计信息的实例,并创建记分牌
	stats = GameStats(ai_set)
	
	sb = ScoreBoard(ai_set,screen,stats)
	
	#设置背景色
	# ~ bg_color = (230,230,230)
	
	#创建一艘飞船
	ship = Ship(ai_set,screen)
	#创建一个用于存储子弹的编组
	bullets = Group()
	#创建一个外星人
	# ~ alien = Alien(ai_set,screen)
	
	#创建一群外星人
	aliens = Group()
	gf.creat_fleet(ai_set,screen,aliens)
	# ~ print (bullets)
	
	# ~ 开始游戏的主循环
	while True:
		# ~ 监视键盘和鼠标事件
		gf.check_event(stats,ai_set,screen,play_button,ship,
			bullets,aliens,sb)
		if stats.game_active:
			ship.update()
			bullets.update(ai_set,bullets,aliens,stats,sb)
			gf.update_aliens(ai_set,aliens,bullets,screen,ship,stats,sb)
			
		#如果外星人全部被消灭，则新创建一群,同时加快速度,提高等级
		if len(aliens) == 0:
			bullets.empty()
			ai_set.increase_speed()
			
			#提高等级
			stats.level += 1
			sb.prep_level()
			
			gf.creat_fleet(ai_set,screen,aliens)
			
		# ~ 更新屏幕
		gf.update_screen(ai_set,screen,ship,aliens,bullets,
			stats,play_button,sb)
		
run_game()
	
