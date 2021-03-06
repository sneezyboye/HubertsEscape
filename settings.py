# define some colors (R, G, B)
WHITE = (255, 255, 255)
DARKER_WHITE = (180, 180, 180)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 246, 237)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "oooaaaaaooooo"
BGCOLOR = DARKGREY

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_FRICTION = -0.11
PLAYER_ACC = 20
PLAYER_GRAVITY = 500
JUMP_SPEED = 450
BOUNCE_SPEED = 900