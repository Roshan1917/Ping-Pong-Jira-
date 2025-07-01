import pygame
import sys
import random
import json
from datetime import datetime

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 90
BALL_SIZE = 20
PADDLE_SPEED = 5
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

class GameStats:
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0
        self.games_played = 0
        self.start_time = datetime.now()
        
    def to_dict(self):
        return {
            "player1_score": self.player1_score,
            "player2_score": self.player2_score,
            "games_played": self.games_played,
            "session_duration": str(datetime.now() - self.start_time),
            "timestamp": datetime.now().isoformat()
        }

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        
    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= PADDLE_SPEED
            
    def move_down(self):
        if self.rect.bottom < WINDOW_HEIGHT:
            self.rect.y += PADDLE_SPEED
            
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, BALL_SIZE, BALL_SIZE)
        self.speed_x = BALL_SPEED_X * random.choice([-1, 1])
        self.speed_y = BALL_SPEED_Y * random.choice([-1, 1])
        
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        # Bounce off top and bottom walls
        if self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT:
            self.speed_y = -self.speed_y
            
    def reset(self):
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.speed_x = BALL_SPEED_X * random.choice([-1, 1])
        self.speed_y = BALL_SPEED_Y * random.choice([-1, 1])
        
    def draw(self, screen):
        pygame.draw.ellipse(screen, WHITE, self.rect)

class PongGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pong Game")
        self.clock = pygame.time.Clock()
        
        # Game objects
        self.player1 = Paddle(30, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.player2 = Paddle(WINDOW_WIDTH - 30 - PADDLE_WIDTH, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.ball = Ball()
        
        # Game state
        self.stats = GameStats()
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)
        
        # AI for player 2
        self.ai_enabled = True
        
        # Visual feedback
        self.score_flash = {"player1": 0, "player2": 0}
        self.last_scorer = None
        
    def handle_input(self):
        keys = pygame.key.get_pressed()
        
        # Player 1 controls (W/S)
        if keys[pygame.K_w]:
            self.player1.move_up()
        if keys[pygame.K_s]:
            self.player1.move_down()
            
        # Player 2 controls (UP/DOWN arrows) - only if AI is disabled
        if not self.ai_enabled:
            if keys[pygame.K_UP]:
                self.player2.move_up()
            if keys[pygame.K_DOWN]:
                self.player2.move_down()
                
    def ai_move_player2(self):
        if self.ai_enabled:
            # Simple AI: follow the ball
            paddle_center = self.player2.rect.centery
            ball_center = self.ball.rect.centery
            
            if paddle_center < ball_center - 10:
                self.player2.move_down()
            elif paddle_center > ball_center + 10:
                self.player2.move_up()
                
    def check_collisions(self):
        # Ball collision with paddles
        if self.ball.rect.colliderect(self.player1.rect):
            if self.ball.speed_x < 0:  # Only reverse if ball is moving towards paddle
                self.ball.speed_x = abs(self.ball.speed_x)
                # Add slight speed increase for excitement
                self.ball.speed_x = int(min(self.ball.speed_x * 1.05, 8))
                print("Player 1 hit!")
                
        elif self.ball.rect.colliderect(self.player2.rect):
            if self.ball.speed_x > 0:  # Only reverse if ball is moving towards paddle
                self.ball.speed_x = -abs(self.ball.speed_x)
                # Add slight speed increase for excitement
                self.ball.speed_x = int(max(self.ball.speed_x * 1.05, -8))
                print("Player 2 hit!")
            
        # Ball goes off screen - SCORING HAPPENS HERE
        if self.ball.rect.right < 0:  # Ball went off left side
            self.stats.player2_score += 1
            self.score_flash["player2"] = 30  # Flash for 30 frames
            self.last_scorer = "player2"
            print(f"SCORE! Player 2: {self.stats.player2_score}")
            self.ball.reset()
            # Reset ball speed
            self.ball.speed_x = BALL_SPEED_X * random.choice([-1, 1])
            self.ball.speed_y = BALL_SPEED_Y * random.choice([-1, 1])
            
        elif self.ball.rect.left > WINDOW_WIDTH:  # Ball went off right side
            self.stats.player1_score += 1
            self.score_flash["player1"] = 30  # Flash for 30 frames
            self.last_scorer = "player1"
            print(f"SCORE! Player 1: {self.stats.player1_score}")
            self.ball.reset()
            # Reset ball speed
            self.ball.speed_x = BALL_SPEED_X * random.choice([-1, 1])
            self.ball.speed_y = BALL_SPEED_Y * random.choice([-1, 1])
            
    def draw(self):
        self.screen.fill(BLACK)
        
        # Draw center line
        pygame.draw.aaline(self.screen, WHITE, (WINDOW_WIDTH // 2, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT))
        
        # Draw game objects
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)
        self.ball.draw(self.screen)
        
        # Draw scores with flashing effect
        player1_color = GREEN if self.score_flash["player1"] > 0 else WHITE
        player2_color = GREEN if self.score_flash["player2"] > 0 else WHITE
        
        player1_score_text = self.font.render(str(self.stats.player1_score), True, player1_color)
        player2_score_text = self.font.render(str(self.stats.player2_score), True, player2_color)
        
        self.screen.blit(player1_score_text, (WINDOW_WIDTH // 4, 50))
        self.screen.blit(player2_score_text, (3 * WINDOW_WIDTH // 4, 50))
        
        # Reduce flash timers
        if self.score_flash["player1"] > 0:
            self.score_flash["player1"] -= 1
        if self.score_flash["player2"] > 0:
            self.score_flash["player2"] -= 1
        
        # Draw instructions
        instructions = [
            "Player 1: W/S keys",
            f"Player 2: {'AI' if self.ai_enabled else 'Arrow keys'}",
            "Press 'A' to toggle AI",
            "Press 'ESC' to quit",
            "SCORE when opponent misses!"
        ]
        
        for i, instruction in enumerate(instructions):
            text = self.small_font.render(instruction, True, WHITE)
            self.screen.blit(text, (10, WINDOW_HEIGHT - 150 + i * 25))
        
        # Draw copyright notice in bottom-right corner
        copyright_text = self.small_font.render("© Ronaldo", True, WHITE)
        copyright_rect = copyright_text.get_rect()
        copyright_rect.bottomright = (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 10)
        self.screen.blit(copyright_text, copyright_rect)
            
        pygame.display.flip()
        
    def save_game_stats(self):
        """Save game statistics to a file"""
        try:
            with open('game_stats.json', 'w') as f:
                json.dump(self.stats.to_dict(), f, indent=2)
            print("Game stats saved to game_stats.json")
        except Exception as e:
            print(f"Error saving stats: {e}")
        
    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_a:
                        self.ai_enabled = not self.ai_enabled
                        print(f"AI {'enabled' if self.ai_enabled else 'disabled'}")
                        
            self.handle_input()
            self.ai_move_player2()
            self.ball.move()
            self.check_collisions()
            self.draw()
            
            self.clock.tick(60)
            
        # Save stats before quitting
        self.save_game_stats()
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = PongGame()
    game.run() 