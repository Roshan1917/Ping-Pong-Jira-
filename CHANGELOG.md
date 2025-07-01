# Changelog

All notable changes to the Pong Game project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-07-01

### Added
- Visual feedback with green flashing scores when points are scored
- Console output for paddle hits and scoring events
- Progressive ball speed increase during rallies
- Improved collision detection with direction checking
- Better game responsiveness and feedback

### Changed
- Enhanced scoring system with immediate visual feedback
- Improved ball collision detection for more accurate gameplay
- Increased base ball speed for more exciting gameplay
- Updated game instructions to clarify scoring mechanism

### Fixed
- Ball collision detection now prevents double-bounces
- Scoring is now more responsive and immediate
- Ball speed resets properly after each score

## [1.0.0] - 2025-07-01

### Added
- Complete Pong game implementation using pygame
- AI opponent with intelligent ball-following behavior
- Toggle between AI and human player for Player 2
- Game statistics tracking (scores, session duration, timestamps)
- Automatic game statistics saving to JSON file
- Interactive statistics analysis script
- Professional project setup with dependencies management
- Comprehensive documentation and README

### Features
- Classic Pong gameplay with two paddles and ball
- Smooth 60 FPS gameplay
- Keyboard controls (WASD for Player 1, Arrow keys for Player 2)
- Score tracking with on-screen display
- Game session statistics collection
- Cross-platform compatibility (Windows, macOS, Linux)

### Technical
- Object-oriented design with separate classes for game entities
- Clean code structure with proper separation of concerns
- Comprehensive error handling
- JSON-based statistics storage
- Professional Python packaging with setup.py 