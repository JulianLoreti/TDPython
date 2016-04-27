from classes import *

class Game(QMainWindow):

	def __init__(self):
		super(Game, self).__init__()
		self.move(200, 50) 
		self.towers = []
		self.enemies = []
		self.setFixedSize(960, 624)
		self.setWindowTitle('Tower Defense')
		self.setWindowIcon(QIcon( ICON ))
		self.setAcceptDrops(True)
		self.isClicked_Holder = QLabel()
		self.currentlyClickedTower = self.isClicked_Holder

		palette = QPalette()
		background = QPixmap( BG_PIC )
		palette.setBrush(QPalette.Background, QBrush(background))
		self.setPalette(palette)
		self.initUI()

	def initUI(self):
		frame = QWidget()
		frame.resize(960, 624)
		
		self.setCentralWidget(frame)
		self.grid = QGridLayout()
		frame.setLayout(self.grid)

		# Welcome Name Input Dialog Box
		name, accept = QInputDialog.getText(self, 'Tower Defense', 'Enter your name:')
		if not accept or name == "":
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

		# GUI Elements
		toolbar = QLabel("", frame)
		toolbar.setPixmap(QPixmap( TB_PIC ))
		self.grid.addWidget(toolbar, 0, 0, 8, 4)

		heart_pic = QLabel("", frame)
		heart_pic.setPixmap(QPixmap( HRT_PIC ))
		heart_pic.move(20, 55)
		heart_pic.resize(60, 60)

		gold_pic = QLabel("", frame)
		gold_pic.setPixmap(QPixmap( GLD_PIC ))
		gold_pic.move(20, 100)
		gold_pic.resize(60, 60)

		# Declare tower buttons as objects
		self.tower1 = Tower1("1", self, 0, 0)
		self.tower1.move(20, 165)
		
		self.tower2 = Tower2("2", self, 0, 0)
		self.tower2.move(20, 225)
		
		self.tower3 = Tower3("3", self, 0, 0)
		self.tower3.move(20, 285)

		self.the_btn = QPushButton()
		self.the_btn.setIcon(QIcon( ST_PIC ))
		self.the_btn.setFlat(True)
		self.the_btn.setIconSize(QSize(168,48))
		self.the_btn.clicked.connect(self.GameStart)
		self.grid.addWidget(self.the_btn, 13, 17, 1, 3)

		# Text Elements
		TitleFont = QFont("San Serif", pointSize=12, weight=80)
		InfoFont = QFont("San Serif", pointSize=8, weight=50)
		
		name_str = str(self.human.name)
		self.name_label = QLabel(name_str, frame)
		self.name_label.setFont(TitleFont)
		self.name_label.move(20, 15)

		level_str = "Round "+str(self.human.round)
		self.level_label = QLabel(level_str, frame)
		self.level_label.setFont(TitleFont)
		self.level_label.move(20, 40)

		hpstr = str(START_LIVES)
		self.hp_num = QLabel(hpstr, frame)
		self.hp_num.setFont(TitleFont)
		self.hp_num.move(75, 72)

		gldstr = str(START_GOLD)
		self.gold_num = QLabel(gldstr, frame)
		self.gold_num.setFont(TitleFont)
		self.gold_num.move(75, 114)

		t1str = "Cost:"+str(T1_VAL)+"\nDamage:"+str(T1_DAM)+"\nRange:"+str(T1_RAN)+"\nSpeed:"+str(T1_SPD)
		t1_info = QLabel(t1str, frame)
		t1_info.setFont(InfoFont)
		t1_info.resize(80, 60)
		t1_info.move(75, 160)

		t2str = "Cost:"+str(T2_VAL)+"\nDamage:"+str(T2_DAM)+"\nRange:"+str(T2_RAN)+"\nSpeed:"+str(T2_SPD)
		t2_info = QLabel(t2str, frame)
		t2_info.setFont(InfoFont)
		t2_info.resize(80, 60)
		t2_info.move(75, 220)
		
		t3str = "Cost:"+str(T3_VAL)+"\nDamage:"+str(T3_DAM)+"\nRange:"+str(T3_RAN)+"\nSpeed:"+str(T3_SPD)
		t3_info = QLabel(t3str, frame)
		t3_info.setFont(InfoFont)
		t3_info.resize(80, 60)
		t3_info.move(75, 280)

		hint = QLabel("*Drag to place towers*", frame)
		hint.setFont(InfoFont)
		hint.resize(144, 48)
		hint.move(20, 325)

		frame.show()
		self.show()

	#tied the moveEnemies command to the start button for now just to try and get
	#the graphics to move one grid spot at a time on press
	#also to get tower clicks to run smoothly we need to thread the movement of guys
	def GameStart(self):
		print "Start Game Button"
		self.the_btn.setIcon(QIcon( NX_PIC )) # change the button to next
		self.the_btn.setEnabled(False) # make start not clickable

		self.human.round += 1
		self.level_label.setText( "Round "+str(self.human.round) )

		number = int(NUM_ENEM * ROUND_MULT * self.human.round)
		print number

		for i in range(number):
			temp = Enemy1("",self,0,0)
			temp.move(672,0)
			print "Making enemy " + str(1)
			self.enemies.append(temp) # add to enemies list
			
			temp.show()
			self.show()
			
			Worker(temp, self.human) # Enemy moving thread
			self.hp_num = self.human.lives
			self.show()
			
			time.sleep(5)	# wait to create new enemy

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
		
		# check if placement is okay
		moveSpot = e.pos()-QPoint(x,y)
		print "MoveSpot: " + str(moveSpot)
 		checkx = int(moveSpot.x() / 48)
 		checky = int(moveSpot.y() / 48)
 
 		if self.gameBoard[checky][checkx] == "-":
			x = (((moveSpot.x() ) /48)*48)
			y = (((moveSpot.y() ) /48)*48)

			# if so create a new label
			if pic == T1_PIC and self.human.gold >= T1_VAL:
				newTower = Tower1("", self,y,x)
				self.gameBoard[checky][checkx] = "1"
				self.human.gold -= T1_VAL

			elif pic == T2_PIC and self.human.gold >= T2_VAL:
				newTower = Tower2("", self,y,x)
				self.gameBoard[checky][checkx] = "2"
				self.human.gold -= T2_VAL

			elif pic == T3_PIC and self.human.gold >= T3_VAL:
				newTower = Tower3("", self,y,x)
				self.gameBoard[checky][checkx] = "3"
				self.human.gold -= T3_VAL

			else:
				print "Not Enough Gold"
				return

			# Update the GUI gold figure.
			self.gold_num.setText(str(self.human.gold))

			# move it to the position adjusted with the cursor position at drag
			newTower.move(QPoint(x, y))
			newTower.show()
			newTower.flag = False
			self.towers.append(newTower)

			# set the drop action as Copy
			e.setDropAction(Qt.CopyAction)
			e.accept()

		else:
			print "Invalid Location"

 		print "TESTING"
 		for row in self.gameBoard:
			for ap in row:
				print ap,
			print


	def paintEvent(self, event):
		super(Game, self).paintEvent(event) 
		qp = QPainter()
		qp.begin(self)
		for i in self.towers:
			if i.isClicked == True:
				qp.setPen(Qt.NoPen)
				qp.setBrush(QColor(100, 100, 100, 75))
				qp.drawEllipse(QPoint(i.position[1] + 24, i.position[0] + 24), i.range, i.range)
				print "Drew ellipse"
		qp.end()

	def mousePressEvent(self, e):
		spot = e.pos()
		print "Spot.x " + str(spot.x()) + "       Spot.y " + str(spot.y())
		if self.currentlyClickedTower == self.isClicked_Holder:
			for i in self.towers:
				if((spot.x() / 48) == (i.position[1]/48) and (spot.y()/48) == (i.position[0]/48)):
					i.isClicked = True
					self.currentlyClickedTower = i
					self.repaint()
					print "Worked"
		else:
			self.currentlyClickedTower.isClicked = False
			self.currentlyClickedTower = self.isClicked_Holder
			for i in self.towers:
				if((spot.x() / 48) == (i.position[1]/48) and (spot.y()/48) == (i.position[0]/48)):
					i.isClicked = True
					self.currentlyClickedTower = i
					print "Clicked new tower"
			self.repaint()

