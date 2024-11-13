import random

print("Welcome to the guess game! Can you guess the number?")

wrong_guess = 0          # Here we will count the wrong guesses
win_guess = random.randint(0, 100) # This is the number, that randomly was picked by game
print(win_guess) # for testing purpose


while True:
    try:
        players_answer = int(input("Type the number between 0 and 100: "))

        if players_answer == win_guess:  #checking if answer is right
            print(f"WOW! You won! The number was {win_guess} and you guessed it only with {wrong_guess + 1} tries! :D")
            break  # the game is over, cause player won!

        print("BAD LUCK! Try again!") # If wrong, we give another chance to the player
        wrong_guess += 1

    except Exception:
        print("PLEASE USE THE NUMBERS! :(")
        wrong_guess += 1


"""
So I did everything almost right, but i wanted to loop our game after players wrong input type, couldn't do it on my own, so i used AI
for correct placement.
Commented part is my attempt.
"""

# try:
#   players_answer = int(input("Type the number between 0 and 100: "))

#   while players_answer != win_guess:
#       print("BAD LUCK! Try again!")
#       players_answer = int(input("Type the number between 0 and 100: "))
#       wrong_guess += 1
#   else:
#         print(f"WOW! You won! The number was {win_guess} and you guessed it only with {wrong_guess} try! :D")
# except Exception:
#   print("PLEASE USE THE NUMBERS! :(")
#   players_answer = int(input("Type the number between 0 and 100: "))
