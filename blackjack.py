import random

def dealcard():
    cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "draw"
    elif c_score == 0:
        return "lose, opponent has blackjack"
    elif u_score == 0:
        return "win with a blackjack"
    elif u_score > 21:
        return " you went over , You Lose"
    elif c_score > 21:
        return "Opponent went over,  You Win"
    elif u_score > c_score:
        return "You Win"
    else:
        return "You Lose"

def play_game():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False


    for _ in range(2):
        user_cards.append(dealcard())
        computer_cards.append(dealcard())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"user: {user_cards}, current score: {user_score}")
        print(f"computer: {computer_cards[0]}")

        if user_score == 0 and computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("type y to get another card,type n to pass")
            if user_should_deal == "y":
                user_cards.append(dealcard())
            else:
                is_game_over = True



    while computer_score != 0 and computer_score < 17:
        computer_cards.append(dealcard())
        computer_score = calculate_score(computer_cards)

    print(f"user: {user_cards}, current score: {user_score}")
    print(f"computer: {computer_cards}, current score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play blackjack (y/n) ").lower() == "y":
    play_game()
    print("Thank you for playing")
