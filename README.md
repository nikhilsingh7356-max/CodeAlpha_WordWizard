# Word Wizard 🧙 (Hangman Game)
 
A simple text-based Hangman game built in Python, where the player guesses a secret word one letter at a time before running out of incorrect guesses.
 
> Built as part of the **CodeAlpha Python Programming Internship** — Task 1.
 
## 🎮 How It Works
 
- The program randomly picks a secret word from a small predefined list.
- The player guesses one letter at a time.
- Correctly guessed letters are revealed in the word.
- Incorrect guesses reduce the player's remaining attempts, drawn as ASCII hangman art.
- The game ends when the player either guesses the full word (win) or makes 6 incorrect guesses (lose).
- After each round, the player can choose to play again.
## ✨ Features
 
- 5 predefined words — no external file or API required
- Maximum of 6 incorrect guesses, with ASCII hangman art that updates each wrong guess
- Input validation (rejects empty input, multiple characters, non-letters, and repeated guesses)
- Replay option after each game
- Clean, beginner-friendly console output
## 🧠 Key Concepts Used
 
| Concept | Where it's used |
|---|---|
| `random` | Picking a random word from the word list |
| `while` loop | Driving the main game loop until win/loss |
| `if / else` | Checking guesses, win/loss conditions, input validation |
| Strings | Building the masked word display (e.g. `_ y t _ o n`) |
| Lists | Storing the word bank and tracking guessed letters |
 
## 🚀 How to Run
 
1. Make sure you have **Python 3** installed.
2. Download or clone this repository.
3. Run the game from your terminal:
```bash
   python3 word_wizard.py
```
4. Follow the on-screen prompts to guess letters.
## 📂 Project Structure
 
```
CodeAlpha_WordWizard/
├── word_wizard.py     # Main game source code
└── README.md           # Project documentation
```
 
## 🖥️ Example Gameplay
 
```
========================================
WELCOME TO WORD WIZARD
========================================
The word has 6 letters. You may make 6 incorrect guesses.
 
Word: _ _ _ _ _ _
 
Guess a letter: p
Good guess! 'p' is in the word.
```
 
## 🙋 Author
 
Built as part of the CodeAlpha Internship Program.
 

