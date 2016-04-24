import sys, time
from random import random
from balancing import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *	

###########################################################

class Tower(QLabel):
	def __init__(self, a, b, y_loc, x_loc, pic, dam, ran, spd):
		super(Tower, self).__init__(a,b)
		
		self.position = [y_loc, x_loc]
		self.pic = pic
		self.damage = dam
		self.range = ran
		self.speed = spd
		self.isClicked = False
		self.clickable = True
		self.flag = True

		self.setPixmap(QPixmap(pic))
		#self.setSizePolicy (QSizePolicy.Preferred, QSizePolicy.Preferred)
		#self.setMaximumWidth(48)
		#self.setMaximumHeight(48)
		self.resize(48,48)
		
	def mouseMoveEvent(self, e):
		if e.buttons() != Qt.LeftButton:
			return
			
		if self.clickable and self.flag:
			# write the relative cursor position to mime data
			mimeData = QMimeData()
			# simple string with 'x,y'
			mimeData.setText('%d,%d,%s' % (e.x(), e.y(), self.pic))

			# let's make it fancy. we'll show a "ghost" of the button as we drag
			# grab the button to a pixmap
			pixmap = QPixmap.grabWidget(self)

			# below makes the pixmap half transparent
			painter = QPainter(pixmap)
			painter.setCompositionMode(painter.CompositionMode_DestinationIn)
			painter.fillRect(pixmap.rect(), QColor(0, 0, 0, 127))
			painter.end()

			# make a QDrag
			drag = QDrag(self)
			# put our MimeData
			drag.setMimeData(mimeData)
			# set its Pixmap
			drag.setPixmap(pixmap)
			# shift the Pixmap so that it coincides with the cursor position
			drag.setHotSpot(e.pos())

			# start the drag operation
			# exec_ will return the accepted action from dropEvent
			if drag.exec_(Qt.CopyAction | Qt.MoveAction) == Qt.MoveAction:
				print 'moved'
			else:
				print 'copied'

	""""def mousePressEvent(self, e):
		if (self.flag == False):
			if e.button() == Qt.LeftButton:
				self.isClicked = True
				print "Clicked"""
	
class Tower1(Tower):
	def __init__(self, a, b, y_loc, x_loc):
		Tower.__init__(self, a, b, y_loc, x_loc, T1_PIC, T1_DAM, T1_RAN, T1_SPD)

class Tower2(Tower):
	def __init__(self, a, b, y_loc, x_loc):
		Tower.__init__(self, a, b, y_loc, x_loc, T2_PIC, T2_DAM, T2_RAN, T2_SPD)

class Tower3(Tower):
	def __init__(self, a, b, y_loc, x_loc):
		Tower.__init__(self, a, b, y_loc, x_loc, T3_PIC, T3_DAM, T3_RAN, T3_SPD)

###########################################################

class Enemy(QLabel):
	def __init__(self, a, b, y_loc, x_loc, pic, hp, spd):
		super(Enemy, self).__init__(a,b)
		
		self.location = [y_loc, x_loc]
		self.pic = pic
		self.health = hp
		self.speed = spd
		self.next_loc = (loc for loc in PATH) # Path location generator

		self.setPixmap(QPixmap(pic))
		#self.setSizePolicy (QSizePolicy.Preferred, QSizePolicy.Preferred)
		#self.setMaximumWidth(48)
		#self.setMaximumHeight(48)
		self.resize(48,48)

	
	# generate the next place in the path
	def next(self):
		return self.next_loc.next()

		"""
		self.locationStart = gameBoard[0][14]
		self.i = 0
		self.j = 14
		self.plusCount = 0
		self.time = E1_SPD

		#57 spaces
		#runs through ryan's command one step every call 
		self.location = gameBoard[self.i][self.j]
		if self.round != 0:
			if(self.location == "D"):
				self.i = self.i + 1

			if(self.location == "L"):
				self.j = self.j - 1


			if(self.location == "R"):
				self.j = self.j + 1

			if(self.location == "U"):
				self.i = self.i - 1

			if(self.plusCount == 0 and self.location == "T"):
				self.plusCount = 1
				self.i = self.i - 1
				self.location = "U"

			if(self.plusCount == 1 and self.location == "T"):
				self.j = self.j + 1
				print "2nd T location", self.location
				self.location = "R"
				if(self.ocation == "E"):
					print "life lost"

		print "TESTING"
 		for row in gameBoard:
			for ap in row:
				print ap,
			print

		#changes position to new square in pixels
		self.position = [self.j* 48, self.i*48]
		"""
		
class Enemy1(Enemy):
	def __init__(self, a, b, y_loc=0, x_loc=0):
		Enemy.__init__(self, a, b, y_loc, x_loc, E1_PIC, E1_HP, E1_SPD)

class Enemy2(Enemy):
	def __init__(self, a, b, y_loc=0, x_loc=0):
		Enemy.__init__(self, a, b, y_loc, x_loc, E2_PIC, E2_HP, E2_SPD)

class Enemy3(Enemy):
	def __init__(self, a, b, y_loc=0, x_loc=0):
		Enemy.__init__(self, a, b, y_loc, x_loc, E3_PIC, E3_HP, E3_SPD)

#############################################################

class Player:
	def __init__(self, name=DEFAULT):
		self.name = name
		self.gold = START_GOLD
		self.lives = START_LIVES
		self.round = 0

#############################################################

class Wave:
	def __init__(self, player, roundNum, enemiesList, board):
		self.round = roundNum
		self.enemies = 0

	def send_enemy(self, player):
		if(self.round == 1):
			self.enemies = 25
		else:
			self.enemies = int(float(self.enemies * ROUND_MULT))

		for i in range(self.enemies):
			num = random(3)
			if num == 0:
				e = Enemy1(START_LOC[0], START_LOC[1])
			e = Enemy()
			e.enemy_start(board)

#############################################################
