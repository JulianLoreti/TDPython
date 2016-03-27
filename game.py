import pygame
from pygame.locals import *
from classes import *
import time
import sys

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


#if __name__ == "__main__":


pygame.init()

gameBoard = [["-" for x in range(20)] for x in range(13)]

#initialize board 
InitializeBoard(1, gameBoard)
human = Player()
#Print the underlying board
for row in gameBoard:
	for e in row:
		print e,
	print

displayW = 950
displayH = 612
BACKGROUND_COLOR = (0,0,0)

gameDisplay = pygame.display.set_mode((displayW, displayH))
gameDisplay.fill(BACKGROUND_COLOR)
pygame.display.set_caption('Tower Defense')

#display lives, etc
img_lives = pygame.image.load("heart.PNG").convert()
img_gold = pygame.image.load("gold.jpg").convert()
myfont = pygame.font.SysFont("comicsansms", 18)
myfont1 = pygame.font.SysFont("comicsansms", 22)

# render text
lives = "Lives: " + str(human.get_lives())
gold = "Gold: " + str(human.get_gold())
rounds = "Round " + str(human.get_round())
lives_text = myfont.render(lives, 1, (255,255,255))
gold_text = myfont.render(gold, 1, (255,255,255))
round_text = myfont1.render(rounds, 1, (255,255,255))


while True:
	#mouse_position = mousepos = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			print "BUTTON PRESSED!\n"

	background = pygame.image.load('bg.PNG')
	gameDisplay.blit(background, [0, 0])
	gameDisplay.blit(img_lives, (0,0))
	gameDisplay.blit(img_gold, (0,26))
	gameDisplay.blit(lives_text, (26, 0))
	gameDisplay.blit(gold_text, (26, 26))
	gameDisplay.blit(round_text, (0, 52))

	pygame.display.flip()

	if event.type == pygame.QUIT:
		sys.exit()