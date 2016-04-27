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
		
		self.path = PATH
		self.location = [y_loc, x_loc]
		self.pic = pic
		self.health = hp
		self.speed = spd
		self.next_loc = (loc for loc in self.path) # Path location generator

		self.setPixmap(QPixmap(pic))
		self.resize(48,48)
	
	# generate the next place in the path
	def next(self):
		temp = self.next_loc.next()
		print "TEMP: " + str(temp) 
		self.position = [temp[1]*48, temp[0]*48]
		return temp
		
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

class Worker(QThread):
	def __init__(self, enemy, player):
		QThread.__init__(self)
		self.run(enemy, player)

	def __del__(self):
		self.wait()

	def run(self, enemy, player):
		for i in range(len(PATH)):
			pos = enemy.next()
			enemy.move( pos[1]*48, pos[0]*48 )

			# if enemy is within tower range add it to tower's list
			#for tower in towers:
				# for loc in range:
					# if enemy is in range:
						# shootemlizbeth

			enemy.show()
			time.sleep(1/enemy.speed)
			QCoreApplication.processEvents()
		
		enemy.hide() 
		player.hp -= 1 # decrement players health (pass that in as well)
		#show this change
		
		self.terminate() # exit thread

#############################################################