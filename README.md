# Tic-Tac-Toe with Minimax AI

This project implements a Tic-Tac-Toe game with a graphical user interface using Python's Pygame library. The game includes an AI opponent that uses the Minimax algorithm to play optimally. The AI is designed to challenge players by making the best possible moves, providing a competitive and engaging experience.

## Description

Tic-Tac-Toe with Minimax AI is a sophisticated and interactive game application built to demonstrate the implementation of game theory and artificial intelligence using Python. The project features a classic Tic-Tac-Toe game where users can play against an AI opponent. The AI is powered by the Minimax algorithm, a decision rule used for minimizing the possible loss in a worst-case scenario. This ensures that the AI plays optimally, making it a formidable opponent.

The application is built using Pygame, a popular library for creating games in Python. The graphical interface is designed to be intuitive and user-friendly, allowing players to easily interact with the game. Players can select their preferred symbol (X or O) and make moves by clicking on the game board. The game provides immediate feedback by updating the board and indicating the current player's turn. It also detects the end of the game, displaying the result whether it's a win, loss, or tie, and offers an option to replay.

This project serves as a great example for those looking to learn about game development, AI algorithms, and the practical use of Python and Pygame. It combines theoretical concepts with practical implementation, making it a valuable resource for both beginners and advanced learners.

## Features
- **Player Selection**: Choose to play as X or O.
- **AI Opponent**: The AI uses the Minimax algorithm to make optimal moves.
- **Graphical Interface**: Interactive and user-friendly interface built with Pygame.
- **End Game Detection**: The game recognizes a win, loss, or tie and displays the result.
- **Replay Option**: Option to play again after a game ends.

## Installation

### Prerequisites
- Python 3.6 or higher
- Pygame library

### Steps
1. **Clone the repository**:
    ```bash
    git clone https://github.com/Yehya0/AI-Powered-Tic-Tac-Toe.git
    cd AI-Powered-Tic-Tac-Toe
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the game**:
    ```bash
    python runner.py
    ```

## Usage

### Running the Game
1. Run the `runner.py` script:
    ```bash
    python runner.py
    ```
2. Choose to play as X or O by clicking on the corresponding button.
3. Make your move by clicking on the desired cell in the grid.
4. The AI will make its move automatically.
5. The game ends when there is a winner or a tie, and the result will be displayed.
6. Click on the "Play Again" button to start a new game.

## Code Structure

### Files
- **`tictactoe.py`**: Contains the game logic, including the implementation of the Minimax algorithm.
- **`runner.py`**: Handles the graphical interface and user interactions using Pygame.
- **`requirements.txt`**: Lists the required Python libraries (Pygame).
- **`OpenSans-Regular.ttf`**: Font file used in the graphical interface.

### Key Functions in `tictactoe.py`
- **`initial_state()`**: Returns the initial state of the board.
- **`player(board)`**: Determines the current player.
- **`actions(board)`**: Returns the set of all possible actions.
- **`result(board, action)`**: Returns the board state resulting from a move.
- **`winner(board)`**: Determines the winner, if any.
- **`terminal(board)`**: Checks if the game is over.
- **`utility(board)`**: Evaluates the board for Minimax.
- **`minimax(board)`**: Determines the optimal move using the Minimax algorithm.

### Key Sections in `runner.py`
- **Initialization**: Sets up Pygame and the game window.
- **Event Loop**: Handles user input and updates the game state.
- **Rendering**: Draws the game board and elements on the screen.
- **AI Move**: Calls the Minimax function to determine and execute the AI's move.
- **End Game Handling**: Displays the result and provides an option to replay.

### Gameplay

![Screen Recording - Jun 1, 2024](https://github.com/Yehya0/AI-Powered-Tic-Tac-Toe/assets/89547515/6b4dcb3f-d4f3-4d1b-b049-01aaa7912c0d)

## Contributing

Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
