"""
Game Configuration Settings
Modify these values to customize the Pong game behavior.
"""

# Display Settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Colors (RGB values)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Game Object Sizes
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 90
BALL_SIZE = 20

# Game Speed Settings
PADDLE_SPEED = 5
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
MAX_BALL_SPEED = 8

# AI Settings
AI_REACTION_DELAY = 10  # Pixels of "dead zone" for AI paddle
AI_ENABLED_BY_DEFAULT = True

# Game Features
PROGRESSIVE_SPEED = True  # Ball speeds up during rallies
SPEED_INCREASE_FACTOR = 1.05
SCORE_FLASH_DURATION = 30  # Frames to flash score when points scored

# File Settings
STATS_FILE = "game_stats.json"
REPORT_FILE_PREFIX = "game_report_"

# Controls (pygame key constants)
# Player 1 Controls
PLAYER1_UP = "w"
PLAYER1_DOWN = "s"

# Player 2 Controls (when AI disabled)
PLAYER2_UP = "up"
PLAYER2_DOWN = "down"

# Game Controls
TOGGLE_AI_KEY = "a"
QUIT_KEY = "escape"

# Font Settings
SCORE_FONT_SIZE = 74
INSTRUCTION_FONT_SIZE = 36

# Performance Settings
ENABLE_CONSOLE_OUTPUT = True  # Set to False to disable print statements
ENABLE_STATISTICS = True      # Set to False to disable stats collection 