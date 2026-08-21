Number Guessing Game 🎯

📌 Project Description

The Number Guessing Game is a simple Python-based game in which the computer randomly selects a number between 1 and 100. The player has a limited number of attempts to guess the correct number.

After every guess, the game provides a hint:

- Too Low – if the guessed number is smaller.
- Too High – if the guessed number is larger.
- Correct – if the player guesses the number successfully.

The game also keeps track of the player's attempts, score, total rounds, and final score.

✨ Features

- Random number generation
- Number range from 1 to 100
- Maximum 7 attempts per round
- Too High / Too Low hints
- Score calculation
- Multiple rounds of gameplay
- Total score tracking
- Invalid input handling
- Interactive console-based interface

🛠️ Technologies Used

- Programming Language: Python
- Library Used: "random"
- Interface: Command Line / Console

📚 Python Library

The project uses the built-in Python "random" library.

import random

It is used to generate a random number:

random.randint(1, 100)

🎮 How to Play

1. Run the Python program.
2. The computer selects a random number between 1 and 100.
3. Enter your guess.
4. The game gives a hint if your guess is too high or too low.
5. Try to guess the number within 7 attempts.
6. If you guess correctly, your score is calculated.
7. Choose whether you want to play another round.
8. At the end, your total score and rounds played are displayed.

🧮 Scoring System

The score is calculated based on the number of attempts.

Score = (Maximum Attempts - Attempts + 1) × 10

Fewer attempts result in a higher score.


▶️ How to Run

Make sure Python is installed on your computer.

Run the program using:

python number_guessing_game.py

📂 Project Structure

Number-Guessing-Game/
│
├── number_guessing_game.py
└── README.md

🎯 Objective

The main objective of this project is to demonstrate basic Python programming concepts such as:

- Variables
- Functions
- Loops
- Conditional statements
- User input
- Exception handling
- Random number generation

👨‍💻 Author

Nagesh Atmaram Raut

📄 License

This project is created for educational purposes.
