"""
Game Statistics and Project Demo for Pong Game
This script demonstrates game statistics tracking and project management concepts.
"""

import json
import os
from datetime import datetime

class PongGameStats:
    def __init__(self):
        self.project_name = "Pong Game"
        self.game_stats_file = "game_stats.json"
        
    def load_game_stats(self):
        """Load the latest game statistics"""
        try:
            if os.path.exists(self.game_stats_file):
                with open(self.game_stats_file, 'r') as f:
                    return json.load(f)
            return None
        except Exception as e:
            print(f"Error loading game stats: {e}")
            return None
            
    def create_game_session_report(self):
        """Create a detailed report of the latest game session"""
        stats = self.load_game_stats()
        if not stats:
            print("No game stats found. Play the game first!")
            return
            
        report_title = f"Pong Game Session Report - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        report_content = f"""
# {report_title}

## Session Statistics
- Player 1 Score: {stats['player1_score']}
- Player 2 Score: {stats['player2_score']}
- Games Played: {stats['games_played']}
- Session Duration: {stats['session_duration']}
- Timestamp: {stats['timestamp']}

## Game Performance Analysis
- Winner: {'Player 1' if stats['player1_score'] > stats['player2_score'] else 'Player 2' if stats['player2_score'] > stats['player1_score'] else 'Tie'}
- Total Points Scored: {stats['player1_score'] + stats['player2_score']}
- Average Score per Player: {(stats['player1_score'] + stats['player2_score']) / 2:.1f}

## Session Summary
This gaming session was automatically recorded from the Pong game.
Session data can be used for performance tracking and game improvement analysis.
        """
        
        print("=== GAME SESSION REPORT ===")
        print(report_content)
        
        # Save report to file
        try:
            report_filename = f"game_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(report_filename, 'w') as f:
                f.write(report_content)
            print(f"\n📄 Report saved to: {report_filename}")
        except Exception as e:
            print(f"Error saving report: {e}")
        
    def suggest_game_improvements(self):
        """Suggest potential improvements for the Pong game"""
        improvements = [
            {
                "title": "Add Power-ups to Pong Game",
                "description": "Implement power-ups that randomly appear and affect ball speed or paddle size",
                "category": "Gameplay Enhancement"
            },
            {
                "title": "Implement Multiplayer Network Support",
                "description": "Allow two players to play Pong over network connection",
                "category": "Networking Feature"
            },
            {
                "title": "Add Sound Effects and Music",
                "description": "Enhance game experience with paddle hits, scoring sounds, and background music",
                "category": "Audio Enhancement"
            },
            {
                "title": "Create Tournament Mode",
                "description": "Add tournament bracket system for multiple players",
                "category": "Game Mode"
            },
            {
                "title": "Add Visual Effects",
                "description": "Implement particle effects, ball trails, and screen shake",
                "category": "Visual Enhancement"
            }
        ]
        
        print("=== GAME IMPROVEMENT SUGGESTIONS ===\n")
        for i, improvement in enumerate(improvements, 1):
            print(f"{i}. {improvement['title']}")
            print(f"   Category: {improvement['category']}")
            print(f"   Description: {improvement['description']}")
            print()
            
        print("These suggestions could be implemented as future features!")
        
    def demonstrate_project_management(self):
        """Demonstrate project management concepts for the Pong game"""
        print("=== PONG GAME PROJECT MANAGEMENT DEMO ===\n")
        
        print("This demo shows project management concepts for game development.\n")
        
        print("📊 PROJECT TRACKING CONCEPTS:")
        concepts = [
            "Feature Planning - Organize game improvements into releases",
            "Bug Tracking - Log and prioritize game issues", 
            "Performance Monitoring - Track game statistics over time",
            "User Feedback - Collect and analyze player suggestions",
            "Release Management - Plan and execute game updates",
            "Documentation - Maintain game development records"
        ]
        
        for concept in concepts:
            print(f"  • {concept}")
            
        print(f"\n🎯 PROJECT WORKFLOW IDEAS:")
        workflow_ideas = [
            "Create tasks for each game feature development",
            "Log bugs found during playtesting",
            "Track feature requests from players",
            "Organize development in sprint cycles",
            "Create dashboards for game analytics",
            "Plan releases with feature roadmaps"
        ]
        
        for idea in workflow_ideas:
            print(f"  • {idea}")
            
        print(f"\n🚀 GETTING STARTED WITH PROJECT MANAGEMENT:")
        print("1. Define your game development goals")
        print("2. Break down features into manageable tasks")
        print("3. Track progress and collect feedback")
        print("4. Plan regular updates and improvements")
        print("5. Maintain documentation and statistics")

def main():
    game_stats = PongGameStats()
    
    print("Welcome to the Pong Game Statistics and Project Demo!")
    print("This tool helps you analyze game performance and explore project management concepts.\n")
    
    while True:
        print("\nOptions:")
        print("1. Show project management demonstration")
        print("2. Load and display game statistics")
        print("3. Show game improvement suggestions")
        print("4. Create detailed game session report")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            game_stats.demonstrate_project_management()
        elif choice == "2":
            stats = game_stats.load_game_stats()
            if stats:
                print("\n=== LATEST GAME STATISTICS ===")
                for key, value in stats.items():
                    print(f"  {key.replace('_', ' ').title()}: {value}")
            else:
                print("No game statistics found. Play the Pong game first!")
        elif choice == "3":
            game_stats.suggest_game_improvements()
        elif choice == "4":
            game_stats.create_game_session_report()
        elif choice == "5":
            print("Thanks for exploring the Pong Game Project Demo!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 