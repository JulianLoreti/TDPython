from classes import *
import sys, time
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Game(QWidget):

	def __init__(self):
		super(Game, self).__init__()
		self.initUI()

	def dragEnterEvent(self, e):
		e.accept()

	def dropEvent(self, e):
		# get the relative position from the mime data
		mime = e.mimeData().text()
		x, y = map(int, mime.split(','))

		#if player gold > 200 else print no enough gold
		# copy
		# so create a new button
		temp = Tower('', self,40,50,"./images/tower1.png")
		# move it to the position adjusted with the cursor position at drag
		temp.move(e.pos()-QPoint(x, y))
		# show it
		temp.show()
		temp.set_flag(False)
		# set the drop action as Copy
		e.setDropAction(Qt.CopyAction)

		e.accept()

	def initUI(self):               
		self.resize(950,612)
		self.move(50,50)
		self.setWindowTitle('Tower Defense')
		palette	= QPalette()
		palette.setBrush(QPalette.Background,QBrush(QPixmap("./images/bg.PNG")))
		self.setAcceptDrops(True)
		
		tower1 = Tower('', self, 30,50, "./images/tower1.png")
		tower2 = Tower('', self, 40,60, "./images/tower2.png")
		tower3 = Tower('', self, 50,70, "./images/tower3.png")
	

		nextButton = QLabel()
		nextButton.setPixmap(QPixmap("./images/next.png"))
		startButton = QLabel()
		startButton.setPixmap(QPixmap("./images/start.png"))

		vbox = QVBoxLayout()
		#vbox.addWidget(nextButton)
		#vbox.addWidget(startButton)
		vbox.addStretch(2)
		vbox.addWidget(tower1)
		vbox.addWidget(tower2)
		vbox.addWidget(tower3)
		vbox.addStretch(5)
		self.setLayout(vbox)
		#sidebar.setPalette(palette1)

	#sidebar.addWidget(tower2)
	#sidebar.addWidget(tower2)


		self.setPalette(palette)
		self.show()

	

	def mousePressEvent(self, QMouseEvent):
		print QMouseEvent.pos()

	def mouseReleaseEvent(self, QMouseEvent):
		cursor = QCursor()
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
		
	app = QApplication(sys.argv)
	ex = Game()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
