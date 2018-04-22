import json
class GameStats():
	"""跟踪游戏的统计信息"""
	
	def __init__(self,ai_set):
		"""初始化统计信息"""
		self.ai_set = ai_set
		#游戏刚启动时处于活跃状态
		self.game_active = False
		#最高得分
		try:
			with open("high_score.json") as f_obj:
				self.high_score = json.load(f_obj)
		except FileNotFoundError:
			self.high_score = 0
						
# 		self.high_score = 0
		
		self.reset_stats()
		
	def reset_stats(self):
		"""初始化随游戏可能变化的统计信息"""
		self.ships_left = self.ai_set.ship_limit
		self.score = 0
		self.level = 1
		
