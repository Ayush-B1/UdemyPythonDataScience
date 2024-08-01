import random
from blackjackart import logo
from os import system

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def random_Card():
    new_card = random.choice(cards)
    return new_card


def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has a blackjack"
    elif user_score == 0:
        return "You win with a blackjack"
    elif user_score > 21:
        return "You went over. you lose"
    elif computer_score > 21:
        return "Opponent went over you win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "you lose"


def game():
    user_Card = []
    computer_card = []

    for i in range(2):
        user_Card.append(random_Card())
        computer_card.append(random_Card())

    is_game_over = False

    print(logo)
    while not is_game_over:
        user_score = calculate_score(user_Card)
        comp_score = calculate_score(computer_card)
        print(f"your card is {user_Card} current score {user_score}")
        print(f"computer's first card {computer_card[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input("Type 'y' to get another card or 'n' to pass: ").lower()
            if user_deal == "y":
                user_Card.append(random_Card())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        computer_card.append(random_Card())
        comp_score = calculate_score(computer_card)

    print(f"your final hand {user_Card}, your final score: {user_score}")
    print(f"Computer's final hand {computer_card}, computer's final score: {comp_score}")

    print(compare(user_score, comp_score))

while input("Do you want to play the game 'y' for yes 'N' for no: ") == "y":
    system("clear")
    game()
