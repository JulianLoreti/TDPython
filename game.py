from classes import *

class Game(QMainWindow):

	def __init__(self):
		super(Game, self).__init__()
		self.move(200, 50) 
		self.setFixedSize(960, 624)
		self.setWindowTitle('Tower Defense')
		self.setWindowIcon(QIcon("./images/icon.png"))
		self.setAcceptDrops(True)

		palette = QPalette()
		background = QPixmap("./images/newbg.png")
		palette.setBrush(QPalette.Background, QBrush(background))
		self.setPalette(palette)
		self.initUI()

	def initUI(self):               
		frame = QWidget()
		frame.resize(960, 624)
		self.setCentralWidget(frame)
		self.grid = QGridLayout()
		frame.setLayout(self.grid)

		#initialize board 
		self.gameBoard = [["-" for x in range(20)] for x in range(13)]
		InitializeBoard(1, self.gameBoard)
		#Print the underlying board
		for row in self.gameBoard:
			for e in row:
				print e,
			print

		#try to setup and stretch the grid?
		temp = QSpacerItem(48, 48, 0, 0)
		#tiles = [[ " " for h in range(14)] for w in range(21)]
		for h in range(14):
			for w in range(21):
				self.grid.addItem(temp, h, w, 1, 1)

		# Declare the Tower Objects
		tower1 = Tower('', self, 30, 50, "./images/tower1.png")
		tower2 = Tower('', self, 40, 60, "./images/tower2.png")
		tower3 = Tower('', self, 50, 70, "./images/tower3.png")

		name, accept = QInputDialog.getText(self, 'Tower Defense', 'Enter your name:')
		if not accept:
			name = "No Name"
		self.human = Player(str(name))
		print "Made Player Object"

		myFont = QFont("San Serif", pointSize=12, weight=80)
		
		name_label = QLabel()
		name_label.setText("Name: " + str(self.human.get_name()))
		name_label.setFont(myFont)

		level_label = QLabel()
		level_label.setText("Round: " + str(self.human.get_round()))
		level_label.setFont(myFont)

		toolbar = QLabel()
		toolbar.setPixmap(QPixmap("./images/toolbar.png"))

		heart_pic = QLabel()
		heart_pic.setPixmap(QPixmap("./images/heart.png"))

		gold_pic = QLabel()
		gold_pic.setPixmap(QPixmap("./images/gold.png"))

		next_btn = XQLabel()
		next_btn.setPixmap(QPixmap("./images/next.png"))
		#next_btn.mouseReleaseEvent.connect()

		start_btn = XQLabel()
		start_btn.setPixmap(QPixmap("./images/start.png"))
		#next_btn.mouseReleaseEvent.connect()

		self.grid.addWidget(toolbar, 0, 0, 8, 4)
		self.grid.addWidget(name_label, 0, 0, 1, 4)
		self.grid.addWidget(level_label, 1, 0, 1, 4)
		self.grid.addWidget(heart_pic, 2, 0, 2, 2)
		self.grid.addWidget(gold_pic, 3, 0, 2, 2)
		self.grid.addWidget(tower1, 4, 0, 2, 2)
		self.grid.addWidget(tower2, 5, 0, 2, 2)
		self.grid.addWidget(tower3, 6, 0, 2, 2)
		self.grid.addWidget(next_btn, 13, 12, 1, 4)
		self.grid.addWidget(start_btn, 13, 16, 1, 4)

		frame.show()
		self.show()

	def GameStart(self):
		countdown = QLabel()
		countdown.setGeometry(400, 250)
		Cfont = QFont(pointSize=11, weight=75, bold=True)
		countdown.setFont(Cfont)

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
		if self.gameBoard[y][x] == "-":
			#if player gold > 200 else print no enough gold
			# copy
			# so create a new label
			if pic == "./images/tower1.png":
				temp = Tower('', self, 30,50,"./images/tower1.png")

			elif pic == "./images/tower2.png":
				temp = Tower('', self,40,60,"./images/tower2.png")

			else:
				temp = Tower('', self,50,70,"./images/tower3.png")
			# move it to the position adjusted with the cursor position at drag
			
			moveSpot = e.pos()-QPoint(x,y)
			print "MoveSpot: " + str(moveSpot)

			x = ((moveSpot.x() /48)*48)
			y = ((moveSpot.y() /48)*48)
			print "New x: " + str(x) + "     New y: " + str(y) 
			#x = int(x / 48) +1
			#y = int(y / 48)
			#self.grid.addWidget(temp,y,x,2,2)
			temp.move(QPoint(x, y))
			# show it
			temp.show()
			temp.set_flag(False)
			# set the drop action as Copy
			e.setDropAction(Qt.CopyAction)

			e.accept()

	"""def mousePressEvent(self, QMouseEvent):
		print QMouseEvent.pos()

	def mouseReleaseEvent(self, QMouseEvent):
		cursor = QCursor()
		print cursor.pos()   """

def InitializeBoard(a, gameBoard):
	if (a == 1):
		#initialize the path on the self.gameBoard
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

		gameBoard[0][0] = "*"
		gameBoard[1][0] = "*"
		gameBoard[2][0] = "*"
		gameBoard[3][0] = "*"
		gameBoard[4][0] = "*"
		gameBoard[5][0] = "*"
		gameBoard[6][0] = "*"
		gameBoard[0][1] = "*"
		gameBoard[1][1] = "*"
		gameBoard[2][1] = "*"
		gameBoard[3][1] = "*"
		gameBoard[4][1] = "*"
		gameBoard[5][1] = "*"
		gameBoard[6][1] = "*"
		gameBoard[0][2] = "*"
		gameBoard[1][2] = "*"
		gameBoard[2][2] = "*"
		gameBoard[3][2] = "*"
		gameBoard[4][2] = "*"
		gameBoard[5][2] = "*"
		gameBoard[6][2] = "*"
		gameBoard[0][5] = "*"
		gameBoard[0][6] = "*"
		gameBoard[0][7] = "*"
		gameBoard[0][8] = "*"
		gameBoard[1][5] = "*"
		gameBoard[1][6] = "*"
		gameBoard[1][7] = "*"
		gameBoard[1][8] = "*"
	else:
		print "ERROR\n"

if __name__ == '__main__':
	app = QApplication(sys.argv)
	GUI = Game()
	GUI.show()
	sys.exit(app.exec_())
