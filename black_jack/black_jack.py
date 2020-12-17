'''My Solution to Day 11 - Blackjack Capstone project from 100 days of Code by Dr. Angela Yu
Rules
Score more than 21  = bust
jack king queen  - each count as 10
A can count as 1 or 11 :  1 if putting user over total of 21 or 11 if not
dealer/computer only show first hand
There can be a draw
While dealer/computer has less than 17 points, they must take more cards'''


import random
from logo import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(logo)
user_input = input(
    "Do you want to play a game of blackjack? type 'y' or 'n': ")

user_cards = []
user_total = 0

comp_cards = []
comp_total = 0


def declare_winner():
    if comp_total > 21:
        print("Opponent Went Over, You Win")
    elif comp_total < user_total:
        print("You have more points,You win")
    elif comp_total > user_total:
        print("Opponent has more points, you loose")
    else:
        print("Draw Game!")


def display_final_result():
    string_cards = ','.join([str(item) for item in user_cards])
    print(f'your cards [{string_cards}], final score:{user_total} ')
    string_comp_cards = ','.join([str(item) for item in comp_cards])
    print(
        f'Computers final hand:[{string_comp_cards}], final score:{comp_total} ')


def display_current_score():
    string_cards = ','.join([str(item) for item in user_cards])
    print(f'your cards [{string_cards}], current score:{user_total}')
    print(f"Computer's first card: {comp_cards[0]}")


if user_input == 'y':
    user_card_one = cards[random.randint(1, len(cards))-1]
    user_card_two = cards[random.randint(1, len(cards))-1]
    if (user_card_one == 11 and user_card_two == 11):
        user_card_two = 1

    user_total = user_card_one + user_card_two
    user_cards.extend([user_card_one, user_card_two])

# deal computer cards
    while(comp_total < 17):
        comp_card = cards[random.randint(1, len(cards))-1]
        if comp_card == 11 and (comp_total+comp_card) > 21:
            comp_card = 1
        comp_cards.append(comp_card)
        comp_total += comp_card

    display_current_score()

    while(True):
        card_option = input("Type 'y' to get another card, type 'n' to pass: ")
        if card_option == "y":
            user_card_additional = cards[random.randint(1, len(cards))-1]
            if (user_card_additional == 11 and (user_total+user_card_additional) > 21):
                user_card_additional = 1
            user_total += user_card_additional
            user_cards.append(user_card_additional)
            if user_total > 21:
                display_final_result()
                print("You went over. You Lose")
                break
            else:
                display_current_score()

        else:
            display_final_result()
            declare_winner()
            break
