# 🏓 Pong Game

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Game: Pong](https://img.shields.io/badge/Game-Pong-green.svg)]()

A classic Pong game implementation in Python using pygame. Perfect for learning game development, practicing Python programming, and exploring game physics.

## 🎮 Features

### Game Features
- **Classic Pong Gameplay** - Two paddles and a bouncing ball
- **AI Opponent** - Intelligent computer player (toggleable)
- **Responsive Controls** - Smooth keyboard input handling
- **Score Tracking** - Real-time scoring with visual feedback
- **Progressive Difficulty** - Ball speed increases during rallies
- **Visual Feedback** - Score flashing and console output
- **60 FPS Gameplay** - Smooth, consistent performance

### Technical Features
- **Object-Oriented Design** - Clean, maintainable code structure
- **Game Statistics** - Automatic session tracking and analysis
- **Configurable Settings** - Easy customization via config file
- **Cross-Platform** - Works on Windows, macOS, and Linux
- **Professional Structure** - GitHub-ready project organization

## 🚀 Quick Start

### Installation

**Option 1: Automated Setup (Recommended)**
```bash
git clone https://github.com/roshan-r/pong-game.git
cd pong-game
python setup.py
```

**Option 2: Manual Setup**
```bash
git clone https://github.com/roshan-r/pong-game.git
cd pong-game
pip install -r requirements.txt
```

### Run the Game
```bash
python pong_game.py
```

## 🕹️ How to Play

### Controls
- **Player 1 (Left Paddle):** `W` / `S` keys
- **Player 2 (Right Paddle):** `↑` / `↓` arrow keys (when AI disabled)
- **Toggle AI:** Press `A`
- **Quit Game:** Press `ESC`

### Scoring
- Score when your opponent **misses** the ball
- Ball must go completely off their side of the screen
- Scores flash green when updated
- Console shows hit detection and scoring events

## 📁 Project Structure

```
pong-game/
├── 🎮 Core Game Files
│   ├── pong_game.py          # Main game implementation
│   ├── game_stats.py         # Statistics tracking and analysis
│   └── config.py             # Game configuration settings
│
├── 📦 Setup & Dependencies
│   ├── setup.py              # Installation script
│   ├── requirements.txt      # Python dependencies
│   └── pyproject.toml         # Modern Python project config
│
├── 📚 Documentation
│   ├── README.md             # Project overview (this file)
│   ├── CHANGELOG.md          # Version history
│   ├── CONTRIBUTING.md       # Contribution guidelines
│   └── LICENSE               # MIT license
│
├── 🧪 Testing
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_game.py      # Unit tests
│
└── 🔧 Development
    └── .gitignore            # Git ignore rules
```

## 📊 Game Analysis

After playing, analyze your performance:
```bash
python game_stats.py
```

### Available Analysis Options:
1. **Game Statistics** - View your latest session data
2. **Session Reports** - Detailed performance analysis
3. **Improvement Suggestions** - Ideas for game enhancements
4. **Project Management Demo** - Development workflow concepts

## ⚙️ Customization

Edit `config.py` to customize:
- **Game Speed** - Paddle and ball speeds
- **Visual Settings** - Colors, sizes, window dimensions
- **AI Behavior** - Reaction delays and difficulty
- **Game Features** - Enable/disable progressive speed, scoring effects
- **Controls** - Remap keyboard controls

## 🧪 Testing

Run the test suite:
```bash
python -m pytest tests/
```

Or run individual tests:
```bash
python tests/test_game.py
```

## 🚀 Development Ideas

### Beginner Features
- [ ] Pause functionality
- [ ] Different difficulty levels
- [ ] Sound effects
- [ ] Custom paddle colors
- [ ] Score limit options

### Advanced Features
- [ ] Multiplayer network support
- [ ] Tournament mode
- [ ] Power-ups and special effects
- [ ] Replay system
- [ ] Leaderboards
- [ ] Advanced AI strategies

### Technical Improvements
- [ ] Configuration GUI
- [ ] Better collision detection
- [ ] Performance optimizations
- [ ] Game state management
- [ ] Event system

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Development setup instructions
- Code style guidelines
- Feature suggestions
- Bug reporting process
- Pull request workflow

## 📈 Version History

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

**Current Version: 1.1.0**
- Enhanced scoring system with visual feedback
- Improved collision detection
- Better game responsiveness
- Progressive ball speed during rallies

## 🛠️ Requirements

- **Python 3.7+**
- **pygame 2.5.0+**
- **Cross-platform support** (Windows, macOS, Linux)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Learning Objectives

This project demonstrates:
- **Object-Oriented Programming** - Classes, inheritance, encapsulation
- **Game Development** - Game loops, collision detection, user input
- **Python Best Practices** - Code organization, documentation, testing
- **Project Management** - Version control, documentation, issue tracking

## 💡 Educational Use

Perfect for:
- **Python beginners** learning OOP concepts
- **Game development students** exploring pygame
- **Computer science courses** as a practical project
- **Portfolio projects** demonstrating programming skills

## 🏆 Acknowledgments

- Inspired by the classic Pong arcade game (1972)
- Built with [pygame](https://pygame.org) community library
- Following Python community best practices

---

**Made with ❤️ for learning and fun!** 🎮

*Star ⭐ this repository if you found it helpful!* 