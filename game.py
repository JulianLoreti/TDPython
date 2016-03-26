import pygame
from pygame.locals import *
import time
import sys

#skeleton of game set up
if __name__ == "__main__":


	pygame.init()

	displayW = 950
	displayH = 612
	BACKGROUND_COLOR = (0,0,0)

	gameDisplay = pygame.display.set_mode((displayW, displayH))
	gameDisplay.fill(BACKGROUND_COLOR)
	pygame.display.set_caption('Tower Defense')


	while True:
		#mouse_position = mousepos = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				pass

		background = pygame.image.load('bg.PNG')
		gameDisplay.blit(background, [0, 0])

		pygame.display.flip()

		if event.type == pygame.QUIT:
			pygame.quit()

	quit()