def InitializeBoard(a, gameBoard):
	if (a == 1):
		"""
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
		"""

		# Path
		for loc in PATH:
			print loc
			gameBoard[ loc[0] ][ loc[1] ] = "P"

		# Blocked Areas
		for y in range(13):				# left side
			for x in range(4):
				gameBoard[y][x] = "*"
		gameBoard[10][4] = "*"
		gameBoard[11][4] = "*"

		for y in range(2):				# top middle
			for x in range(5,9):
				gameBoard[y][x] = "*"

		for y in range(4):				# top right
			for x in range(17,20):
				gameBoard[y][x] = "*"
		gameBoard[0][16] = "*"
		gameBoard[1][16] = "*"
		gameBoard[4][18] = "*"
		gameBoard[4][19] = "*"

		for y in range (8,13):			# bottom right
			for x in range(17,20):
				gameBoard[y][x] = "*"
                                                                                                                                                                                                                                                                                                                                                                                                                                                          
		for x in range(20):				# bottom
			gameBoard[12][x] = "*"

		gameBoard[0][15] = "*" # Start Sign
		gameBoard[5][19] = "*" # Exit Sign

	else:
		print "ERROR\n"

def main():
	app = QApplication(sys.argv)
	"""
	start = time.time() 
	splash = QSplashScreen(QPixmap("./images/splash.png"))
	splash.show()
	while time.time() - start < 2:
		time.sleep(0.001)
		app.processEvents()

	splash.close()
	"""
	GUI = Game()
	GUI.show()
	app.exec_()
	sys.exit()

if __name__ == '__main__':
	main()
