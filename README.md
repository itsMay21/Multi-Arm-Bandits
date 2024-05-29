# Multi-Arm Bandit Task Game
Multi-Arm Bandit Decision Game


## Project Description
The Five-Armed Bandit Task Game is an interactive decision-making game designed to study how individuals make decisions under time pressure. The project features two versions: a five-arm bandit and a three-arm bandit. The aim is to select an arm within a given time limit, accumulate rewards, and ultimately understand decision-making patterns and strategies.

## Table of Contents
1. [Project Description](#project-description)
2. [Installation and Setup](#installation-and-setup)
3. [How to Play](#how-to-play)
4. [Game Controls](#game-controls)
5. [Credits](#credits)

## Installation and Setup
To run the game locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/itsMay21/Multi-Arm-Bandits.git
   cd five-armed-bandit-game
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Then, install the required dependencies:
   ```bash
   pip install pygame
   ```

3. **Run the Game**:
   Navigate to the project directory and run the game:
   ```bash
   python five_arm_bandit.py
   ```
   
4. **Note**:
   For the three-arm version, similar steps apply but with `three_arm_bandit.py`.

## How to Play
The game involves selecting one of the five (or three) bandit arms within a limited time to earn rewards. Here's how to start and play the game:

1. **Game Start**:
   - Enter your name when prompted.
   - Select your emotional state using the slider (-5 to 5 scale).

2. **Game Settings**:
   - Enter the time limit per trial (in 100s of milliseconds).
   - Enter the number of trials you wish to play.

3. **Gameplay**:
   - Each round, select an arm (A-E) before the time runs out.
   - Your score for each round depends on the rewards from the selected arm.

4. **End of Game**:
   - After the final round, the game saves your data to a CSV file (`bandit_data.csv`).

## Game Controls
- **Mouse**:
  - Click on the bandit arms displayed on the screen to select them.
- **Keyboard**:
  - Use keys `Q`, `W`, `E`, `R`, `T` to select arms A, B, C, D, E respectively.(`Q`, `W`, `E`for 3- ARM Bandit task)

## Credits
- **Developer**: Mayank Saini
- **GitHub**: [itsMay21](https://github.com/itsMay21)


Enjoy playing the Five-Armed Bandit Task Game and exploring decision-making under pressure!