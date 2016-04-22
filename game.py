from jclasses import *

class Game(QMainWindow):

	def __init__(self):
		super(Game, self).__init__()
		self.move(200, 50) 
		self.setFixedSize(960, 624)
		self.setWindowTitle('Tower Defense')
		self.setWindowIcon(QIcon( ICON ))
		self.setAcceptDrops(True)

		palette = QPalette()
		background = QPixmap( BG_PIC )
		palette.setBrush(QPalette.Background, QBrush(background))
		self.setPalette(palette)
		self.initUI()

	def initUI(self):
		frame = QWidget()
		frame.resize(960, 624)
		self.status = QStatusBar()
		self.setStatusBar(self.status)
		
		self.setCentralWidget(frame)
		self.grid = QGridLayout()
		frame.setLayout(self.grid)

		# Welcome Name Input Dialog Box
		name, accept = QInputDialog.getText(self, 'Tower Defense', 'Enter your name:')
		if not accept:
			name = "No Name"
		self.human = Player(str(name))
		print "Made Player Object"

		# Initialize GUI board 
		self.gameBoard = [["-" for x in range(20)] for x in range(13)]
		InitializeBoard(1, self.gameBoard)
		temp = QSpacerItem(48, 48, 0, 0)
		for h in range(14):
			for w in range(21):
				self.grid.addItem(temp, h, w, 1, 1)

		# Print Command Line board
		for row in self.gameBoard:
			for e in row:
				print e,
			print

		# Declare Tower Objects (0, 0) for buttons
		self.tower1 = Tower1("", self, 0, 0)
		self.tower2 = Tower2("", self,0, 0)
		self.tower3 = Tower3("", self,0, 0)

		myFont = QFont("San Serif", pointSize=12, weight=80)
		
		name_label = QLabel()
		name_label.setText(str(self.human.name))
		name_label.setFont(myFont)

		level_label = QLabel()
		level_label.setText("Round " + str(self.human.round))
		level_label.setFont(myFont)

		toolbar = QLabel()
		toolbar.setPixmap(QPixmap( TB_PIC ))

		heart_pic = QLabel()
		heart_pic.setPixmap(QPixmap( HRT_PIC ))

		gold_pic = QLabel()
		gold_pic.setPixmap(QPixmap( GLD_PIC ))

		self.next_btn = QPushButton()
		self.next_btn.setIcon(QIcon( NX_PIC ))
		self.next_btn.setFlat(True)
		self.next_btn.setIconSize(QSize(168,48))
		self.next_btn.clicked.connect(self.NextButton)

		self.start_btn = QPushButton()
		self.start_btn.setIcon(QIcon( ST_PIC ))
		self.start_btn.setFlat(True)
		self.start_btn.setIconSize(QSize(168,48))
		self.start_btn.clicked.connect(self.GameStart)
		
		self.grid.addWidget(toolbar, 0, 0, 8, 4)
		self.grid.addWidget(name_label, 0, 0, 1, 4)
		self.grid.addWidget(level_label, 1, 0, 1, 4)
		self.grid.addWidget(heart_pic, 2, 0, 2, 2)
		self.grid.addWidget(gold_pic, 3, 0, 2, 2)
		self.grid.addWidget(self.tower1, 4, 0, 2, 2)
		self.grid.addWidget(self.tower2, 5, 0, 2, 2)
		self.grid.addWidget(self.tower3, 6, 0, 2, 2)
		self.grid.addWidget(self.next_btn, 13, 12, 1, 3)
		self.grid.addWidget(self.start_btn, 13, 16, 1, 3)

		frame.show()
		self.show()

	def GameStart(self):
		#countdown = QLabel()
		#countdown.setGeometry(400, 250)
		#Cfont = QFont(pointSize=11, weight=75, bold=True)
		#countdown.setFont(Cfont)
		print "Start Button"

	def NextButton(self):
		print "Next Button"

#################### MOUSE EVENTS ############################################	
	def dragEnterEvent(self, e):
		e.accept()

	def dropEvent(self, e):
		# get the relative position from the mime data
		mime = e.mimeData().text()
		temp1 = mime.split(',')
		counter = 0
		for i in temp1:
			counter = counter + 1
			if counter == 3:
				pic = i

		temp1.removeAt(counter-1)
		x, y = map(int, temp1)
		#check if placement is okay
		moveSpot = e.pos()-QPoint(x,y)
		print "MoveSpot: " + str(moveSpot)
 		checkx = int(moveSpot.x() / 48)
 		checky = int(moveSpot.y() / 48)
 
 		if self.gameBoard[checky][checkx] == "-":
	    #and player gold > 200 else print no enough gold
			x = (((moveSpot.x() ) /48)*48)
			y = (((moveSpot.y() ) /48)*48)

			# copy
			# so create a new label
			if pic == T1_PIC:
				newTower = Tower1("", self,y,x)
				print T1_PIC
				self.gameBoard[checky][checkx] = "1"

			elif pic == T2_PIC:
				newTower = Tower2("", self,y,x)
				self.gameBoard[checky][checkx] = "2"

			else:
				newTower = Tower3("", self,y,x)
				self.gameBoard[checky][checkx] = "3"

			# move it to the position adjusted with the cursor position at drag
			newTower.move(QPoint(x, y))
			newTower.show()
			newTower.flag = False

			# set the drop action as Copy
			e.setDropAction(Qt.CopyAction)

			self.status.clearMessage()
			e.accept()

		else:
			self.status.showMessage("Invalid Tower Location", 5000)
			print "Invalid Location"


 		print "TESTING"
 		for row in self.gameBoard:
			for ap in row:
				print ap,
			print

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
		gameBoard[6][14] = "T"
		gameBoard[6][15] = "R"
		gameBoard[6][16] = "R"
		gameBoard[6][17] = "R"
		gameBoard[6][18] = "R"
		gameBoard[6][19] = "E"
		
		# Blocked Areas
		for y in range(13):
			for x in range(4):
				gameBoard[y][x] = "*"

		for y in range(2):
			for x in range(5,9):
				gameBoard[y][x] = "*"

		for y in range(4):
			for x in range(16,20):
				gameBoard[y][x] = "*"

		for y in range (8,13):
			for x in range(17,20):
				gameBoard[y][x] = "*"

		for x in range(11,20):
			gameBoard[12][x] = "*"

	else:
		print "ERROR\n"

def main():
	app = QApplication(sys.argv)
	GUI = Game()
	GUI.show()
	app.exec_()
	sys.exit()


if __name__ == '__main__':
	main()