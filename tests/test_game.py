"""
Basic tests for Pong Game functionality.
"""

import unittest
import sys
import os

# Add parent directory to path to import game modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import pygame
    pygame.init()
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False

@unittest.skipUnless(PYGAME_AVAILABLE, "pygame not available")
class TestPongGame(unittest.TestCase):
    """Test cases for Pong Game components."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        if PYGAME_AVAILABLE:
            from pong_game import GameStats, Paddle, Ball
            self.GameStats = GameStats
            self.Paddle = Paddle
            self.Ball = Ball
    
    def test_game_stats_initialization(self):
        """Test that GameStats initializes correctly."""
        stats = self.GameStats()
        self.assertEqual(stats.player1_score, 0)
        self.assertEqual(stats.player2_score, 0)
        self.assertEqual(stats.games_played, 0)
        self.assertIsNotNone(stats.start_time)
    
    def test_game_stats_to_dict(self):
        """Test GameStats to_dict method."""
        stats = self.GameStats()
        stats.player1_score = 5
        stats.player2_score = 3
        
        data = stats.to_dict()
        self.assertEqual(data["player1_score"], 5)
        self.assertEqual(data["player2_score"], 3)
        self.assertIn("session_duration", data)
        self.assertIn("timestamp", data)
    
    def test_paddle_initialization(self):
        """Test that Paddle initializes correctly."""
        paddle = self.Paddle(100, 200)
        self.assertEqual(paddle.rect.x, 100)
        self.assertEqual(paddle.rect.y, 200)
    
    def test_paddle_movement(self):
        """Test paddle movement methods."""
        paddle = self.Paddle(100, 200)
        original_y = paddle.rect.y
        
        # Test moving up
        paddle.move_up()
        self.assertLess(paddle.rect.y, original_y)
        
        # Test moving down
        original_y = paddle.rect.y
        paddle.move_down()
        self.assertGreater(paddle.rect.y, original_y)
    
    def test_ball_initialization(self):
        """Test that Ball initializes correctly."""
        ball = self.Ball()
        self.assertIsNotNone(ball.rect)
        self.assertNotEqual(ball.speed_x, 0)
        self.assertNotEqual(ball.speed_y, 0)
    
    def test_ball_movement(self):
        """Test ball movement."""
        ball = self.Ball()
        original_x = ball.rect.x
        original_y = ball.rect.y
        
        ball.move()
        
        # Ball should have moved
        self.assertNotEqual(ball.rect.x, original_x)
        self.assertNotEqual(ball.rect.y, original_y)
    
    def test_ball_reset(self):
        """Test ball reset functionality."""
        ball = self.Ball()
        
        # Move ball away from center
        ball.rect.x = 100
        ball.rect.y = 100
        
        ball.reset()
        
        # Ball should be back in center
        self.assertEqual(ball.rect.centerx, 400)  # WINDOW_WIDTH // 2
        self.assertEqual(ball.rect.centery, 300)  # WINDOW_HEIGHT // 2


class TestGameLogic(unittest.TestCase):
    """Test game logic without pygame dependencies."""
    
    def test_scoring_logic(self):
        """Test scoring scenarios."""
        # Simulate ball going off left side (Player 2 scores)
        ball_left = -10
        window_width = 800
        
        if ball_left < 0:
            player2_scores = True
        else:
            player2_scores = False
        
        self.assertTrue(player2_scores)
        
        # Simulate ball going off right side (Player 1 scores)
        ball_right = 810
        
        if ball_right > window_width:
            player1_scores = True
        else:
            player1_scores = False
        
        self.assertTrue(player1_scores)


if __name__ == "__main__":
    unittest.main() 