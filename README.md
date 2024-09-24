# Space Invader Game

Welcome to my **Space Invader Game** built using the **Pygame** library! This project was inspired by the classic arcade game, with my own twist on the mechanics, design, and overall feel. Whether you’re looking to relive nostalgia or just want to explore some fun gameplay, this project is designed to deliver a smooth, engaging experience.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [File Structure](#file-structure)
- [Game Preview](#game-preview)
- [Demo Video](#demo-video)
- [Challenges](#challenges)
- [Future Improvements](#future-improvements)
- [Credits](#credits)

---

## Overview

This project is a beginner-friendly take on the classic **Space Invader** game. It features spaceships, alien enemies, scoring, high score management, and a simple game loop. I've also integrated animations for celebratory effects when the game ends and added the ability to select spaceships from a menu.

The game is split into multiple files for clarity and structure, making it easier to understand the flow of the game. It's designed with simplicity in mind but leaves room for more advanced features in the future.

---

## Features

- **Multiple Spaceship Choices**: Select different spaceship designs from the menu.
- **Alien Waves**: The game spawns enemies that increase in difficulty as the score increases.
- **High Score Management**: The game stores the highest score between sessions.
- **Celebratory Animations**: Special effects play when the player reaches the end.
- **Smooth Game Loop**: Handles player movement, alien spawning, bullet firing, and collision detection.
- **Multiple Backgrounds**: Preview five different backgrounds in the spaceship selection menu.
- **Modular Structure**: Code is split across different files for readability and ease of modification.

---

## Technologies

- **Python** (v3.8+)
- **Pygame** (v2.0+)

---

## Installation

To run this game on your local machine, follow these steps:

1. Clone the repository:

    ```bash

    git clone https://github.com/yourusername/space-invader-game.git
    cd space-invader-game 

2. Install the required dependencies:

    ```bash
    pip install pygame

3. Run the game:

    ```bash
    python main.py

Back to top
## How to Play

    Start the Game: After running the game, use the arrow keys to navigate the spaceship selection menu.
    Choose Your Spaceship: Preview different spaceships and backgrounds using the arrow keys, and press Enter to confirm your choice.
    Move and Shoot: Use the arrow keys to move your spaceship and press the space bar to shoot bullets at incoming aliens.
    Defend the Earth: Your goal is to shoot as many alien enemies as possible before they reach you. If they do, the game ends.
    Score Points: Every alien hit increases your score, with more challenging enemies appearing as your score grows.

Back to top
## File Structure

The project is divided into several key files and directories to make the code more readable:

    ```bash

    .
    ├── main.py               # The main game loop and event handling
    ├── player.py             # The player's spaceship logic
    ├── alien.py              # The alien enemy logic
    ├── bullet.py             # Bullet firing and collision logic
    ├── settings.py           # Game settings and constants
    ├── utils.py              # Helper functions
    ├── images/
    │   ├── spaceships/       # Spaceship images
    │   ├── enemies/          # Alien enemy images
    │   └── backgrounds/      # Background images
    └── README.md             # This file

Back to top
## Game Preview

The game features a spaceship selection screen where players can choose from different designs. During gameplay, backgrounds change dynamically based on your score.

Back to top
## Demo Video

Check out a video demo of the game in action here.

Back to top
## Challenges

Building this project, I faced a few challenges:

    Pygame Video System Initialization: I initially encountered an issue with Pygame not loading correctly, but resolved it by properly setting up the Pygame environment.
    Image Imports: There were a few bugs when importing and displaying images for enemies and spaceships, but restructuring the directories helped clean this up.
    Collision Detection: Implementing smooth and efficient collision detection took a few iterations to get right.

Back to top
## Future Improvements

Here are a few things I plan to improve in future versions:

    Enemy AI: Currently, enemies follow a simple path. I'd like to add more complex behaviors as the game progresses.
    Power-Ups: Introduce power-ups that players can collect to boost firepower or shields.
    Multiplayer Mode: Adding a local multiplayer mode where two players can defend against alien waves together.

Back to top
## Credits

This project was built using the Pygame library, and all spaceship and alien images are custom-designed or sourced from open graphics libraries. Thanks to the Pygame community for their excellent documentation, which made this project possible.

Back to top