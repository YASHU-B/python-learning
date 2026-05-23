from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

#function to check users guess against actual number
def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("You guessed too high")
        return turns - 1
    elif user_guess < actual_answer:
        print("You guessed too low")
        return turns - 1
    else:
        print(f"You guessed correctly {actual_answer}")


#function to select difficulty
def set_difficulty():
    level = input("Choose a difficulty level (easy or hard): ")
    if level == "easy":
        return  EASY_LEVEL
    else:
        return  HARD_LEVEL
def game():

    #choosing a random number between 1 and 100
    print("Welcome to the Number Guessing GAME")
    print("I am thinking of a number between 1 and 100")
    answer = randint(1,10)



    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} turns left")

        #user guess a number
        guess = int(input("Guess a number between 1 and 10: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You ran out of guesses, you lose")
            return
        elif guess != answer:
            print("Guessed wrong, try again")
game()
