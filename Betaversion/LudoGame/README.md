# Ludo Game

## Overview
This project is a Java-based Ludo game simulation. It includes a graphical user interface (GUI) using Swing, and simulates a classic Ludo game with four players, each having four pawns. The objective is to move all four pawns to the finish line according to the roll of a dice.
The Ludo Game Simulation project simulates the traditional board game Ludo. The game involves four players, each with four pawns. The pawns move based on the outcome of a dice roll, with the goal of getting all four pawns to the home area before the other players. This project uses Java's Swing library to create the GUI and manage game interactions.
## Table of Contents
1. [Features](#features)
2. [How It Works](#How-It-Works)
3. [Libraries Used](#Libraries-Used)
4. [How to Configure](#How-to-Configure)
5. [Requirements](#requirements)
6. [Installation and Setup](#installation-and-setup)
7. [Gameplay Instructions](#gameplay-instructions)

## Team members
1. [Meenakshi M Kumar](https://github.com/Meenakshimkumar)
2. [Meenakshi Pramod](https://github.com/MeenakshiPramod)
3. [Aleena Bino](https://github.com/aleena24bino)

## Features
- Four-player Ludo game
- Roll dice to move pawns
- Color-coded pawns and paths
- Display winner and restart game

## How It Works
1. **Player Initialization**: Each player is assigned four pawns. Pawns start from a predefined position and move according to dice rolls. 
2. **Board Layou**t: The board is drawn using the Layout class, which handles the rendering of the Ludo board and its squares.
3. **Pawn Movement**: Pawns move along a predefined path based on dice rolls. Each player has a unique path for their pawns.
4. **Dice Roll**: Players take turns to roll the dice by pressing the Enter key. The dice value determines the movement of the pawns.
5. **Winning Condition**: The first player to get all four pawns to the home area wins the game.

## Libraries Used
1. **Swing**: For creating the graphical user interface.
2. **AWT**: For handling graphical rendering and events.

## How to Configure
1. **Java Installation**: Ensure that Java is installed on your system. You can download it from Java SE Downloads.
2. **IDE Setup**: You can use any Java IDE such as IntelliJ IDEA, Eclipse, or NetBeans.
3. **Project Files**: Ensure all Java files (Player.java, Pawn.java, Path.java, Layout.java, Build_Player.java, GameMoves.java) are in the same directory or appropriately configured in your IDE.

## Requirements
- Java Development Kit (JDK) 8 or higher
- An IDE or text editor (e.g., IntelliJ IDEA, Eclipse, VS Code)
  
## Installation and Setup
1. Clone the repository or download the ZIP file and extract it.
   ```bash
   git clone https://github.com/your-username/ludo-game.git
2. Open the Project: Open the project in your preferred IDE.
3. Compile the Code: Compile all Java files. Most IDEs will handle this automatically.
4. Run the Game: Run the GameMoves class. This class contains the main game loop and event listeners.
   - Compile the java files:
    ```bash
     javac LudoGame.java
    ```
   - Run the game:
    ```bash
     java LudoGame
     ```

   - Press Enter to roll the dice.
   - Click on the pawn to move it according to the dice roll.
## Gameplay Instructions
1. Start the game by running the GameMoves class.
2. The game board will be displayed with all players' pawns in their starting positions.
3. Players take turns rolling the dice by pressing the Enter key.
4. Move a pawn by clicking on it. The pawn will move according to the dice roll.
5. The first player to move all four pawns to the home area wins the game.
6. If a player rolls a six, they get an additional turn.
7. Players can capture opponent's pawns by landing on the same square, sending the opponent's pawn back to the starting area.



