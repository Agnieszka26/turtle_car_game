# Turtle Crossing Game

## Overview
Turtle Crossing is a simple Python game built using the `turtle` module. The player controls a turtle attempting to cross a busy road while avoiding moving cars. The goal is to reach the finish line at the top of the screen.

## Features
- Player-controlled turtle movement
- Randomly generated cars moving from right to left
- Increasing difficulty as the player progresses
- Score tracking system

## Game Rules
1. The player can move the turtle **upward** using the **Up Arrow key**.
2. Cars appear at random positions and move across the screen.
3. If the turtle collides with a car, the game **ends**.
4. If the turtle reaches the **finish line**, the score increases, the player resets to the starting position, and the car speed increases.

## Installation & Setup
1. Install Python (if not already installed):
   ```sh
   python --version

2. Clone or download the repository:
    ```sh
    git clone https://github.com/Agnieszka26/turtle_car_game
    cd turtle-car-game
    
## How to Play
  - Use the Up Arrow key to move the turtle upwards.
  - Avoid getting hit by the cars.
  - Reach the top of the screen to increase your score and speed up the game.

## Files
  - main.py - Runs the game logic.
  - player.py - Defines the player character and movement.
  - car_manager.py - Handles car creation and movement.
  - scoreboard.py - Manages the player's score display.

## Credits
This project was built while following the **100 Days of Code** course by **Dr. Angela Yu** on Udemy.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


