# 🎉 Welcome to the Guessing Game! 🎉

A simple yet exciting number guessing game created in Python. The game challenges you to guess a randomly selected number between 0 and 100. Each wrong guess brings you closer to discovering the correct number—but can you guess it before you reach too many attempts? Good luck!

## 🌟 How to Play
1. Run the program.
2. A random number between 0 and 100 will be generated for you to guess.
3. Type your guesses in the prompt provided.
4. The game will give feedback after each guess:
   - If your guess is correct, you'll be celebrated as the winner!
   - If your guess is incorrect, you'll receive a message to try again.
5. Continue guessing until you find the right number. Each wrong guess will be counted!

## 🧑‍💻 Code Highlights

- **Random Number Generation:** The game leverages Python’s `random` module to select a new target number each time you play.
- **Exception Handling:** If the player inputs something that isn't a number, the program will catch the error and prompt them to enter a valid number.
- **Friendly Feedback:** The game provides player-friendly messages for each guess, guiding them towards victory with humor and encouragement.

## 🚀 Running the Game

To start the game, simply clone this repository and run the `main.py` file in any Python environment.

```bash
python main.py
```

## Sample Game Session

Here's what a sample game session might look like:

```plaintext
Welcome to the Guessing Game! Can you guess the number?
Type a number between 0 and 100: 45
BAD LUCK! Try again!
Type a number between 0 and 100: 73
WOW! You won! The number was 73, and you guessed it with 2 tries! :D
```

## 🚩 Features to Try Adding
- **Limit the Number of Attempts:** Set a maximum number of guesses allowed, making it more challenging.
- **Hints System:** Add hints like "Higher" or "Lower" after each guess to help players zero in on the answer faster.
- **Difficulty Levels:** Adjust the range or allowed attempts based on difficulty (Easy, Medium, Hard).

## 💡 Fun Facts
Did you know? Games that involve guessing random numbers like this one can help improve memory, attention to detail, and problem-solving skills!

---

Enjoy the game and happy guessing!
