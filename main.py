import random

print("Welcome to the guess game! Can you guess the number?")

wrong_guess = 0          # Here we will count the wrong guesses
win_guess = random.randint(0, 100) # This is the number, that randomly was picked by game
print(win_guess)


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
# если переменная не была объявлена раньше
while True:
    try:
        players_answer = int(input("Type the number between 0 and 100: "))

        # Проверка, угадал ли игрок число
        if players_answer == win_guess:
            print(f"WOW! You won! The number was {win_guess} and you guessed it only with {wrong_guess + 1} tries! :D")
            break  # завершаем цикл, если число угадано

        # Если не угадал, даём шанс попробовать ещё раз
        print("BAD LUCK! Try again!")
        wrong_guess += 1

    except ValueError:
        print("PLEASE USE THE NUMBERS! :(")
        wrong_guess += 1
