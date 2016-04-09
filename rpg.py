# coding: utf-8
"""
Julian Loreti
JL12k

Game Server
"""

from socket import *
from classes import *
import threading


def handle_client(c):
	attacking = false


	c.send("Enter your character's name: ")
	name = c.recv(25)
	c.send("Are you a CodeWarrior or 1337H4x0r? Enter [c] or [h]: ")
	playertype = c.recv(4)
	while (playertype != "c" or playertype != "h"):
		c.send("Invalid type. Enter [c] or [h]: ")
		playertype = c.recv(4)
	
	#set up board
	gameboard = [[" " for x in range(5)] for x in range(5)]
	
	#pick player type
	if (playertype == "c"):
		human = CodeWarrior() 
	else:
		human = second()
		
	#set position
	human.set_position(2,0)
	
	#Evil Robot initialization
	robot1 = EvilRobot("Evilrobot1",gameboard)
	robot2 = EvilRobot("Evilrobot2",gameboard)
	robot3 = EvilRobot("Evilrobot3",gameboard)
	robot4 = EvilRobot("Evilrobot4",gameboard)
	
	#rat trap set up
	ratrow = -1
	ratcolumn = -1
	while ((row < 0 or column < 0) or (row == 2 and column == 0) or (gameboard[row][column] != " " )):
		row = randint(0,4)
		colummn = randint(0,4)
		gameboard[row][colummn] = "R"
		
	#set backpack
	while ((row < 0 or column < 0) or (row == 2 and column == 0) or (gameboard[row][column] != " " )):
		row = randint(0,4)
		colummn = randint(0,4)
		gameboard[row][colummn] = "B"
	
	#Gameboard is now set up!!
	
	
	c.send("It’s a dark and stormy night. One unfortunate Computer Science student has fallen asleep on the Love 105 suites couch while cramming for their upcoming final. They head down to the Majors Lab to gather their belongings before heading home. They approach the lab and encounter a strange sight: the lab is empty and dark...but the door is open. The power must have been knocked out by the storm. The brave little CS student enters the dark room to find their backpack...")
	while(1):
	
		c.send(">")
		input = c.recv(25)
		line1 = input.split(' ')
		
		if (line1[0] == go):
			if (line1[1] == "N" or line1[1] == "n" or (line1[1] == "E" or line1[1] == "e") or (line1[1] == "W" or line1[1] == "w") or (line1[1] == "S" or line1[1] == "s") ):
				temp = human.go(direction.upper(), gameboard, attacking)
				if (temp == "e"):
					c.send(human.get_name() + " has encountered an Evil Robot. It appears to have assembled itself out ofspare parts. Prepare to fight!")
				
				#moved a spot with nothing there
				elif (temp == ""):
					y = human.get_position()
					gameboard[y[0]][y[1]] = "P"
					
				#backpack found: winner
				elif(temp == "w"):
					c.send(human.get_name() + "Congratulations, Caitlin found their backpack!!!")
					c.send("And so, our hero safely makes their way to the exit. Luckily, Caitlin made it out alive this time. But onething is for sure: Caitlin will never put off studying for their final exams ever again.")
					break
				
				#rat trap hit: dead
				elif(temp == "d"):
					c.send(human.get_name() + "ran into one of those legendary mechanical rat traps in the Love basement. RIP.")
					break
					
				else:
					#print message
					c.send(temp)
			else:
				c.send("Direction is not valid. Try again!")
				
		elif (line1[0] == health):
			c.send(human.health())
		
		elif (line1[0] == help):
			c.send(human.help())
		
		elif (line1[0] == attack):
			if (attacking == false):
				c.send(human.get_name() + "doesn’t see anything worth attacking")
			else:
			
				t = human.get_position()
			
				rt1 = robot1.get_position()
				rt2 = robot2.get_position()
				rt3 = robot3.get_position()
				rt4 = robot4.get_position()
				if (t[0] == rt1[0] and t[1]==rt1[1]):
					z = checkattack(human, robot1, attacking, c)
					if (z == 0):
						robot1.dead()
						
				elif (t[0] == rt2[0] and t[1]==rt2[1]):
					z = checkattack(human, robot2, attacking, c)
					if (z == 0):
						robot2.dead()
						
				elif (t[0] == rt3[0] and t[1]==rt3[1]):
					z = checkattack(human, robot3, attacking, c)
					if (z == 0):
						robot3.dead()
						
				elif (t[0] == rt4[0] and t[1]==r4[1]):
					z = checkattack(human, robot4, attacking, c)
					if (z == 0):
						robot4.dead()
			
				else:
					c.send("ERROR")
			
				if (z == -1):
					break;
				
		elif (line1[0] == quit):
			c.send(human.quit())
			break;
	
	
def checkattack(human, robot1, attacking, c):
	human.attack(robot1,attacking)
	if (robot1.get_health() == 0):
		c.send("Evil Robot has crashed! " + human.get_name() + " wins!")
		attacking = false
		gameboard[t[0]][t[1]] = "P"
		return 0
					
	robot1.attack(human)
	if (human.get_health() == 0):
	#Game Over 
		c.send(human.get_name() + " epic backpack search has come to an end. RIP.")	
		return -1
	
	return 1
			
					
if __name__ == "__main__":
	# Create IPv4 TCP socket
	s = socket(AF_INET, SOCK_STREAM)
	# Bind to localhost:9700
	s.bind(("",9000))
	s.listen(5)
	while True:
		c,a = s.accept()
		# Handle client connection in a new thread. 
		t=threading.Thread(target=handle_client, args=(c,))
		t.start()