# Space Invader Game

## Introduction

Welcome to **Space Invader**, a classic 2D arcade shooter game I built using **Python** and **Pygame**. In this game, you control a spaceship, battling waves of alien invaders to defend Earth. It’s a personal project where I explored game mechanics like sprite movement, collision detection, and dynamic difficulty scaling. 

This project was a fun opportunity to dive into game development, and I learned a lot along the way. Below is a breakdown of how the game works, how to play, and what I plan to add in future versions.

## Features

- **Spaceship Selection**: Choose your favorite spaceship from a variety of designs.
- **Dynamic Alien Waves**: The aliens become more challenging as your score increases.
- **Multiple Backgrounds**: Backgrounds change during gameplay based on your score.
- **Game Over & Scoring**: Survive for as long as you can. The game tracks your high score across sessions.

## How to Play

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/space-invader-game.git
   cd space-invader-game
   ```

2. Install the required dependencies:
   ```bash
   pip install pygame
   ```

3. Run the game:
   ```bash
   python main.py
   ```

### In-Game Instructions

- **Start the Game**: After running the game, use the arrow keys to navigate the spaceship selection menu.
- **Choose Your Spaceship**: Preview different spaceships and backgrounds using the arrow keys. Press **Enter** to confirm your choice.
- **Move and Shoot**: Use the arrow keys to move your spaceship and press the space bar to shoot bullets at incoming aliens.
- **Defend the Earth**: Your goal is to shoot as many alien enemies as possible before they reach you. If they do, it's game over.
- **Score Points**: Every alien hit increases your score. As your score grows, more challenging enemies will appear.

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
```

## Game Preview

The game features a spaceship selection screen where players can choose from different spaceship designs. During gameplay, backgrounds change dynamically based on your score, adding variety to each playthrough.

## Demo Video

Check out a video demo of the game in action [here](https://youtu.be/_9DXpVGpGuU?si=5QhBFcfdteMdx7Mz).

## Challenges

Building this project, I faced a few challenges:

- **Pygame Video System Initialization**: I initially encountered an issue with Pygame not loading correctly, but resolved it by properly setting up the Pygame environment.
- **Image Imports**: There were some bugs when importing and displaying images for enemies and spaceships. Restructuring the directories helped clean this up.
- **Collision Detection**: Implementing smooth and efficient collision detection took a few iterations to get right.

## Future Improvements

Here are a few things I plan to improve in future versions:

- **Enemy AI**: Currently, enemies follow a simple path. I’d like to add more complex behaviors as the game progresses.
- **Power-Ups**: Introduce power-ups that players can collect to boost firepower or shields.
- **Multiplayer Mode**: Adding a local multiplayer mode where two players can defend against alien waves together.

## Credits

This project was built using the Pygame library, and all spaceship and alien images are custom-designed or sourced from open graphics libraries. A special thanks to the Pygame community for their excellent documentation, which made this project possible.

---

I had a great time developing this game and learned a lot throughout the process. If you'd like to contribute or have any suggestions, feel free to fork the repository or reach out to me!
```

You can copy this script and paste it directly into your `README.md` file, and it will render as intended when viewed on GitHub or any other markdown-supported platform.