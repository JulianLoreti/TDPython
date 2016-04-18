from classes import *
import time
import sys
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4 import QtCore

class Button(QtGui.QPushButton):

	def __init__(self,a,b):
		super(Button, self).__init__(a,b)
		self.setSizePolicy ( QSizePolicy.Preferred, QSizePolicy.Preferred)
		self.setMaximumWidth(48)
		self.setMaximumHeight(48)
		palette1 = QPalette()
		palette1.setBrush(QPalette.Background,QBrush(QtCore.Qt.transparent))
		self.setPalette(palette1)

	def mouseMoveEvent(self, e):
		if e.buttons() != QtCore.Qt.RightButton:
			return

		# write the relative cursor position to mime data
		mimeData = QtCore.QMimeData()
		# simple string with 'x,y'
		mimeData.setText('%d,%d' % (e.x(), e.y()))

		# let's make it fancy. we'll show a "ghost" of the button as we drag
		# grab the button to a pixmap
		pixmap = QtGui.QPixmap.grabWidget(self)

		# below makes the pixmap half transparent
		painter = QtGui.QPainter(pixmap)
		painter.setCompositionMode(painter.CompositionMode_DestinationIn)
		painter.fillRect(pixmap.rect(), QtGui.QColor(0, 0, 0, 127))
		painter.end()

		# make a QDrag
		drag = QtGui.QDrag(self)
		# put our MimeData
		drag.setMimeData(mimeData)
		# set its Pixmap
		drag.setPixmap(pixmap)
		# shift the Pixmap so that it coincides with the cursor position
		drag.setHotSpot(e.pos())

		# start the drag operation
		# exec_ will return the accepted action from dropEvent
		if drag.exec_(QtCore.Qt.CopyAction | QtCore.Qt.MoveAction) == QtCore.Qt.MoveAction:
			print 'moved'
		else:
			print 'copied'


	def mousePressEvent(self, e):
		QtGui.QPushButton.mousePressEvent(self, e)
		if e.button() == QtCore.Qt.LeftButton:
			print 'press'

class Game(QtGui.QWidget):

	def __init__(self):
		super(Game, self).__init__()
		self.initUI()

	def dragEnterEvent(self, e):
		e.accept()


	def dropEvent(self, e):
		# get the relative position from the mime data
		mime = e.mimeData().text()
		x, y = map(int, mime.split(','))

		if e.keyboardModifiers() & QtCore.Qt.ShiftModifier:
			# copy
			# so create a new button
			button = Button('Button', self)
			# move it to the position adjusted with the cursor position at drag
			button.move(e.pos()-QtCore.QPoint(x, y))
			# show it
			button.show()
			# store it
			self.buttons.append(button)
			# set the drop action as Copy
			e.setDropAction(QtCore.Qt.CopyAction)
		else:
			# move
			# so move the dragged button (i.e. event.source())
			e.source().move(e.pos()-QtCore.QPoint(x, y))
			# set the drop action as Move
			e.setDropAction(QtCore.Qt.MoveAction)
		# tell the QDrag we accepted it
		e.accept()


	def initUI(self):               
		self.resize(950,612)
		self.move(50,50)
		self.setWindowTitle('Tower Defense')
		palette	= QPalette()
		palette.setBrush(QPalette.Background,QBrush(QPixmap("./images/bg.PNG")))
		self.setAcceptDrops(True)
	
		tower1 = Button('', self)
		tower2 = Button('', self)
		tower3 = Button('', self)
	
		tower1.resize(48,48)
		tower1.setFlat(True)
		tower1.setAutoFillBackground(True)
		tower1.setIcon(QIcon("./images/tower1.png"))
		tower1.setIconSize(QtCore.QSize(48,48))

		tower2.resize(48,48)
		tower2.setFlat(True)
		tower2.setAutoFillBackground(True)
		tower2.setIcon(QIcon("./images/tower2.png"))
		tower2.setIconSize(QtCore.QSize(48,48))

		tower3.resize(48,48)
		tower3.setFlat(True)
		tower3.setAutoFillBackground(True)
		tower3.setIcon(QIcon("./images/tower3.png"))
		tower3.setIconSize(QtCore.QSize(48,48))

		grid = QGridLayout()
		grid.addWidget(tower1,0,0)
		grid.addWidget(tower2,1,0)
		grid.addWidget(tower3,2,0)
		self.setLayout(grid)
		#sidebar.setPalette(palette1)

	#sidebar.addWidget(tower2)
	#sidebar.addWidget(tower2)


		self.setPalette(palette)
		self.show()

	

	def mousePressEvent(self, QMouseEvent):
		print QMouseEvent.pos()

	def mouseReleaseEvent(self, QMouseEvent):
		cursor =QtGui.QCursor()
		print cursor.pos()   

def InitializeBoard(a, gameBoard):
	if (a == 1):
		#initialize the path on the gameboard
		gameBoard[0][14] = "D"
		gameBoard[1][14] = "D"
		gameBoard[2][14] = "L"
		gameBoard[2][13] = "L"
		gameBoard[2][12] = "L"
		gameBoard[2][11] = "L"
		gameBoard[2][10] = "L"
		gameBoard[2][9] = "L"
		gameBoard[2][8] = "L"
		gameBoard[2][7] = "L"
		gameBoard[2][6] = "D"
		gameBoard[3][6] = "D"
		gameBoard[4][6] = "D"
		gameBoard[5][6] = "D"
		gameBoard[6][6] = "D"
		gameBoard[7][6] = "D"
		gameBoard[8][6] = "D"
		gameBoard[9][6] = "D"
		gameBoard[10][6] = "R"
		gameBoard[10][7] = "R"
		gameBoard[10][8] = "R"
		gameBoard[10][9] = "R"
		gameBoard[10][10] = "R"
		gameBoard[10][11] = "R"
		gameBoard[10][12] = "R"
		gameBoard[10][13] = "R"
		gameBoard[10][14] = "U"
		gameBoard[9][14] = "U"
		gameBoard[8][14] = "U"
		gameBoard[7][14] = "U"
		gameBoard[6][14] = "U"
		gameBoard[5][14] = "U"
		gameBoard[4][14] = "L"
		gameBoard[4][13] = "L"
		gameBoard[4][12] = "L"
		gameBoard[4][11] = "L"
		gameBoard[4][10] = "L"
		gameBoard[4][9] = "L"
		gameBoard[4][8] = "D"
		gameBoard[5][8] = "D"
		gameBoard[6][8] = "D"
		gameBoard[7][8] = "D"
		gameBoard[8][8] = "R"
		gameBoard[8][9] = "R"
		gameBoard[8][10] = "R"
		gameBoard[8][11] = "R"
		gameBoard[8][12] = "U"
		gameBoard[7][12] = "U"
		gameBoard[6][12] = "R"
		gameBoard[6][13] = "R"
		gameBoard[6][14] = "R"
		gameBoard[6][15] = "R"
		gameBoard[6][16] = "R"
		gameBoard[6][17] = "R"
		gameBoard[6][18] = "R"
		gameBoard[6][19] = "E"
	else:
		print "ERROR\n"

def main():
	gameBoard = [["-" for x in range(20)] for x in range(13)]

	#initialize board 
	InitializeBoard(1, gameBoard)
	human = Player()
	#Print the underlying board
	for row in gameBoard:
		for e in row:
			print e,
		print
		
	app = QtGui.QApplication(sys.argv)
	ex = Game()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()