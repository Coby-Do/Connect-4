# AI-Enhanced Connect Four

## Introduction
This project is an AI-enhanced Connect Four game that allows users to play against an AI player. The game uses a resizable board, and the objective is to connect four checkers in a row vertically, horizontally, or diagonally.

# Languages Used:
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

## Features
- Connect Four game with AI player
- Customizable board size (width and height)
- AI player with varying levels of difficulty
- Different tie-breaking strategies for AI (leftmost, rightmost, random)
- Players can play against each other or against the AI
- Terminal-based Gameboard visualization

## Installation
No additional libraries are required to run this project. Simply clone the repository and execute the Python script.

## Usage
To start a new game, execute the `main()` function at the end of the script. You can customize the board size and level of difficulty by modifying the parameters passed to the `Connect4` and `Player` classes.

Example:
```python
board = Connect4(7, 6)  # Creates a 7x6 board
p = Player('x', 'Left', 2)  # AI player with 'x' as its symbol, 'Left' tie-breaking strategy, and ply of 2
board.playGameWith(p)  # Starts the game with the specified AI player
```
Gameboard Visualization in Terminal:

<img width="155" alt="image" src="https://user-images.githubusercontent.com/111834642/227357116-63c6337c-1f5e-47f5-9cc7-a107cb0fbcfc.png">

# Classes and Functions

## Connect4 Class

- <strong>__init__(self, width, height, window=None)</strong>: Initializes the Connect4 board with the specified width and height
- <strong>__repr__(self)</strong>: Displays the game board
- <strong>clear(self)</strong>: Clears the board
- <strong>allowsMove(self, col)</strong>: Checks if a move is allowed in the specified column
- <strong>addMove(self, col, ox)</strong>: Adds a move to the board
- <strong>delMove(self, col)</strong>: Removes the top checker from the specified column
- <strong>isFull(self)</strong>: Checks if the board is full
- <strong>winsFor(self, ox)</strong>: Checks if the specified player has won the game
- <strong>hostGame(self)</strong>: Controls player turns for a game between two human players
- <strong>playGameWith(self, Player)</strong>: Controls player turns for a game between a human player and an AI player

## Player Class

- <strong>__init__(self, ox, tbt, ply)</strong>: Initializes the Player with the specified symbol, tie-breaking strategy, and ply
- <strong>scoresBoard(self, board)</strong>: Calculates the scores for each column on the board
- <strong>switchPlayers(self, ox)</strong>: Switches the current player's symbol
- <strong>scoresFor(self, board, ox, ply)</strong>: Returns a list of scores for each column
- <strong>tieBreakMove(self, scores)</strong>: Determines the best move based on the specified tie-breaking strategy
- <strong>nextMove(self, board)</strong>: Returns the best column number based on the best score

## Main Function

- <strong>main()</strong>: Initializes the game with the specified board size and level of difficulty

## License

This project is released under the MIT License. Please see the 'LICENSE' file for more information.
