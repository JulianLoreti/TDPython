""" Global Defaults and configuration values for game balancing and alike. """

# Player Defaults
DEFAULT = "Player1"    # If one is not provided
START_GOLD = 1000       # Player's initial gold amount (where do they earn more?)
START_LIVES = 100       # Player's initial number of Lives   
ROUNDS = 4              # Number of rounds before victory
ROUND_MULT = 1.2        # Enemy number multiplier per round

# Tower Attributes
T1_VAL = 100 # Tower 1 Cost 
T1_DAM = 20  # Tower 1 Damage
T1_RAN = 80   # Tower 1 Range  
T1_SPD = 5   # Tower 1 Speed

T2_VAL = 200 # Tower 2 Cost
T2_DAM = 15  # Tower 2 Damage
T2_RAN = 120   # Tower 2 Range  
T2_SPD = 3   # Tower 2 Speed

T3_VAL = 300 # Tower 3 Cost
T3_DAM = 30  # Tower 3 Damage
T3_RAN = 100   # Tower 3 Range  
T3_SPD = 4   # Tower 3 Speed

# Enemy Attributes
START_LOC = [0,14] # (y, x)

E1_HP = 20  # Enemy 1 Health
E1_SPD = 1  # Enemy 1 Speed

E2_HP = 20  # Enemy 2 Health
E2_SPD = 2  # Enemy 2 Speed

E3_HP = 20  # Enemy 3 Health
E3_SPD = 3  # Enemy 3 Speed

# Images
T1_PIC = "./images/tower1.png"
T2_PIC = "./images/tower2.png"
T3_PIC = "./images/tower3.png"

E1_PIC = "./images/enemy1.png"
E2_PIC = "./images/enemy2.png"
E3_PIC = "./images/enemy3.png"

BG_PIC = "./images/bg3.png"
TB_PIC = "./images/toolbar.png"
ICON = "./images/icon.png"

ST_PIC = "./images/start.png"
NX_PIC = "./images/next.png"

HRT_PIC = "./images/heart.png"
GLD_PIC = "./images/gold.png"
BUL_PIC = "./images/bullet.png"
