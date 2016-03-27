############################################################
class Tower:
	def __init__(self,attack,speed):
		self.attack = attack
		self.speed = speed
		self.position = []

	def get_attack(self):
		return self.attack

	def set_speed(self, a):
		self.speed = a

	def get_position(self):
		return self.position

	def set_position(self, row, column):
		self.position[0] = row
		self.position[1] = column

	def get_speed(self):
		return self.speed

	def set_attack(self, a):
		self.attack = a

############################################################
class arrowTower(Tower):
	def __init__(self,attack, speed, numName):
		self.name = "arrow" + str(numName)
		Tower.__init__(self,attack,speed)

	def get_attack(self):
		return Tower.get_attack(self)

	def set_speed(self, a):
		Tower.set_speed(self,a)

	def get_position(self):
		return Tower.get_position(self)

	def set_position(self, row, column):
		Tower.set_position(self,row,column)

	def get_speed(self):
		return Tower.get_speed(self)

	def set_attack(self, a):
		Tower.set_attack(self,a)

#############################################################
class Player:
	def __init__(self):
		self.gold = 200
		self.lives = 100
		self.level = 0
		self.currentRound = 0

	def set_gold(self, a):
		self.gold = a

	def get_gold(self):
		return self.gold

	def set_lives(self, a):
		self.lives = a

	def get_lives(self):
		return self.lives

	def set_level(self, a):
		self.level = a

	def get_level(self):
		return self.level

	def set_round(self, a):
		self.currentRound = a

	def get_round(self):
		return self.currentRound

