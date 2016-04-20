import sys, time
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class myLabel(QLabel):

	def __init__(self,a,b,pic):
		super(myLabel, self).__init__(a,b)
		self.setSizePolicy ( QSizePolicy.Preferred, QSizePolicy.Preferred)
		self.setMaximumWidth(48)
		self.setMaximumHeight(48)
		self.resize(48,48)
		#self.setFlat(True)
		self.setPixmap(QPixmap(pic))
		self.flag = True
		self.towerpic = pic

	def set_flag(self, a):
		self.flag = a

	def mouseMoveEvent(self, e):
		if e.buttons() != Qt.LeftButton:
			return

		if (self.flag == True):
			# write the relative cursor position to mime data
			mimeData = QMimeData()
			# simple string with 'x,y'
			mimeData.setText('%d,%d,%s' % (e.x(), e.y(), self.towerpic))

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


	def mousePressEvent(self, e):
		if (self.flag == False):
			if e.button() == Qt.LeftButton:
				print "pressed"


############################################################
class Tower(myLabel):
	def __init__(self,a,b,attack,speed,pic):
		self.attack = attack
		self.speed = speed
		self.position = []
		myLabel.__init__(self,a,b, pic)

	def set_flag(self, a):
		return myLabel.set_flag(self,a)

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

#############################################################
class Player:
	def __init__(self,name):
		self.name = name
		self.gold = 200
		self.lives = 100
		self.round = 0

	def set_name(self, a):
		self.name = a

	def get_name(self):
		return self.name

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
		self.round = a

	def get_round(self):
		return self.round
		
#############################################################
class Wave:
	def __init__(self, player, roundNum, enemiesList, gameb):
		self.round = roundNum
		self.enemies = 0

	def send_enemy(self, player):
		if(self.round == 1):
			self.enemies = self.round * 25
		else:
			self.enemies = int(float(self.enemies * 1.2))

		for i in range(self.enemies):
			e = Enemy()
			e.enemy_start(gameb)
#need more gui to finish this stuff

#############################################################
class Enemy:
	def __init__(self):
		self.health = 100
		self.speed = 1

	def enemy_start(self, gameBoard):
	
		locationStart = gameBoard[0][14]
		i = 0
		j = 14
		plusCount = 0
		#57 spaces
		count = 1
		location = gameBoard[i][j]
		while(count <= 56):
			if(location == "D"):
				i = i + 1

			#time.sleep(0.2)
			if(location == "L"):
				j = j - 1

			#time.sleep(0.2)

			if(location == "R"):
				j = j + 1

			#time.sleep(0.2)
			if(location == "U"):
				i = i - 1

			#time.sleep(0.2)
			if(plusCount == 0 and location == "T"):
				plusCount = 1
				i = i - 1
				location = "U"

			#time.sleep(0.2)
			if(plusCount == 1 and location == "T"):
				j = j + 1
				print "2nd T location", location
				location = "R"
				#time.sleep(0.2)
				if(location == "E"):
					print "life lost"
					break

			count = count + 1
			location = gameBoard[i][j]

#############################################################

class XQLabel(QLabel):

    def __init(self, parent):
        QLabel.__init__(self, parent)

    def mouseReleaseEvent(self, ev):
        self.emit(SIGNAL('clicked()'))